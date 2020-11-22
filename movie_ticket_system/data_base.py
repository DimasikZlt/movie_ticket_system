import sqlite3
from typing import Any

from genre import Genre
from movie import Movie
from movie_hall import MovieHall
from role import Role
from session import Session
from user import User


class DataBase:
    def __init__(self, name: str, db_connect):
        self.name = name
        self.db_connect = db_connect
        self.cur = db_connect.cursor()
        self.role = None
        self.user = None
        self.genre = None
        self.movie = None
        self.movie_hall = None
        self.session = None

    @classmethod
    def connect(cls, name: str):
        db_connect = sqlite3.connect(name)
        db = cls(name, db_connect)
        db.create_tables()
        return db

    def execute(self, sql_query: Any):
        if isinstance(sql_query, tuple):
            self.cur.execute(*sql_query)
        else:
            self.cur.execute(sql_query)
        self.db_connect.commit()

    def select_all(self, sql_query: Any):
        if isinstance(sql_query, tuple):
            return self.cur.execute(*sql_query).fetchall()
        return self.cur.execute(sql_query).fetchall()

    def select_one(self, sql_query: Any):
        if isinstance(sql_query, tuple):
            return self.cur.execute(*sql_query).fetchone()
        return self.cur.execute(sql_query).fetchone()

    def has_table(self, table_name: str) -> bool:
        request = """
            SELECT COUNT(*) 
            FROM sqlite_master 
            WHERE type = 'table' 
            AND name = ?
        """, (table_name,)
        return self.cur.execute(*request).fetchone()[0]

    def close(self):
        self.db_connect.close()

    def create_tables(self):
        self.role = Role.create_table(self)
        self.user = User.create_table(self, self.role)
        self.genre = Genre.create_table(self)
        self.movie = Movie.create_table(self, self.genre)
        self.movie_hall = MovieHall.create_table(self)
        self.session = Session.create_table(self, self.movie, self.movie_hall)

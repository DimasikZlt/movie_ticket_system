from typing import List

from genre import Genre
from movie import Movie
from movie_hall import MovieHall
from role import Role
from session import Session
from table import Table
from user import User


class ApplicationDB:
    def __init__(self, tables: List[Table]):
        self.genre = None
        self.role = None
        self.user = None
        self.movie = None
        self.movie_hall = None
        self.session = None

    @classmethod
    def create_tables(cls):
        app_db = cls([])
        app_db.genre = Genre.create_table()
        app_db.role = Role.create_table()
        app_db.user = User.create_table()
        # app_db.movie = Movie.create_table()
        # app_db.movie_hall = MovieHall.create_table()
        # app_db.session = Session.create_table()

from typing import List

from data_base import DataBase
from genre_table import GenreTable
from movie_table import MovieTable
from movie_hall_table import MovieHallTable
from role_table import RoleTable
from session_table import SessionTable
from table import Table
from user_table import UserTable


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
        db_path = '../data/movie_ticket_system.sqlite'
        data_base = DataBase.connect(db_path)
        app_db = cls([])
        app_db.genre = GenreTable.create_table(data_base)
        app_db.role = RoleTable.create_table(data_base)
        app_db.user = UserTable.create_table(data_base)
        app_db.movie = MovieTable.create_table(data_base)
        app_db.movie_hall = MovieHallTable.create_table(data_base)
        app_db.session = SessionTable.create_table(data_base)

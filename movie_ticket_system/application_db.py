from genre_table import GenreTable
from movie_hall_table import MovieHallTable
from movie_table import MovieTable
from role_table import RoleTable
from session_table import SessionTable
from user_table import UserTable


class ApplicationDB:
    def __init__(self):
        self.genre = GenreTable.create_table()
        self.role = RoleTable.create_table()
        self.user = UserTable.create_table()
        self.movie = MovieTable.create_table()
        self.movie_hall = MovieHallTable.create_table()
        self.session = SessionTable.create_table()

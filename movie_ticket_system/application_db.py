from genre_table import GenreTable
from movie_hall_table import MovieHallTable
from movie_table import MovieTable
from role_table import RoleTable
from row_table import RowTable
from seat_table import SeatTable
from session_table import SessionTable
from ticket_table import TicketTable
from user_table import UserTable


class ApplicationDB:
    def __init__(self):
        self.genre = GenreTable.create_table()
        self.role = RoleTable.create_table()
        self.user = UserTable.create_table()
        self.movie = MovieTable.create_table()
        self.movie_hall = MovieHallTable.create_table()
        self.session = SessionTable.create_table()
        self.row = RowTable.create_table()
        self.ticket = TicketTable.create_table()

    def close(self):
        self.session.data_base.close()

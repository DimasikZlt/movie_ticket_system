from row_table import RowTable
from tools.field_pair_tuple import FieldPair


class SeatTable(RowTable):
    def add(self, row_id: int, seat_number: int):
        request = """
            INSERT INTO seat(row_id, seat_number) VALUES(?, ?)
        """, (row_id, seat_number)
        self.data_base.execute(request)

    def remove(self, row_id: int, seat_number: int):
        request = """
            DELETE FROM seat
            WHERE row_id = ?
            AND seat_number = ?
        """, (row_id, seat_number)
        self.data_base.execute(request)

    def fill_seats(self):
        movie_halls = self.get_all('movie_hall')
        for _, name, rows_count, seats_count in movie_halls:
            for row_number in range(1, rows_count + 1):
                super().add(name, row_number)
                row_id, *_ = self.get_by_field('row', FieldPair('row_number', row_number))
                for seat_number in range(1, seats_count + 1):
                    self.add(row_id, seat_number)

    @classmethod
    def create_table(cls):
        seat = cls()
        if not seat.data_base.has_table('seat'):
            request = """
                CREATE TABLE seat (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    row_id INTEGER NOT NULL REFERENCES row(id),
                    seat_number INTEGER NOT NULL
                );
            """
            seat.data_base.execute(request)
            seat.fill_seats()
        return seat

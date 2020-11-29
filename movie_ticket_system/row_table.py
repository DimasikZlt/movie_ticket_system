from seat_table import SeatTable
from tools.field_pair_tuple import FieldPair


class RowTable(SeatTable):
    def get_row_id(self, movie_hall_id: int, row_number: int) -> int:
        request = f"""
                    SELECT id
                    FROM row
                    WHERE movie_hall_id = ?
                    AND row_number = ?
                """, (movie_hall_id, row_number)
        return self.data_base.select_one(request)[0]

    def get_movie_hall_id(self, movie_hall: str) -> int:
        movie_hall_id, *_ = super().get_by_field('movie_hall', FieldPair('name', movie_hall))
        return movie_hall_id

    def add(self, movie_hall_id: int, row_number: int):
        request = """
            INSERT INTO row(movie_hall_id, row_number) VALUES(?, ?)
        """, (movie_hall_id, row_number)
        self.data_base.execute(request)

    def remove(self, movie_hall: str, row_number: int):
        request = """
            DELETE FROM row
            WHERE movie_hall_id = ?
            AND row_number = ?
        """, (self.get_movie_hall_id(movie_hall), row_number)
        self.data_base.execute(request)

    def fill_rows(self, seat: SeatTable):
        movie_halls = super().get_all('movie_hall')
        for movie_halls_id, _, rows_count, seat_count in movie_halls:
            for row_number in range(1, rows_count + 1):
                self.add(movie_halls_id, row_number)
                row_id = self.get_row_id(movie_halls_id, row_number)
                seat.fill_seats(row_id, seat_count)

    @classmethod
    def create_table(cls):
        seat = SeatTable.create_table()
        row = cls()
        if not row.data_base.has_table('row'):
            request = """
                CREATE TABLE row (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    movie_hall_id INTEGER NOT NULL REFERENCES movie_hall(id),
                    row_number INTEGER NOT NULL
                );
            """
            row.data_base.execute(request)
            row.fill_rows(seat)
        return row

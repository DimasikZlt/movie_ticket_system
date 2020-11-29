from table import Table
from tools.field_pair_tuple import FieldPair


class MovieHallTable(Table):
    movie_hall_db_fields = (
        'id',
        'name',
        'rows_count',
        'seats_count',
    )

    def add(self, name: str, rows_count: int, seats_count: int):
        request = """
            INSERT INTO movie_hall(name, rows_count, seats_count) VALUES(?, ?, ?)
        """, (name, rows_count, seats_count)
        self.data_base.execute(request)

    def remove(self, name):
        request = """
            DELETE FROM movie_hall
            WHERE name = ?
        """, (name,)
        self.data_base.execute(request)

    def get_all(self, table_name: str):
        request = f"""
            SELECT id, name, rows_count, seats_count
            FROM {table_name}
        """
        return self.data_base.select_all(request)

    def get_by_field(self, table_name: str, field_pair: FieldPair):
        if field_pair.field_name in self.movie_hall_db_fields:
            request = f"""
                SELECT id, name, rows_count, seats_count
                FROM {table_name}
                WHERE movie_hall.{field_pair.field_name} = ?
            """, (field_pair.field_value,)
            return self.data_base.select_one(request)

    @classmethod
    def create_table(cls):
        movie_hall = cls()
        if not movie_hall.data_base.has_table('movie_hall'):
            request = """
                CREATE TABLE movie_hall (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE,
                    rows_count INTEGER NOT NULL,
                    seats_count INTEGER NOT NULL
                );
            """
            movie_hall.data_base.execute(request)
            movie_hall.add('king', 7, 10)
        return movie_hall

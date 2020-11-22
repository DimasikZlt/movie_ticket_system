from __future__ import annotations

from typing import TYPE_CHECKING

from tools.field_pair_tuple import FieldPair

if TYPE_CHECKING:
    from data_base import DataBase


class MovieHall:
    def __init__(self, data_base: DataBase):
        self.data_base = data_base
        self.movie_hall_db_fields = (
            'id',
            'name',
            'rows_count',
            'seats_count'
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

    def get_all(self):
        request = """
            SELECT id, name, rows_count, seats_count
            FROM movie_hall
        """
        return self.data_base.select_all(request)

    def get_by_field(self, field_pair: FieldPair):
        if field_pair.field_name in self.movie_hall_db_fields:
            request = f"""
                SELECT id, name, rows_count, seats_count
                FROM movie_hall
                WHERE movie_hall.{field_pair.field_name} = ?
            """, (field_pair.field_value,)
            return self.data_base.select_one(request)

    @classmethod
    def create_table(cls, data_base):
        movie_hall = cls(data_base)
        if not data_base.has_table('movie_hall'):
            request = """
                CREATE TABLE movie_hall (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE,
                    rows_count INTEGER NOT NULL,
                    seats_count INTEGER NOT NULL
                );
            """
            data_base.execute(request)
            movie_hall.add('king', 7, 10)
        return movie_hall

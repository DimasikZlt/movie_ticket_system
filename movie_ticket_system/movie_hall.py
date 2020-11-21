from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data_base import DataBase


class MovieHall:
    def __init__(self, data_base: DataBase):
        self.data_base = data_base

    def add(self, name, rows_count, seats_count):
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

    @classmethod
    def create_table(cls, data_base):
        movie_hall = cls(data_base)
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

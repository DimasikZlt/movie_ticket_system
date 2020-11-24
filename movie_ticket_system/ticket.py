from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data_base import DataBase


class Ticket:
    def __init__(self):
        pass

    def add(self):
        pass

    def remove(self):
        pass

    @classmethod
    def create_table(cls, data_base: DataBase):
        request = """
            CREATE TABLE ticket (
                id INTEGER PRIMARY KEY,
                session_id INTEGER NOT NULL REFERENCES session(id),
                row INTEGER NOT NULL,
                seat INTEGER NOT NULL,
                movie_hall_id INTEGER NOT NULL REFERENCES movie_hall(id),
                price INTEGER NOT NULL
            );
        """
        data_base.execute(request)

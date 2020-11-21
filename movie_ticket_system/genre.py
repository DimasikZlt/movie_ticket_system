from __future__ import annotations

from typing import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data_base import DataBase

from tools.field_pair_tuple import FieldPair
from tools.yaml_loader import load_yaml


class Genre:
    DEFAULT_MOVIES_FILE = '../data/movies.yml'

    def __init__(self, data_base: DataBase):
        self.data_base = data_base

    def add(self, name: str):
        request = """
            INSERT INTO genre(name) VALUES(?)
        """, (name,)
        self.data_base.execute(request)

    def remove(self, name):
        request = """
            DELETE FROM genre
            WHERE name = ?
        """, (name,)
        self.data_base.execute(request)

    def get_all(self):
        request = """
            SELECT id, name
            FROM genre
        """
        return self.data_base.select_all(request)

    def get_by_field(self, field_pair: FieldPair):
        request = f"""
            SELECT id, name
            FROM genre
            WHERE {field_pair.field_name} = ?
        """, (field_pair.field_value,)
        return self.data_base.select_one(request)

    def load_default_value(self, loader: Callable, movies_file: str):
        genres = set(
            movie.get('genre')
            for movie in loader(movies_file).get('movies')
            if movie.get('genre')
        )
        for genre in genres:
            self.add(genre)

    @classmethod
    def create_table(cls, data_base):
        genre = cls(data_base)
        if not data_base.has_table('genre'):
            request = """
                CREATE TABLE genre (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE
                );
            """
            data_base.execute(request)
            genre.load_default_value(load_yaml, Genre.DEFAULT_MOVIES_FILE)
        return genre

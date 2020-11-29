from typing import Callable

from data_base import DataBase
from table import Table
from tools.yaml_loader import load_yaml


class GenreTable(Table):
    DEFAULT_MOVIES_FILE = '../data/movies.yml'

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

    def load_default_value(self, loader: Callable, movies_file: str):
        genres = set(
            movie.get('genre')
            for movie in loader(movies_file).get('movies')
            if movie.get('genre')
        )
        for genre in genres:
            self.add(genre)

    @classmethod
    def create_table(cls):
        genre = cls()
        if not genre.data_base.has_table('genre'):
            request = """
                CREATE TABLE genre (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE
                );
            """
            genre.data_base.execute(request)
            genre.load_default_value(load_yaml, GenreTable.DEFAULT_MOVIES_FILE)
        return genre

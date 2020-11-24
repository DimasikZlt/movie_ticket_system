from typing import Callable
from table import Table
from tools.yaml_loader import load_yaml


class Genre(Table):
    DEFAULT_MOVIES_FILE = '../data/movies.yml'

    def add(self, name: str):
        request = """
            INSERT INTO genre(name) VALUES(?)
        """, (name,)
        self.execute(request)

    def remove(self, name):
        request = """
            DELETE FROM genre
            WHERE name = ?
        """, (name,)
        self.execute(request)

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
        if not genre.has_table('genre'):
            request = """
                CREATE TABLE genre (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE
                );
            """
            genre.execute(request)
            genre.load_default_value(load_yaml, Genre.DEFAULT_MOVIES_FILE)
        return genre

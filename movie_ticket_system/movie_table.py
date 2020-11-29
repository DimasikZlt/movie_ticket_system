from typing import Callable

from table import Table
from tools.field_pair_tuple import FieldPair
from tools.yaml_loader import load_yaml


class MovieTable(Table):
    DEFAULT_MOVIES_FILE = '../data/movies.yml'
    movie_db_fields = (
        'id',
        'title',
        'year',
        'description',
        'duration',
        'genre_id',
    )

    def add(self, title: str, year: int, description: str, duration: int, genre: str):
        genre_id, _ = super().get_by_field('genre', FieldPair('name', genre))
        request = """
            INSERT INTO movie (title, year, description, duration, genre_id) VALUES(?, ?, ?, ?, ?)
        """, (title, year, description, duration, genre_id)
        self.data_base.execute(request)

    def get_all(self, table_name: str):
        request = f"""
            SELECT movie.id, movie.title, movie.year, movie.description, movie.duration, genre.name
            FROM {table_name}
            INNER JOIN genre on genre.id = movie.genre_id
        """
        return self.data_base.select_all(request)

    def get_by_field(self, table_name, field_pair: FieldPair):
        if field_pair.field_name in self.movie_db_fields:
            request = f"""
                SELECT
                    movie.id,
                    movie.title,
                    movie.year,
                    movie.description,
                    movie.duration, 
                    genre.name
                FROM {table_name}
                INNER JOIN genre on genre.id = movie.genre_id
                WHERE movie.{field_pair.field_name} = ?
            """, (field_pair.field_value,)
            return self.data_base.select_one(request)

    def remove(self, title: str):
        request = """
            DELETE FROM movie
            WHERE title = ?
        """, (title,)
        self.data_base.execute(request)

    def update(self, field_pair: FieldPair, filter_field_pair: FieldPair):
        if (field_pair.field_name != 'id'
                and field_pair.field_name in self.movie_db_fields
                and filter_field_pair.field_name in self.movie_db_fields):
            request = f"""
                UPDATE movie
                SET {field_pair.field_name} = ?
                WHERE {filter_field_pair.field_name} = ? 
            """, (field_pair.field_value, filter_field_pair.field_value)
            self.data_base.execute(request)

    def update_genre(self, title: str, genre: str):
        genre_id, _ = super().get_by_field('genre', FieldPair('name', genre))
        self.update(FieldPair('genre_id', genre_id), FieldPair('title', title))

    def load_default_value(self, loader: Callable, movies_file: str):
        for movie in loader(movies_file).get('movies'):
            title = movie.get('movie_title')
            year = movie.get('year')
            description = movie.get('description')
            duration = movie.get('duration')
            genre = movie.get('genre')
            if title and year and description and genre:
                self.add(title, year, description, duration, genre)

    @classmethod
    def create_table(cls):
        movie = cls()
        if not movie.data_base.has_table('movie'):
            request = """
                CREATE TABLE movie (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL UNIQUE,
                    year INTEGER NOT NULL,
                    description TEXT NOT NULL,
                    duration INTEGER NOT NULL, 
                    genre_id INTEGER NOT NULL REFERENCES genre(id)
                );
            """
            movie.data_base.execute(request)
            movie.load_default_value(load_yaml, MovieTable.DEFAULT_MOVIES_FILE)
        return movie

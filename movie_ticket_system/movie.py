from data_base import DataBase
from genre import Genre
from tools.field_pair_tuple import FieldPair


class Movie:
    def __init__(self, data_base: DataBase, genre: Genre):
        self.data_base = data_base
        self.genre = genre
        self.movie_db_fields = (
            'id',
            'title',
            'year',
            'description',
            'duration',
        )

    def add(self, title: str, year: int, description: str, duration: int, genre: str):
        genre_id, _ = self.genre.get_by_field(FieldPair('name', genre))
        request = """
            INSERT INTO movie (title, year, description, duration, genre_id) VALUES(?, ?, ?, ?, ?)
        """, (title, year, description, duration, genre_id)
        self.data_base.execute(request)

    def get_all(self):
        request = """
            SELECT movie.id, movie.title, movie.year, movie.description, movie.duration, genre.name
            FROM movie
            INNER JOIN genre on genre.id = movie.genre_id
        """
        return self.data_base.select_all(request)

    def get_by_field(self, field_pair: FieldPair):
        if field_pair.field_name in self.movie_db_fields:
            request = f"""
                SELECT
                    movie.id,
                    movie.title,
                    movie.year,
                    movie.description,
                    movie.duration, 
                    genre.name
                FROM movie
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
        genre_id, _ = self.genre.get_by_field(FieldPair('name', genre))
        self.update(FieldPair('genre_id', genre_id), FieldPair('title', title))

    @classmethod
    def create_table(cls, data_base):
        genre = Genre.create_table(data_base)
        request = """
            CREATE TABLE IF NOT EXISTS movie (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL UNIQUE,
                year INTEGER NOT NULL,
                description TEXT NOT NULL,
                duration INTEGER NOT NULL, 
                genre_id INTEGER NOT NULL, 
                FOREIGN KEY (genre_id) REFERENCES genre(id)
            );
        """
        data_base.execute(request)
        return cls(data_base, genre)

from datetime import datetime

from data_base import DataBase
from table import Table
from tools.field_pair_tuple import FieldPair


class SessionTable(Table):
    movie_hall_db_fields = (
        'id',
        'date',
        'time',
        'movie_hall_id',
        'movie_title_id',
    )

    def add(self, date_time: datetime, movie_hall_name: str, movie_title: str):
        movie_title_id, _ = super().get_by_field('movie_title', FieldPair('name', movie_title))
        movie_hall_id, _ = super().get_by_field('movie_hall', FieldPair('name', movie_hall_name))
        date, time = date_time.strftime('%d.%m.%Y'), date_time.strftime('%H:%M')
        request = """
            INSERT INTO session(date, time, movie_hall_id, movie_title_id) VALUES(?, ?, ?, ?)
        """, (date, time, movie_hall_id, movie_title_id)
        self.data_base.execute(request)

    def remove(self, date_time: datetime, movie_hall_name: str, movie_title: str):
        movie_title_id, _ = super().get_by_field('movie_title', FieldPair('name', movie_title))
        movie_hall_id, _ = super().get_by_field('movie_hall', FieldPair('name', movie_hall_name))
        date, time = date_time.strftime('%d.%m.%Y'), date_time.strftime('%H:%M')
        request = """
            DELETE FROM session
            WHERE date = ?
            AND time = ?
            AND movie_title_id = ?
            AND movie_hall_id = ?
        """, (date, time, movie_title_id, movie_hall_id)
        self.data_base.execute(request)

    def get_all(self, table_name: str):
        request = f"""
            SELECT session.id, session.date, session.time, movie_hall.name, movie.title
            FROM {table_name}
            INNER JOIN movie_hall on movie_hall.id = session.movie_hall_id
            INNER JOIN movie on movie.id = session.movie_title_id
        """
        return self.data_base.select_all(request)

    def get_by_field(self, table_name: str, field_pair: FieldPair):
        if field_pair.field_name in self.movie_hall_db_fields:
            request = f"""
                SELECT session.id, session.date, session.time, movie_hall.name, movie.title
                FROM {table_name}
                INNER JOIN movie_hall on movie_hall.id = session.movie_hall_id
                INNER JOIN movie on movie.id = session.movie_title_id
                WHERE session.{field_pair.field_name} = ?
            """, (field_pair.field_value,)
            return self.data_base.select_one(request)

    @classmethod
    def create_table(cls, data_base: DataBase):
        session = cls(data_base)
        if not data_base.has_table('session'):
            request = """
                CREATE TABLE session (
                    id INTEGER PRIMARY KEY,
                    date TEXT NOT NULL,
                    time TEXT NOT NULL,
                    movie_hall_id INTEGER REFERENCES movie_hall(id),
                    movie_title_id INTEGER REFERENCES movie(id)
                );
            """
            data_base.execute(request)
        return session

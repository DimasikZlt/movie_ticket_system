from datetime import datetime, timedelta
import random

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
        movie_title_id, *_ = super().get_by_field('movie', FieldPair('title', movie_title))
        movie_hall_id, *_ = super().get_by_field('movie_hall', FieldPair('name', movie_hall_name))
        self.add_by_id(date_time, movie_hall_id, movie_title_id)

    def add_by_id(self, date_time: datetime, movie_hall_id: str, movie_title_id: str):
        date, time = date_time.strftime('%d.%m.%Y'), date_time.strftime('%H:%M')
        request = """
            INSERT INTO session(date, time, movie_hall_id, movie_title_id) VALUES(?, ?, ?, ?)
        """
        self.data_base.execute(request, (date, time, movie_hall_id, movie_title_id))

    def remove(self, date_time: datetime, movie_hall_name: str, movie_title: str):
        movie_title_id, *_ = super().get_by_field('movie', FieldPair('title', movie_title))
        movie_hall_id, *_ = super().get_by_field('movie_hall', FieldPair('name', movie_hall_name))
        date, time = date_time.strftime('%d.%m.%Y'), date_time.strftime('%H:%M')
        request = """
            DELETE FROM session
            WHERE date = ?
            AND time = ?
            AND movie_title_id = ?
            AND movie_hall_id = ?
        """
        self.data_base.execute(request, (date, time, movie_title_id, movie_hall_id))

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
            """
            return self.data_base.select_one(request, (field_pair.field_value,))

    def get_movies(self, session_date: datetime.date):
        request = f"""
            SELECT movie.id, movie.title, movie.duration
            FROM movie
            INNER JOIN session ON movie.id = session.movie_title_id
            WHERE session.date = ?
        """
        return self.data_base.select_all(request, (session_date,))

    def make_sessions(self):
        today = datetime.now().date()
        movies = self.get_movies(today)
        if not movies:
            for movie_hall_id, *_ in super().get_all('movie_hall'):
                start_time = datetime.now()
                start_time = start_time.replace(hour=9, minute=0, second=0)
                end_time = start_time.replace(hour=22, minute=0, second=0)
                while start_time < end_time:
                    movie_id, title, _, _, duration, *_ = random.choice(super().get_all('movie'))
                    self.add_by_id(
                        datetime.combine(today, start_time.time()), movie_hall_id, movie_id
                    )
                    start_time = start_time + timedelta(minutes=duration) + timedelta(minutes=15)
                    start_time += timedelta(minutes=10 - start_time.minute % 10)

    @classmethod
    def create_table(cls):
        session = cls()
        if not session.data_base.has_table('session'):
            request = """
                CREATE TABLE session (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date DATE NOT NULL,
                    time TIME NOT NULL,
                    movie_hall_id INTEGER NOT NULL REFERENCES movie_hall(id),
                    movie_title_id INTEGER NOT NULL REFERENCES movie(id)
                );
            """
            session.data_base.execute(request)
        session.make_sessions()
        return session

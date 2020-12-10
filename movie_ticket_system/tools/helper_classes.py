from collections import namedtuple
from datetime import datetime
from typing import NamedTuple, Any


class FieldPair(NamedTuple):
    field_name: str
    field_value: Any


class Session(NamedTuple):
    session_id: int
    time: datetime.time
    movie_hall_id: int
    movie_hall: str
    movie_title_id: int
    movie_title: str


class Seat(NamedTuple):
    seat_id: int
    row_id: int
    row_number: int
    seat_number: int
    movie_hall_id: int

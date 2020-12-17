from typing import Tuple, Any

from data_base import DataBase
from tools.helper_classes import FieldPair
from abc import ABCMeta, abstractmethod


class Table(metaclass=ABCMeta):
    """
    Abstract class describes a table of database
    Contains some basic methods
    """
    DB_PATH = '../data/movie_ticket_system.sqlite'
    DATABASE = DataBase.connect(DB_PATH)

    def __init__(self, db: DataBase = None):
        self.data_base = db or Table.DATABASE

    @abstractmethod
    def add(self, *args, **kwargs):
        raise NotImplemented

    @abstractmethod
    def remove(self, *args, **kwargs):
        raise NotImplemented

    def get_all(self, name: str):
        request = f"""
            SELECT *
            FROM {name}
        """
        return self.data_base.select_all(request)

    def get_by_field(self, name: str, field_pair: FieldPair) -> Tuple[Any]:
        request = f"""
            SELECT *
            FROM {name}
            WHERE {field_pair.field_name} = ?
        """
        return self.data_base.select_one(request, (field_pair.field_value,))

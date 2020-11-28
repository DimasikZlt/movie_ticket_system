from data_base import DataBase
from tools.field_pair_tuple import FieldPair
from abc import ABCMeta, abstractmethod


class Table(metaclass=ABCMeta):
    DB_PATH = '../data/movie_ticket_system.sqlite'
    DB_CURSOR = DataBase.connect(DB_PATH)

    @abstractmethod
    def add(self):
        raise NotImplemented

    @abstractmethod
    def remove(self):
        raise NotImplemented

    def get_all(self, name: str):
        request = f"""
            SELECT *
            FROM {name}
        """
        return Table.DB_CURSOR.select_all(request)

    def get_by_field(self, name: str, field_pair: FieldPair):
        request = f"""
            SELECT *
            FROM {name}
            WHERE {field_pair.field_name} = ?
        """, (field_pair.field_value,)
        return Table.DB_CURSOR.select_one(request)

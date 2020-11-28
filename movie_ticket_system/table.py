from data_base import DataBase
from tools.field_pair_tuple import FieldPair
from abc import ABCMeta, abstractmethod


class Table(metaclass=ABCMeta):

    def __init__(self, db: DataBase):
        self.data_base = db

    @abstractmethod
    def add(self, name: str):
        raise NotImplemented

    @abstractmethod
    def remove(self, name: str):
        raise NotImplemented

    def get_all(self, name: str):
        request = f"""
            SELECT *
            FROM {name}
        """
        return self.data_base.select_all(request)

    def get_by_field(self, name: str, field_pair: FieldPair):
        request = f"""
            SELECT *
            FROM {name}
            WHERE {field_pair.field_name} = ?
        """, (field_pair.field_value,)
        return self.data_base.select_one(request)

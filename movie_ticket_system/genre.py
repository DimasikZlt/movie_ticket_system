from data_base import DataBase
from tools.field_pair_tuple import FieldPair


class Genre:
    def __init__(self, data_base: DataBase):
        self.data_base = data_base

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

    def get_all(self):
        request = """
            SELECT id, name
            FROM genre
        """
        return self.data_base.select_all(request)

    def get_by_field(self, field_pair: FieldPair):
        request = f"""
            SELECT id, name
            FROM genre
            WHERE {field_pair.field_name} = ?
        """, (field_pair.field_value,)
        return self.data_base.select_one(request)

    @classmethod
    def create_table(cls, data_base):
        request = """
            CREATE TABLE IF NOT EXISTS genre (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            );
        """
        data_base.execute(request)
        return cls(data_base)
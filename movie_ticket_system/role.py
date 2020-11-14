from data_base import DataBase


class Role:
    def __init__(self, data_base: DataBase):
        self.data_base = data_base

    def add(self, name: str):
        request = """
            INSERT INTO role VALUES(?)
        """, (name,)
        self.data_base.execute(request)

    def get_all(self):
        request = """
            SELECT id, name
            FROM role
        """
        return self.data_base.select_all(request)

    def get_by_id(self, id_: int):
        request = """
            SELECT name
            FROM role
            WHERE id = ?
        """, (id_,)
        return self.data_base.select_one(request)

    def get_by_name(self, name: str):
        request = """
            SELECT id
            FROM role
            WHERE name = ?
        """, (name,)
        return self.data_base.select_one(request)

    def remove(self, name: str):
        request = """
            DELETE FROM role
            WHERE name = ?
        """, (name,)
        self.data_base.execute(request)

    @classmethod
    def create_table(cls, data_base):
        request = """
            CREATE TABLE IF NOT EXISTS role (
	            id INTEGER PRIMARY KEY,
   	            name TEXT NOT NULL UNIQUE
            );
        """
        data_base.execute(request)
        return cls(data_base)

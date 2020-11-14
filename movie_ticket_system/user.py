from typing import Any

from data_base import DataBase


class User:
    def __init__(self, data_base: DataBase):
        self.data_base = data_base
        self.user_db_fields = (
            'id',
            'first_name',
            'last_name',
            'login',
        )

    def add(self):
        pass

    def get_all(self):
        pass

    def get_by_field(self, field_name: str, field_value: Any):
        if field_name in self.user_db_fields:
            request = f"""
                SELECT *
                FROM role
                WHERE {field_name} = ?
            """, (field_value,)
            return self.data_base.select_one(request)

    def get_by_login(self):
        pass

    def remove(self):
        pass

    def update(self, field_name: str, field_value: Any, filter_field_name: str,
               filter_field_value: Any):
        if (field_name != 'id'
                and field_name in self.user_db_fields
                and filter_field_name in self.user_db_fields):
            request = f"""
                UPDATE user
                SET {field_name} = ?
                WHERE {filter_field_name} = ? 
            """, (field_value, filter_field_value)
            self.data_base.execute(request)

    @classmethod
    def create_table(cls, data_base):
        request = """
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                login TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role_id INTEGER NOT NULL, 
                FOREIGN KEY (role_id) REFERENCES role(id)
            );
        """
        data_base.execute(request)
        return cls(data_base)

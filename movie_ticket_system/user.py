from typing import Any

from data_base import DataBase
from role import Role
from tools.field_pair_tuple import FieldPair


class User:
    def __init__(self, data_base: DataBase, role: Role):
        self.data_base = data_base
        self.role = role
        self.user_db_fields = (
            'id',
            'first_name',
            'last_name',
            'login',
        )

    def add(self, first_name: str, last_name: str, login: str, password: str, role: str):
        role_id, _ = self.role.get_by_field(FieldPair('name', role))
        request = """
            INSERT INTO user (first_name, last_name, login, password, role_id) VALUES(?, ?, ?, ?, ?)
        """, (first_name, last_name, login, password, role_id)
        self.data_base.execute(request)

    def get_all(self):
        request = """
                    SELECT id, first_name, last_name, login
                    FROM user
                """
        return self.data_base.select_all(request)

    def get_by_field(self, field_name: str, field_value: Any):
        if field_name in self.user_db_fields:
            request = f"""
                SELECT id, first_name, last_name, login
                FROM user
                WHERE {field_name} = ?
            """, (field_value,)
            return self.data_base.select_one(request)

    def remove(self, login):
        request = """
            DELETE FROM user
            WHERE login = ?
        """, (login,)
        self.data_base.execute(request)

    def update(self, field_pair: FieldPair, filter_field_pair: FieldPair):
        if (field_pair.field_name != 'id'
                and field_pair.field_name in self.user_db_fields
                and filter_field_pair.field_name in self.user_db_fields):
            request = f"""
                UPDATE user
                SET {field_pair.field_name} = ?
                WHERE {filter_field_pair.field_name} = ? 
            """, (field_pair.field_value, filter_field_pair.field_value)
            self.data_base.execute(request)

    @classmethod
    def create_table(cls, data_base):
        role = Role.create_table(data_base)
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
        return cls(data_base, role)

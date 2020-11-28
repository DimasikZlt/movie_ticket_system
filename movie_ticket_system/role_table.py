from typing import Callable

from data_base import DataBase
from table import Table
from tools.yaml_loader import load_yaml


class RoleTable(Table):
    DEFAULT_ROLES_FILE = '../data/users.yml'

    def add(self, name: str):
        request = """
            INSERT INTO role(name) VALUES(?)
        """, (name,)
        self.data_base.execute(request)

    def remove(self, name: str):
        request = """
            DELETE FROM role
            WHERE name = ?
        """, (name,)
        self.data_base.execute(request)

    def load_default_value(self, loader: Callable, users_file: str):
        roles = set(user.get('role') for user in loader(users_file) if user.get('role'))
        for role in roles:
            self.add(role)

    @classmethod
    def create_table(cls, data_base: DataBase):
        role = cls(data_base)
        if not data_base.has_table('role'):
            request = """
                CREATE TABLE role (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE
                );
            """
            data_base.execute(request)
            role.load_default_value(load_yaml, RoleTable.DEFAULT_ROLES_FILE)
        return role

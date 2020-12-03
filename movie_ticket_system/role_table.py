from typing import Callable

from table import Table
from tools.yaml_loader import load_yaml


class RoleTable(Table):
    DEFAULT_ROLES_FILE = '../data/users.yml'

    def add(self, name: str):
        request = """
            INSERT INTO role(name) VALUES(?)
        """
        self.data_base.execute(request, (name,))

    def remove(self, name: str):
        request = """
            DELETE FROM role
            WHERE name = ?
        """
        self.data_base.execute(request, (name,))

    def load_default_value(self, loader: Callable, users_file: str):
        roles = set(user.get('role') for user in loader(users_file) if user.get('role'))
        for role in roles:
            self.add(role)

    @classmethod
    def create_table(cls):
        role = cls()
        if not role.data_base.has_table('role'):
            request = """
                CREATE TABLE role (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                );
            """
            role.data_base.execute(request)
            role.load_default_value(load_yaml, RoleTable.DEFAULT_ROLES_FILE)
        return role

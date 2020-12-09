from typing import Callable

from table import Table
from tools.helper_classes import FieldPair
from tools.yaml_loader import load_yaml


class UserTable(Table):
    DEFAULT_USERS_FILE = '../data/users.yml'
    user_db_fields = (
        'id',
        'first_name',
        'last_name',
        'login',
        'role_id',
    )

    def add(self, first_name: str, last_name: str, login: str, password: str, role: str):
        role_id, _ = super().get_by_field('role', FieldPair('name', role))
        request = """
            INSERT INTO user (first_name, last_name, login, password, role_id) VALUES(?, ?, ?, ?, ?)
        """
        self.data_base.execute(request, (first_name, last_name, login, password, role_id))

    def get_all(self, table_name: str):
        request = f"""
            SELECT user.id, user.first_name, user.last_name, user.login, role.name
            FROM {table_name}
            INNER JOIN role on role.id = user.role_id
        """
        return self.data_base.select_all(request)

    def get_by_field(self, table_name: str, field_pair: FieldPair):
        if field_pair.field_name in self.user_db_fields:
            request = f"""
                SELECT user.id, user.first_name, user.last_name, user.login, role.name
                FROM {table_name}
                INNER JOIN role on role.id = user.role_id
                WHERE user.{field_pair.field_name} = ?
            """
            return self.data_base.select_one(request, (field_pair.field_value,))

    def remove(self, login):
        request = """
            DELETE FROM user
            WHERE login = ?
        """
        self.data_base.execute(request, (login,))

    def update(self, field_pair: FieldPair, filter_field_pair: FieldPair):
        if (field_pair.field_name != 'id'
                and field_pair.field_name in self.user_db_fields
                and filter_field_pair.field_name in self.user_db_fields):
            request = f"""
                UPDATE user
                SET {field_pair.field_name} = ?
                WHERE {filter_field_pair.field_name} = ? 
            """
            self.data_base.execute(request, (field_pair.field_value, filter_field_pair.field_value))

    def update_user(self, login: str, role: str):
        role_id, _ = super().get_by_field('role', FieldPair('name', role))
        self.update(FieldPair('role_id', role_id), FieldPair('login', login))

    def load_default_value(self, loader: Callable, users_file: str):
        for user in loader(users_file):
            first_name = user.get('first_name')
            last_name = user.get('last_name')
            login = user.get('login')
            password = user.get('password')
            role = user.get('role')
            if first_name and last_name and login and password:
                self.add(first_name, last_name, login, password, role)

    @classmethod
    def create_table(cls):
        user = cls()
        if not user.data_base.has_table('user'):
            request = """
                CREATE TABLE user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    login TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    role_id INTEGER NOT NULL REFERENCES role(id)
                );
            """
            user.data_base.execute(request)
            user.load_default_value(load_yaml, UserTable.DEFAULT_USERS_FILE)
        return user

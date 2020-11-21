from __future__ import annotations

from typing import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data_base import DataBase

from role import Role
from tools.field_pair_tuple import FieldPair
from tools.yaml_loader import load_yaml


class User:
    DEFAULT_USERS_FILE = '../data/users.yml'

    def __init__(self, data_base: DataBase, role: Role):
        self.data_base = data_base
        self.role = role
        self.user_db_fields = (
            'id',
            'first_name',
            'last_name',
            'login',
            'role_id',
        )

    def add(self, first_name: str, last_name: str, login: str, password: str, role: str):
        role_id, _ = self.role.get_by_field(FieldPair('name', role))
        request = """
            INSERT INTO user (first_name, last_name, login, password, role_id) VALUES(?, ?, ?, ?, ?)
        """, (first_name, last_name, login, password, role_id)
        self.data_base.execute(request)

    def get_all(self):
        request = """
            SELECT user.id, user.first_name, user.last_name, user.login, role.name
            FROM user
            INNER JOIN role on role.id = user.role_id
        """
        return self.data_base.select_all(request)

    def get_by_field(self, field_pair: FieldPair):
        if field_pair.field_name in self.user_db_fields:
            request = f"""
                SELECT user.id, user.first_name, user.last_name, user.login, role.name
                FROM user
                INNER JOIN role on role.id = user.role_id
                WHERE user.{field_pair.field_name} = ?
            """, (field_pair.field_value,)
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

    def update_user(self, login: str, role: str):
        role_id, _ = self.role.get_by_field(FieldPair('name', role))
        self.update(FieldPair('role_id', role_id), FieldPair('login', login))

    def fill_default_value(self, loader: Callable, users_file: str):
        for user in loader(users_file):
            first_name = user.get('first_name')
            last_name = user.get('last_name')
            login = user.get('login')
            password = user.get('password')
            role = user.get('role')
            if first_name and last_name and login and password:
                self.add(first_name, last_name, login, password, role)

    @classmethod
    def create_table(cls, data_base):
        role = Role.create_table(data_base)
        user = cls(data_base, role)
        if not data_base.has_table('user'):
            request = """
                CREATE TABLE user (
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
            user.fill_default_value(load_yaml, User.DEFAULT_USERS_FILE)
        return user

import sqlite3
from typing import Tuple, Union


class DataBase:
    def __init__(self, name: str, db_connect):
        self.name = name
        self.db_connect = db_connect
        self.cur = db_connect.cursor()

    @classmethod
    def connect(cls, name: str):
        db_connect = sqlite3.connect(name)
        return cls(name, db_connect)

    def execute(self, sql_query: Union[Tuple[str], str]):
        self.cur.execute(sql_query)
        self.db_connect.commit()

    def select_all(self, sql_query: Union[Tuple[str], str]):
        return self.cur.execute(sql_query).fetchall()

    def select_one(self, sql_query: Union[Tuple[str], str]):
        return self.cur.execute(sql_query).fetchone()

    def close(self):
        self.db_connect.close()

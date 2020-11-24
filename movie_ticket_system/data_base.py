import sqlite3
from typing import Any


class DataBase:
    name = None
    db_connect = None
    cur = None

    @classmethod
    def connect(cls, name: str):
        DataBase.name = name
        DataBase.db_connect = sqlite3.connect(name)
        DataBase.cur = DataBase.db_connect.cursor()
        return cls()

    def execute(self, sql_query: Any):
        if isinstance(sql_query, tuple):
            self.cur.execute(*sql_query)
        else:
            self.cur.execute(sql_query)
        self.db_connect.commit()

    def select_all(self, sql_query: Any):
        if isinstance(sql_query, tuple):
            return self.cur.execute(*sql_query).fetchall()
        return self.cur.execute(sql_query).fetchall()

    def select_one(self, sql_query: Any):
        if isinstance(sql_query, tuple):
            return self.cur.execute(*sql_query).fetchone()
        return self.cur.execute(sql_query).fetchone()

    def has_table(self, table_name: str) -> bool:
        request = """
            SELECT COUNT(*) 
            FROM sqlite_master 
            WHERE type = 'table' 
            AND name = ?
        """, (table_name,)
        return self.cur.execute(*request).fetchone()[0]

    def close(self):
        self.db_connect.close()

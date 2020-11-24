from data_base import DataBase
from tools.field_pair_tuple import FieldPair


class Table(DataBase):
    def get_all(self, name: str):
        request = f"""
            SELECT *
            FROM {name}
        """
        return self.select_all(request)

    def get_by_field(self, name: str, field_pair: FieldPair):
        request = f"""
            SELECT *
            FROM {name}
            WHERE {field_pair.field_name} = ?
        """, (field_pair.field_value,)
        return self.select_one(request)

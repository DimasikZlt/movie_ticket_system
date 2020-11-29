from table import Table


class TicketTable(Table):
    def add(self):
        pass

    def remove(self):
        pass

    @classmethod
    def create_table(cls):
        ticket = cls()
        if not ticket.data_base.has_table('ticket'):
            request = """
                CREATE TABLE ticket (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id INTEGER NOT NULL REFERENCES session(id),
                    row_id INTEGER NOT NULL REFERENCES row(id),
                    seat_id INTEGER NOT NULL REFERENCES seat(id)
                );
            """
            ticket.data_base.execute(request)
        return ticket

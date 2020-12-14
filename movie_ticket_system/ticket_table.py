from table import Table
from tools.helper_classes import Seat, Session


class TicketTable(Table):
    def add(self, seat: Seat):
        request = """
            INSERT INTO ticket(session_id, row_id, seat_id) VALUES(?, ?, ?)
        """
        self.data_base.execute(request, (seat.session_id, seat.row_id, seat.seat_id))

    def remove(self, seat: Seat):
        request = """
            DELETE FROM ticket
            WHERE session_id = ?
            AND row_id = ?
            AND seat_id = ?
        """
        self.data_base.execute(request, (seat.session_id, seat.row_id, seat.seat_id))

    def get_booked_seats(self, session: Session):
        request = """
            SELECT session.movie_hall_id, ticket.row_id, row.row_number, ticket.seat_id, 
              seat.seat_number, session.id
            FROM ticket
            INNER JOIN session on ticket.session_id = session.id 
            INNER JOIN row on ticket.row_id = row.id
            INNER JOIN seat on ticket.seat_id = seat.id
            WHERE ticket.session_id = ?
        """
        return self.data_base.select_all(request, (session.session_id,))

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

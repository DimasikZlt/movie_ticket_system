from datetime import datetime
from typing import List

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from application_db import ApplicationDB
from gui_designer.gui import Ui_MainWindow
from seat_push_button import SeatPushButton
from session_push_button import SessionPushButton
from tools.helper_classes import Session, FieldPair, Seat


class AppGui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.session_button = None
        self.selected_seats = []
        self.setupUi(self)
        self.statusbar.showMessage("Application is Ready", 3000)
        self.pushButton_cancel.clicked.connect(self.cancel_buy)
        self.pushButton_buy.clicked.connect(self.buy_seats)
        self.app_db = ApplicationDB()
        self.add_session_buttons()
        session = self.app_db.session.get_sessions_by_date(datetime.now().date())[0]
        self.update_seats_buttons(Session(*session))
        self.actionAbout.triggered.connect(self.show_about_dialog)

    def add_session_buttons(self):
        session_buttons = []
        sessions = self.app_db.session.get_sessions_by_date(datetime.now().date())
        for session in sessions:
            btn = SessionPushButton(Session(*session), self.scrollAreaWidgetContents)
            session_buttons.append(btn)
            btn.clicked.connect(self.clicked_session_buttons)
            self.verticalLayout_5.addWidget(btn)
        self.session_button = session_buttons[0]
        self.session_button.click()

    def clicked_session_buttons(self):
        if self.selected_seats:
            self.statusbar.showMessage("Cancel selecting operation before switching to new movie "
                                       "session")
            return
        pressed_button = self.sender()
        self.session_button.setStyleSheet("QPushButton { background-color: #EFF0F1; }")
        pressed_button.setStyleSheet("QPushButton { background-color: blue; }")
        self.session_button = pressed_button
        self.label.setText(f"{pressed_button.session.time} "
                           f"{pressed_button.session.movie_title} "
                           f"Зал: {pressed_button.session.movie_hall}")
        self.update_seats_buttons(pressed_button.session)

    def update_seats_buttons(self, session: Session):
        self.remove_seats_buttons()
        seats = self.app_db.session.get_all_seats(session)
        seat_iter = iter(seats)
        booked_seats = self.app_db.ticket.get_booked_seats(session)
        _, _, rows, seats = self.app_db.movie_hall.get_by_field(
            'movie_hall', FieldPair('id', session.movie_hall_id)
        )
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0)
        for row in range(1, rows + 1):
            label = QtWidgets.QLabel()
            label.setMaximumSize(QtCore.QSize(10, 50))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            label.setFont(font)
            label.setStyleSheet("QLabel { color : red; }")
            label.setText(str(row))
            self.gridLayout.addWidget(label, row, 0)
            for seat in range(1, seats + 1):
                btn = SeatPushButton(Seat(*next(seat_iter)), self)
                if btn.seat in booked_seats:
                    btn.setStyleSheet("QPushButton { background-color: red; }")
                    btn.setEnabled(False)
                btn.clicked.connect(self.clicked_seats_buttons)
                self.gridLayout.addWidget(btn, row, seat)
            label2 = QtWidgets.QLabel()
            label2.setMaximumSize(QtCore.QSize(10, 50))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            label2.setFont(font)
            label2.setStyleSheet("QLabel { color : red; }")
            label2.setText(str(row))
            self.gridLayout.addWidget(label2, row, seats + 1)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, rows + 1, 0)

    def remove_seats_buttons(self):
        while self.gridLayout.count():
            child = self.gridLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def clicked_seats_buttons(self):
        pressed_button = self.sender()
        if len(self.selected_seats) < 5:
            self.selected_seats.append(pressed_button)
            pressed_button.setStyleSheet("QPushButton { background-color: green; }")
        else:
            self.statusbar.showMessage("Selected too many seats!")
        self.pushButton_buy.setEnabled(True)

    def cancel_buy(self):
        for seat_btn in self.selected_seats:
            seat_btn.setStyleSheet("QPushButton { background-color: #EFF0F1; }")
        self.selected_seats.clear()
        self.statusbar.showMessage("")
        self.pushButton_buy.setEnabled(False)

    def buy_seats(self):
        for seat_btn in self.selected_seats:
            self.app_db.ticket.add(seat_btn.seat)
        self.print_ticket(self.session_button.session, self.selected_seats)
        self.selected_seats.clear()
        self.update_seats_buttons(self.session_button.session)
        self.statusbar.showMessage("")
        self.pushButton_buy.setEnabled(False)

    def show_about_dialog(self):
        text = "<center>" \
               "<h1>Movie Ticket System (MTS)</h1>" \
               "" \
               "</center>" \
               "<p>Version 0.1a<br/>" \
               "Copyleft (\u2184) DimasZlt Inc.</p>"

        QMessageBox.about(self, "About", text)

    def print_ticket(self, session: Session, seats_buttons: List[SeatPushButton]):
        with open('../data/tickets.txt', 'a', encoding='utf-8') as ticket_file:
            for seat_button in seats_buttons:
                ticket = f"{'=' * 50}\n" \
                         f"Movie title: {session.movie_title}\n" \
                         f"Movie hall: {session.movie_hall}\n" \
                         f"Session time: {session.time}\n" \
                         f"Row: {seat_button.seat.row_number}\n" \
                         f"Seat: {seat_button.seat.seat_number}\n" \
                         f"{'=' * 50}\n"
                ticket_file.write(ticket)

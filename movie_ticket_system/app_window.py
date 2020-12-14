from datetime import datetime

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow

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
        self.setupUi(self)
        self.app_db = ApplicationDB()
        self.add_session_buttons()
        session = self.app_db.session.get_sessions_by_date(datetime.now().date())[5]
        self.update_seats_buttons(Session(*session))

    def add_session_buttons(self):
        sessions = self.app_db.session.get_sessions_by_date(datetime.now().date())
        for session in sessions:
            btn = SessionPushButton(Session(*session), self.scrollAreaWidgetContents)
            btn.clicked.connect(self.clicked_session_buttons)
            self.verticalLayout_5.addWidget(btn)

    def clicked_session_buttons(self):
        push_button = self.sender()
        push_button.setStyleSheet("background-color: red")
        self.label.setText(f"{push_button.session.movie_title} - {push_button.session.time}")
        self.update_seats_buttons(push_button.session)

    def update_seats_buttons(self, session: Session):
        self.remove_seats_buttons()
        seats = self.app_db.session.get_all_seats(session)
        seat_iter = iter(seats)
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

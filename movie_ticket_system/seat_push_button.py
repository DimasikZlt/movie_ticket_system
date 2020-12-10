from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QPushButton

from tools.helper_classes import Seat


class SeatPushButton(QPushButton):
    def __init__(self, seat: Seat, parent):
        super().__init__(
            str(Seat.seat_number),
            parent
        )
        self.seat = seat
        self.setMinimumSize(QtCore.QSize(50, 50))
        self.setMaximumSize(QtCore.QSize(50, 50))
        self.setStyleSheet("Text-align:left")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.setFont(font)
        # self.setSizePolicy(
        #     QtWidgets.QSizePolicy.Preferred,
        #     QtWidgets.QSizePolicy.Expanding)

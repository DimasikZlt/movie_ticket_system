from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QPushButton

from tools.helper_classes import Seat


class SeatPushButton(QPushButton):
    def __init__(self, seat: Seat, parent):
        super().__init__(
            str(seat.seat_number),
            parent
        )
        self.seat = seat
        self.setMinimumSize(QtCore.QSize(50, 50))
        self.setMaximumSize(QtCore.QSize(50, 50))
        self.setStyleSheet("Text-align:center")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.setFont(font)
        # self.setSizePolicy(
        #     QtWidgets.QSizePolicy.Preferred,
        #     QtWidgets.QSizePolicy.Expanding)

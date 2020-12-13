from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget

from remove_seats_buttons import remove_seats_buttons
from seat_push_button import SeatPushButton
from tools.helper_classes import Session, Seat, FieldPair


def add_seats_buttons(view: QWidget, session: Session):
    view
    remove_seats_buttons(view)
    seats = view.app_db.session.get_all_seats(session)
    seat_iter = iter(seats)
    _, _, rows, seats = view.app_db.movie_hall.get_by_field(
        'movie_hall', FieldPair('id', session.movie_hall_id)
    )
    spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                        QtWidgets.QSizePolicy.Expanding)
    view.gridLayout.addItem(spacerItem1, 0, 0)
    for row in range(1, rows + 1):
        label = QtWidgets.QLabel()
        label.setMaximumSize(QtCore.QSize(10, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        label.setFont(font)
        label.setStyleSheet("QLabel { color : red; }")
        label.setText(str(row))
        view.gridLayout.addWidget(label, row, 0)
        for seat in range(1, seats + 1):
            btn = SeatPushButton(Seat(*next(seat_iter)), view)
            view.gridLayout.addWidget(btn, row, seat)
        label2 = QtWidgets.QLabel()
        label2.setMaximumSize(QtCore.QSize(10, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        label2.setFont(font)
        label2.setStyleSheet("QLabel { color : red; }")
        label2.setText(str(row))
        view.gridLayout.addWidget(label2, row, seats + 1)

    spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                       QtWidgets.QSizePolicy.Minimum)
    view.gridLayout.addItem(spacerItem, rows + 1, 0)


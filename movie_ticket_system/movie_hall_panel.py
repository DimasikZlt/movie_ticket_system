from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget

from seat_push_button import SeatPushButton
from tools.helper_classes import Session, FieldPair, Seat


def make_movie_hall_table_panel(parent: QWidget, session: Session):
    label = QtWidgets.QLabel('SCREEN', parent.tab_session)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                       QtWidgets.QSizePolicy.Maximum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
    label.setSizePolicy(sizePolicy)
    label.setMaximumSize(QtCore.QSize(16777215, 30))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    font.setWeight(75)
    label.setFont(font)
    label.setFrameShape(QtWidgets.QFrame.WinPanel)
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setObjectName("label")
    verticalLayout = QtWidgets.QVBoxLayout()
    verticalLayout.setObjectName("verticalLayout_3")
    verticalLayout.addWidget(label)
    gridLayout = QtWidgets.QGridLayout()
    gridLayout.setVerticalSpacing(6)
    gridLayout.setObjectName("gridLayout")


    _, _, rows, seats = parent.app_db.movie_hall.get_by_field(
        'movie_hall', FieldPair('id', 1)
    )
    spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                        QtWidgets.QSizePolicy.Expanding)
    gridLayout.addItem(spacerItem1, 0, 0)
    for row in range(1, rows + 1):
        for seat in range(seats):
            btn = SeatPushButton(Seat(1, 2, 3, 4, 5), parent)
            gridLayout.addWidget(btn, row, seat)

    spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                       QtWidgets.QSizePolicy.Minimum)
    gridLayout.addItem(spacerItem, rows + 1, 0)
    # parent.pushButton = QtWidgets.QPushButton(parent.tab_session)
    # parent.pushButton.setObjectName("pushButton")
    # parent.pushButton2 = QtWidgets.QPushButton(parent.tab_session)
    # parent.pushButton2.setObjectName("pushButton2")
    # parent.gridLayout.addWidget(parent.pushButton2, 0, 1)

    verticalLayout.addLayout(gridLayout)
    parent.rightVerticalLayout.addLayout(verticalLayout)
    verticalLayout.setStretch(0, 10)
    verticalLayout.setStretch(1, 90)

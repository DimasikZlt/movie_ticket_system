from datetime import datetime, timedelta

from PyQt5 import QtWidgets, QtCore, QtGui

from session_push_button import SessionPushButton
from tools.helper_classes import Session


def make_movie_hall_table_panel(parent: QtWidgets, session: Session):
    parent.rightVerticalLayout = QtWidgets.QVBoxLayout()
    parent.rightVerticalLayout.setObjectName("rightVerticalLayout")
    parent.label = QtWidgets.QLabel('SCREEN', parent.tab_session)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                       QtWidgets.QSizePolicy.Maximum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(parent.label.sizePolicy().hasHeightForWidth())
    parent.label.setSizePolicy(sizePolicy)
    parent.label.setMaximumSize(QtCore.QSize(16777215, 30))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    font.setWeight(75)
    parent.label.setFont(font)
    parent.label.setFrameShape(QtWidgets.QFrame.WinPanel)
    parent.label.setAlignment(QtCore.Qt.AlignCenter)
    parent.label.setObjectName("label")
    parent.verticalLayout = QtWidgets.QVBoxLayout()
    parent.verticalLayout.setObjectName("verticalLayout_3")
    parent.verticalLayout.addWidget(parent.label)
    parent.gridLayout = QtWidgets.QGridLayout()
    parent.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
    parent.gridLayout.setVerticalSpacing(6)
    parent.gridLayout.setObjectName("gridLayout")

    parent.pushButton = QtWidgets.QPushButton(parent.tab_session)
    parent.pushButton.setObjectName("pushButton")
    parent.gridLayout.addWidget(parent.pushButton, 0, 0)
    parent.pushButton2 = QtWidgets.QPushButton(parent.tab_session)
    parent.pushButton2.setObjectName("pushButton2")
    parent.gridLayout.addWidget(parent.pushButton2, 0, 1)

    # parent.rightVerticalLayout.addLayout(parent.gridLayout)
    parent.verticalLayout.addLayout(parent.gridLayout)
    parent.verticalLayout.setStretch(0, 10)
    parent.verticalLayout.setStretch(1, 90)
    parent.rightVerticalLayout.addLayout(parent.verticalLayout)

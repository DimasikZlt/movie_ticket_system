from datetime import datetime

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget

from session_push_button import SessionPushButton
from tools.helper_classes import Session


def make_time_table_panel(parent: QWidget):

    leftVerticalLayout = QtWidgets.QVBoxLayout()
    leftVerticalLayout.setObjectName("leftVerticalLayout")
    scrollArea = QtWidgets.QScrollArea(parent.tab_session)
    scrollArea.setWidgetResizable(True)
    scrollArea.setObjectName("scrollArea")
    scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    scrollAreaWidgetContents = QtWidgets.QWidget()
    btn_layoutVerticalLayout = QtWidgets.QVBoxLayout(scrollAreaWidgetContents)
    btn_layoutVerticalLayout.setObjectName("btn_layoutVerticalLayout")
    sessions = parent.app_db.session.get_sessions_by_date(datetime.now().date())

    for session in sessions:
        btn = SessionPushButton(Session(*session), scrollAreaWidgetContents)
        btn_layoutVerticalLayout.addWidget(btn)

    scrollArea.setWidget(scrollAreaWidgetContents)
    leftVerticalLayout.addWidget(scrollArea)
    parent.sessionHorizontalLayout.addLayout(leftVerticalLayout)
    # parent.sessionHorizontalLayout.setStretch(0, 30)
    # parent.horizontalLayout_3.addLayout(parent.sessionHorizontalLayout, 30)

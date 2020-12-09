from datetime import datetime, timedelta

from PyQt5 import QtWidgets, QtCore

from session_push_button import SessionPushButton
from tools.helper_classes import Session


def make_time_table_panel(parent: QtWidgets):
    parent.tab_session = QtWidgets.QWidget()
    parent.tab_session.setEnabled(True)
    parent.tab_session.setObjectName("tab_session")
    parent.horizontalLayout_3 = QtWidgets.QHBoxLayout(parent.tab_session)
    parent.horizontalLayout_3.setObjectName("horizontalLayout_3")
    parent.leftVerticalLayout = QtWidgets.QVBoxLayout()
    parent.leftVerticalLayout.setObjectName("leftVerticalLayout")
    parent.scrollArea = QtWidgets.QScrollArea(parent.tab_session)
    parent.scrollArea.setWidgetResizable(True)
    parent.scrollArea.setObjectName("scrollArea")
    parent.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    parent.scrollAreaWidgetContents = QtWidgets.QWidget()
    parent.btn_layoutVerticalLayout = QtWidgets.QVBoxLayout(parent.scrollAreaWidgetContents)
    parent.btn_layoutVerticalLayout.setObjectName("btn_layoutVerticalLayout")
    sessions = parent.app_db.session.get_sessions_by_date(datetime.now().date())

    for session in sessions:
        btn = SessionPushButton(Session(*session), parent.scrollAreaWidgetContents)
        parent.btn_layoutVerticalLayout.addWidget(btn)

    parent.scrollArea.setWidget(parent.scrollAreaWidgetContents)
    parent.leftVerticalLayout.addWidget(parent.scrollArea)
    parent.sessionHorizontalLayout.addLayout(parent.leftVerticalLayout)
    parent.sessionHorizontalLayout.setStretch(0, 30)
    parent.horizontalLayout_3.addLayout(parent.sessionHorizontalLayout)
    parent.tabWidget.addTab(parent.tab_session, "Sessions")

from datetime import datetime, timedelta

from PyQt5 import QtWidgets, QtCore

from session_push_button import SessionPushButton
from tools.helper_classes import Session


def make_time_table_panel(parent: QtWidgets):
    parent.horizontalLayout = QtWidgets.QHBoxLayout()
    parent.horizontalLayout.setObjectName("horizontalLayout")
    parent.tabWidget = QtWidgets.QTabWidget()
    parent.tabWidget.setObjectName("tabWidget")
    parent.tab_session = QtWidgets.QWidget()
    parent.tab_session.setEnabled(True)
    parent.tab_session.setObjectName("tab_session")
    parent.horizontalLayout_3 = QtWidgets.QHBoxLayout(parent.tab_session)
    parent.horizontalLayout_3.setObjectName("horizontalLayout_3")
    parent.sessionHorizontalLayout = QtWidgets.QHBoxLayout()
    parent.sessionHorizontalLayout.setObjectName("sessionHorizontalLayout")
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
    parent.rightVerticalLayout = QtWidgets.QVBoxLayout()
    parent.rightVerticalLayout.setObjectName("rightVerticalLayout")
    parent.sessionHorizontalLayout.addLayout(parent.rightVerticalLayout)
    parent.sessionHorizontalLayout.setStretch(0, 30)
    parent.sessionHorizontalLayout.setStretch(1, 70)
    parent.horizontalLayout_3.addLayout(parent.sessionHorizontalLayout)
    parent.tabWidget.addTab(parent.tab_session, "Sessions")
    parent.tab_admin = QtWidgets.QWidget()
    parent.tab_admin.setEnabled(True)
    parent.tab_admin.setObjectName("tab_admin")
    parent.tabWidget.addTab(parent.tab_admin, "Admin")
    parent.menubar = QtWidgets.QMenuBar(parent)
    parent.menubar.setGeometry(QtCore.QRect(0, 0, 640, 18))
    parent.menubar.setObjectName("menubar")
    parent.setMenuBar(parent.menubar)
    parent.statusbar = QtWidgets.QStatusBar(parent)
    parent.statusbar.setObjectName("statusbar")
    parent.setStatusBar(parent.statusbar)
    parent.horizontalLayout.addWidget(parent.tabWidget)
    parent.setCentralWidget(parent.tabWidget)

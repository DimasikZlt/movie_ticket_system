from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMenu

import movie_hall_panel
from application_db import ApplicationDB
from seat_push_button import SeatPushButton
from time_table_panel import make_time_table_panel
from tools.helper_classes import Seat, FieldPair, Session
from movie_hall_panel import make_movie_hall_table_panel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.app_db = ApplicationDB()
        self.setWindowIcon(QtGui.QIcon('../icons/movie_hall.jpeg'))
        self.setWindowTitle("Movie Ticket System")
        self.setGeometry(450, 150, 1024, 768)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setup_ui()

    def setup_ui(self):
        self.tab_session = QtWidgets.QWidget()
        self.tab_session.setEnabled(True)
        self.tab_session.setObjectName("tab_session")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setObjectName("tabWidget")
        self.sessionHorizontalLayout = QtWidgets.QHBoxLayout()
        self.sessionHorizontalLayout.setObjectName("sessionHorizontalLayout")
        make_time_table_panel(self)
        ###
        make_movie_hall_table_panel(self, Session(0, datetime.now().date(), 0, 'King', 0, "NFS"))
        # _, _, rows, seats = self.app_db.movie_hall.get_by_field(
        #     'movie_hall', FieldPair('id', 1)
        # )
        # for row in range(rows):
        #     for seat in range(seats):
        #         btn = SeatPushButton(Seat(1, 2, 3, 4, 5), self)
        #         self.rightVerticalLayout.addWidget(btn)
        ###
        self.sessionHorizontalLayout.addLayout(self.rightVerticalLayout)
        self.sessionHorizontalLayout.setStretch(30, 70)
        self.tab_admin = QtWidgets.QWidget()
        self.tab_admin.setEnabled(True)
        self.tab_admin.setObjectName("tab_admin")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.setCentralWidget(self.tabWidget)

        # Create menu and status bars
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 18))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # Creating menus using a QMenu object
        fileMenu = QMenu("&File", self)
        self.menubar.addMenu(fileMenu)
        # Creating menus using a title
        editMenu = self.menubar.addMenu("&Edit")
        helpMenu = self.menubar.addMenu("&Help")
        self.statusbar.showMessage("Application is Ready", 3000)

        self.tabWidget.addTab(self.tab_session, "Sessions")
        self.tabWidget.addTab(self.tab_admin, "Admin")

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.app_db.close()

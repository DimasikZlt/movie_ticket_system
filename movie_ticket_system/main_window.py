from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMenu

from application_db import ApplicationDB
from time_table_panel import make_time_table_panel


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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setObjectName("tabWidget")
        self.sessionHorizontalLayout = QtWidgets.QHBoxLayout()
        self.sessionHorizontalLayout.setObjectName("sessionHorizontalLayout")
        make_time_table_panel(self)
        self.rightVerticalLayout = QtWidgets.QVBoxLayout()
        self.rightVerticalLayout.setObjectName("rightVerticalLayout")
        self.sessionHorizontalLayout.addLayout(self.rightVerticalLayout)
        self.sessionHorizontalLayout.setStretch(1, 70)
        self.tab_admin = QtWidgets.QWidget()
        self.tab_admin.setEnabled(True)
        self.tab_admin.setObjectName("tab_admin")
        self.tabWidget.addTab(self.tab_admin, "Admin")
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 18))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.horizontalLayout.addWidget(self.tabWidget)
        self.setCentralWidget(self.tabWidget)

        # Creating menus using a QMenu object
        fileMenu = QMenu("&File", self)
        self.menubar.addMenu(fileMenu)
        # Creating menus using a title
        editMenu = self.menubar.addMenu("&Edit")
        helpMenu = self.menubar.addMenu("&Help")
        self.statusbar.showMessage("Application is Ready", 3000)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.app_db.close()

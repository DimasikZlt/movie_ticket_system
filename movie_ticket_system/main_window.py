from PyQt5 import QtCore, QtGui
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
        make_time_table_panel(self)
        # Creating menus using a QMenu object
        fileMenu = QMenu("&File", self)
        self.menubar.addMenu(fileMenu)
        # Creating menus using a title
        editMenu = self.menubar.addMenu("&Edit")
        helpMenu = self.menubar.addMenu("&Help")
        self.statusbar.showMessage("Application is Ready", 3000)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.app_db.close()

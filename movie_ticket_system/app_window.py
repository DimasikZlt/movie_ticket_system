from datetime import datetime

from PyQt5.QtWidgets import QMainWindow

from add_seats_buttons import add_seats_buttons
from add_session_buttons import add_session_buttons
from application_db import ApplicationDB
from gui_designer.gui import Ui_MainWindow
from tools.helper_classes import Session


class AppGui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.app_db = ApplicationDB()
        add_session_buttons(self)
        session = self.app_db.session.get_sessions_by_date(datetime.now().date())[5]
        add_seats_buttons(self, Session(*session))

    def clicked_session_buttons(self):
        push_button = self.sender()

import sys

from PyQt5.QtWidgets import QApplication

from app_window import AppGui
from main_window import MainWindow


def main():
    APP = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(APP.exec())


def app_main():
    app = QApplication(sys.argv)
    ex = AppGui()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    app_main()

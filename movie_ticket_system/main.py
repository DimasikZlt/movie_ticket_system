import sys

from PyQt5.QtWidgets import QApplication

from app_window import AppGui


def main():
    app = QApplication(sys.argv)
    ex = AppGui()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

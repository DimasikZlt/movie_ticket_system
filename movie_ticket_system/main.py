import sys

from PyQt5.QtWidgets import QApplication

from app_window import AppGui


def main():
    """
    Create application, main GUI window and show it on display
    """
    app = QApplication(sys.argv)
    ex = AppGui()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

import sys

from PyQt5.QtWidgets import QApplication

from main_window import MainWindow


def main():
    APP = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(APP.exec_())


if __name__ == '__main__':
    main()


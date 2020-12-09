from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton

from tools.helper_classes import Session


class SessionPushButton(QPushButton):
    def __init__(self, session: Session, parent):
        super().__init__(
            f"{session.movie_title}\n"
            f"{session.time}\n"
            f"Зал: {session.movie_hall}",
            parent
        )
        self.session = session
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.setFont(font)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Expanding)

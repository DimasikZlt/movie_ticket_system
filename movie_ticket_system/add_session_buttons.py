from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from session_push_button import SessionPushButton
from tools.helper_classes import Session


def add_session_buttons(view: QWidget):
    sessions = view.app_db.session.get_sessions_by_date(datetime.now().date())
    for session in sessions:
        btn = SessionPushButton(Session(*session), view.scrollAreaWidgetContents)
        # btn.clicked.connect(clicked_session_buttons)
        view.verticalLayout_5.addWidget(btn)



from datetime import datetime
from typing import List

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from application_db import ApplicationDB
from gui_designer.gui import Ui_MainWindow
from seat_push_button import SeatPushButton
from session_push_button import SessionPushButton
from tools.helper_classes import Session, FieldPair, Seat


class AppGui(QMainWindow, Ui_MainWindow):
    """
    Main GUI Application class and GUI form created by QT Designer
    """

    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.session_button = None
        self.selected_seats = []
        self.setupUi(self)
        self.statusbar.showMessage("Application is Ready", 3000)
        self.pushButton_cancel.clicked.connect(self.cancel_buy)
        self.pushButton_buy.clicked.connect(self.buy_seats)
        self.app_db = ApplicationDB()
        self.add_session_buttons()
        session = self.app_db.session.get_sessions_by_date(datetime.now().date())[0]
        self.update_seats_buttons(Session(*session))
        self.actionAbout.triggered.connect(self.show_about_dialog)
        self.add_genre_btnbox.accepted.connect(self.save_genre)
        self.add_genre_btnbox.rejected.connect(self.clear_genre_field)
        self.add_film_btnbox.accepted.connect(self.save_movie)
        self.add_film_btnbox.rejected.connect(self.clear_movie_field)
        self.delete_film_btn.clicked.connect(self.delete_movie)
        self.fill_genre_cbox()
        self.fill_movie_cbox()

    def add_session_buttons(self):
        """
        Create list of session buttons, add it to the scroll area and select the first by default
        """
        session_buttons = []
        sessions = self.app_db.session.get_sessions_by_date(datetime.now().date())
        for session in sessions:
            btn = SessionPushButton(Session(*session), self.scrollAreaWidgetContents)
            session_buttons.append(btn)
            btn.clicked.connect(self.clicked_session_buttons)
            self.verticalLayout_5.addWidget(btn)
        self.session_button = session_buttons[0]
        self.session_button.click()

    def clicked_session_buttons(self):
        """
        Action on click a session button.
        Switch between session by selecting different button and check if no one seat was
        selected.
        """
        if self.selected_seats:
            self.statusbar.showMessage("Cancel selecting operation before switching to new movie "
                                       "session")
            return
        pressed_button = self.sender()
        self.session_button.setStyleSheet("QPushButton { background-color: #EFF0F1; }")
        pressed_button.setStyleSheet("QPushButton { background-color: blue; }")
        self.session_button = pressed_button
        self.label.setText(f"{pressed_button.session.time} - "
                           f"{pressed_button.session.movie_title} - "
                           f"Зал: {pressed_button.session.movie_hall}")
        self.update_seats_buttons(pressed_button.session)

    def update_seats_buttons(self, session: Session):
        self.remove_seats_buttons()
        seats = self.app_db.session.get_all_seats(session)
        seat_iter = iter(seats)
        booked_seats = self.app_db.ticket.get_booked_seats(session)
        _, _, rows, seats = self.app_db.movie_hall.get_by_field(
            'movie_hall', FieldPair('id', session.movie_hall_id)
        )
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0)
        for row in range(1, rows + 1):
            label = QtWidgets.QLabel()
            label.setMaximumSize(QtCore.QSize(10, 50))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            label.setFont(font)
            label.setStyleSheet("QLabel { color : red; }")
            label.setText(str(row))
            self.gridLayout.addWidget(label, row, 0)
            for seat in range(1, seats + 1):
                btn = SeatPushButton(Seat(*next(seat_iter)), self)
                btn.setToolTip(f"Row: {btn.seat.row_number}\nSeat: {btn.seat.seat_number}")
                btn.setStyleSheet("QToolTip { background-color: #ffffca; color: #000023; }")
                if btn.seat in booked_seats:
                    btn.setStyleSheet("QPushButton { background-color: red; }")
                    btn.setEnabled(False)
                btn.clicked.connect(self.clicked_seats_buttons)
                self.gridLayout.addWidget(btn, row, seat)
            label2 = QtWidgets.QLabel()
            label2.setMaximumSize(QtCore.QSize(10, 50))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            label2.setFont(font)
            label2.setStyleSheet("QLabel { color : red; }")
            label2.setText(str(row))
            self.gridLayout.addWidget(label2, row, seats + 1)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, rows + 1, 0)

    def remove_seats_buttons(self):
        while self.gridLayout.count():
            child = self.gridLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def clicked_seats_buttons(self):
        pressed_button = self.sender()
        if len(self.selected_seats) < 5:
            self.selected_seats.append(pressed_button)
            pressed_button.setStyleSheet("QPushButton { background-color: green; }")
        else:
            self.statusbar.showMessage("Selected too many seats!")
        self.pushButton_buy.setEnabled(True)

    def cancel_buy(self):
        for seat_btn in self.selected_seats:
            seat_btn.setStyleSheet("QPushButton { background-color: #EFF0F1; }")
        self.selected_seats.clear()
        self.statusbar.showMessage("")
        self.pushButton_buy.setEnabled(False)

    def buy_seats(self):
        for seat_btn in self.selected_seats:
            self.app_db.ticket.add(seat_btn.seat)
        self.save_ticket(self.session_button.session, self.selected_seats)
        self.selected_seats.clear()
        self.update_seats_buttons(self.session_button.session)
        self.statusbar.showMessage("")
        self.pushButton_buy.setEnabled(False)

    def show_about_dialog(self) -> None:
        """
        Show About program window by clicked Help->About menu item
        """
        text = "<center>" \
               "<h1>Movie Ticket System (MTS)</h1>" \
               "" \
               "</center>" \
               "<p>Version 0.2b<br/>" \
               "Copyleft (\u2184) DimasZlt Inc.</p>"

        QMessageBox.about(self, "About", text)

    def save_ticket(self, session: Session, seats_buttons: List[SeatPushButton]) -> None:
        """
        Create tickets from selected seats and save them to a file
        :param session: Movie session contains Movie Hall, Time and Movie Title
        :param seats_buttons: SeatButton contains row and seat number
        """
        with open('../data/tickets.txt', 'a', encoding='utf-8') as ticket_file:
            for seat_button in seats_buttons:
                ticket = f"{'=' * 50}\n" \
                         f"Movie title: {session.movie_title}\n" \
                         f"Movie hall: {session.movie_hall}\n" \
                         f"Session time: {session.time}\n" \
                         f"Row: {seat_button.seat.row_number}\n" \
                         f"Seat: {seat_button.seat.seat_number}\n" \
                         f"{'=' * 50}\n"
                ticket_file.write(ticket)

    def save_genre(self):
        new_genre = self.name_genre_le.text()
        genres = tuple(genre[1] for genre in self.app_db.genre.get_all('genre'))
        if new_genre.isalpha() and new_genre not in genres:
            self.app_db.genre.add(new_genre)
            self.statusbar.showMessage("New genre has been added successfully")
            self.fill_genre_cbox()
        else:
            QMessageBox.information(self, 'Warning', 'Duplicate genre, change it!', QMessageBox.Ok)
        self.name_genre_le.clear()

    def clear_genre_field(self):
        self.name_genre_le.clear()

    def fill_genre_cbox(self):
        self.genre_film_cbox.clear()
        genres = tuple(genre[1] for genre in self.app_db.genre.get_all('genre'))
        self.genre_film_cbox.addItems(genres)

    def save_movie(self):
        new_title = self.title_film_le.text()
        movie_titles = tuple(movie[1] for movie in self.app_db.movie.get_all('movie'))
        if new_title and new_title not in movie_titles:
            self.app_db.movie.add(
                new_title,
                int(self.year_film_sbox.text()),
                self.description_film_txtedit.toPlainText(),
                int(self.duration_film_sbox.text()),
                self.genre_film_cbox.currentText()
            )
            self.statusbar.showMessage("New movie has been added successfully")
        else:
            QMessageBox.information(self, 'Warning', 'Duplicate movie title, change it!',
                                    QMessageBox.Ok)
        self.title_film_le.clear()
        self.description_film_txtedit.clear()
        self.fill_movie_cbox()

    def clear_movie_field(self):
        self.title_film_le.clear()
        self.description_film_txtedit.clear()

    def fill_movie_cbox(self):
        self.delete_movie_cbox.clear()
        movie_titles = tuple(movie[1] for movie in self.app_db.movie.get_all('movie'))
        self.delete_movie_cbox.addItems(movie_titles)

    def delete_movie(self):
        title = self.delete_movie_cbox.currentText()
        movie_id, *_ = self.app_db.movie.get_by_field('movie', FieldPair('title', title))
        movie_title_ids = [
            session[0] for session in self.app_db.session.get_all('session')
        ]
        if movie_id not in movie_title_ids:
            self.app_db.movie.remove(title)
            self.fill_movie_cbox()
        else:
            QMessageBox.information(
                self, 'Warning', 'Cannot remove movie because it currently used in session!',
                QMessageBox.Ok
            )

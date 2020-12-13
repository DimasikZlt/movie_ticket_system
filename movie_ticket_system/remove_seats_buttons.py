from PyQt5.QtWidgets import QWidget


def remove_seats_buttons(view: QWidget):
    while view.gridLayout.count():
        child = view.gridLayout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()

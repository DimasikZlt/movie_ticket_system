# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    """
    GUI items created by QT Designer
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setWindowTitle("Movie Ticket System")
        MainWindow.setWindowIcon(QtGui.QIcon('../icons/movie_hall.jpeg'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_sessions = QtWidgets.QWidget()
        self.tab_sessions.setObjectName("tab_sessions")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_sessions)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_panel_vl = QtWidgets.QVBoxLayout()
        self.left_panel_vl.setObjectName("left_panel_vl")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_sessions)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.left_panel_vl.addWidget(self.scrollArea)
        self.horizontalLayout.addLayout(self.left_panel_vl)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.tab_sessions)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_buy = QtWidgets.QPushButton(self.tab_sessions)
        self.pushButton_buy.setObjectName("pushButton_buy")
        self.pushButton_buy.setEnabled(False)
        self.horizontalLayout_3.addWidget(self.pushButton_buy)
        self.pushButton_cancel = QtWidgets.QPushButton(self.tab_sessions)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.setStretch(0, 10)
        self.verticalLayout_4.setStretch(1, 80)
        self.verticalLayout_4.setStretch(2, 10)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout.setStretch(0, 30)
        self.horizontalLayout.setStretch(1, 70)
        self.tabWidget.addTab(self.tab_sessions, "")
        self.tab_admin = QtWidgets.QWidget()
        self.tab_admin.setObjectName("tab_admin")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_admin)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_admin)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.add_genre = QtWidgets.QWidget()
        self.add_genre.setMaximumSize(QtCore.QSize(400, 400))
        self.add_genre.setObjectName("add_gaenre")
        self.formLayout = QtWidgets.QFormLayout(self.add_genre)
        self.formLayout.setObjectName("formLayout")
        self.name_genre_lbl = QtWidgets.QLabel(self.add_genre)
        self.name_genre_lbl.setObjectName("name_genre_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_genre_lbl)
        self.name_genre_le = QtWidgets.QLineEdit(self.add_genre)
        self.name_genre_le.setObjectName("name_genre_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_genre_le)
        self.add_genre_btnbox = QtWidgets.QDialogButtonBox(self.add_genre)
        self.add_genre_btnbox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.add_genre_btnbox.setObjectName("add_genre_btnbox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.add_genre_btnbox)
        self.tabWidget_2.addTab(self.add_genre, "")
        self.film_add = QtWidgets.QWidget()
        self.film_add.setMaximumSize(QtCore.QSize(400, 400))
        self.film_add.setObjectName("film_add")
        self.formLayout_2 = QtWidgets.QFormLayout(self.film_add)
        self.formLayout_2.setObjectName("formLayout_2")
        self.title_film_lbl = QtWidgets.QLabel(self.film_add)
        self.title_film_lbl.setObjectName("title_film_lbl")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.title_film_lbl)
        self.title_film_le = QtWidgets.QLineEdit(self.film_add)
        self.title_film_le.setObjectName("title_film_le")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.title_film_le)
        self.year_film_lbl = QtWidgets.QLabel(self.film_add)
        self.year_film_lbl.setObjectName("year_film_lbl")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.year_film_lbl)
        self.year_film_sbox = QtWidgets.QSpinBox(self.film_add)
        self.year_film_sbox.setWrapping(False)
        self.year_film_sbox.setMinimum(1895)
        self.year_film_sbox.setMaximum(datetime.now().year)
        self.year_film_sbox.setValue(datetime.now().year)
        self.year_film_sbox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.year_film_sbox.setDisplayIntegerBase(10)
        self.year_film_sbox.setObjectName("year_film_sbox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.year_film_sbox)
        self.duration_film_lbl = QtWidgets.QLabel(self.film_add)
        self.duration_film_lbl.setObjectName("duration_film_lbl")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.duration_film_lbl)
        self.genre_film_lbl = QtWidgets.QLabel(self.film_add)
        self.genre_film_lbl.setObjectName("genre_film_lbl")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.genre_film_lbl)
        self.description_film_lbl = QtWidgets.QLabel(self.film_add)
        self.description_film_lbl.setObjectName("description_film_lbl")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.description_film_lbl)
        self.description_film_txtedit = QtWidgets.QTextEdit(self.film_add)
        self.description_film_txtedit.setObjectName("description_film_txtedit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole,
                                    self.description_film_txtedit)
        self.duration_film_sbox = QtWidgets.QSpinBox(self.film_add)
        self.duration_film_sbox.setMinimum(30)
        self.duration_film_sbox.setMaximum(200)
        self.duration_film_sbox.setValue(90)
        self.duration_film_sbox.setObjectName("duration_film_sbox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.duration_film_sbox)
        self.genre_film_cbox = QtWidgets.QComboBox(self.film_add)
        self.genre_film_cbox.setObjectName("genre_film_cbox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.genre_film_cbox)
        self.add_film_btnbox = QtWidgets.QDialogButtonBox(self.film_add)
        self.add_film_btnbox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.add_film_btnbox.setObjectName("add_film_btnbox")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.add_film_btnbox)
        self.tabWidget_2.addTab(self.film_add, "")
        self.delete_film = QtWidgets.QWidget()
        self.delete_film.setMaximumSize(QtCore.QSize(400, 400))
        self.delete_film.setObjectName("delete_film")
        self.formLayout_3 = QtWidgets.QFormLayout(self.delete_film)
        self.formLayout_3.setObjectName("formLayout_3")
        self.delete_film_lbl = QtWidgets.QLabel(self.delete_film)
        self.delete_film_lbl.setObjectName("delete_film_lbl")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.delete_film_lbl)
        self.delete_movie_cbox = QtWidgets.QComboBox(self.film_add)
        self.delete_movie_cbox.setObjectName("delete_movie_cbox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.delete_movie_cbox)
        self.delete_film_btn = QtWidgets.QPushButton(self.delete_film)
        self.delete_film_btn.setObjectName("delete_fiim_btn")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.delete_film_btn)
        self.tabWidget_2.addTab(self.delete_film, "")
        self.verticalLayout_2.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.tab_admin, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.session_btn.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "SCREEN"))
        # self.seat_btn.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_buy.setText(_translate("MainWindow", "Buy"))
        self.pushButton_cancel.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sessions),
                                  _translate("MainWindow", "Sessions"))
        self.name_genre_lbl.setText(_translate("MainWindow", "Name"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.add_genre),
                                    _translate("MainWindow", "Add genre"))
        self.title_film_lbl.setText(_translate("MainWindow", "Film title"))
        self.year_film_lbl.setText(_translate("MainWindow", "Year"))
        self.duration_film_lbl.setText(_translate("MainWindow", "Duration"))
        self.genre_film_lbl.setText(_translate("MainWindow", "Genre"))
        self.description_film_lbl.setText(_translate("MainWindow", "Description"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.film_add),
                                    _translate("MainWindow", "Add film"))
        self.delete_film_lbl.setText(_translate("MainWindow", "Film title"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.delete_film),
                                    _translate("MainWindow", "Delete film"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_admin),
                                  _translate("MainWindow", "Admin"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.delete_film_btn.setText(_translate("MainWindow", "Delete"))

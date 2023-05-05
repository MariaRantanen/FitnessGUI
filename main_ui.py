# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\pc\Documents\GitHub\FitnessGUI\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(552, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setGeometry(QtCore.QRect(20, 50, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(20, 10, 101, 41))
        self.nameLabel.setObjectName("nameLabel")
        self.weighingDateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.weighingDateEdit.setGeometry(QtCore.QRect(20, 110, 110, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.weighingDateEdit.setFont(font)
        self.weighingDateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Finnish, QtCore.QLocale.Finland))
        self.weighingDateEdit.setCalendarPopup(True)
        self.weighingDateEdit.setObjectName("weighingDateEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 191, 31))
        self.label.setObjectName("label")
        self.heightSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.heightSpinBox.setGeometry(QtCore.QRect(20, 190, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.heightSpinBox.setFont(font)
        self.heightSpinBox.setMinimum(100.0)
        self.heightSpinBox.setMaximum(400.0)
        self.heightSpinBox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.weightSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.weightSpinBox.setGeometry(QtCore.QRect(120, 190, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.weightSpinBox.setFont(font)
        self.weightSpinBox.setMinimum(20.0)
        self.weightSpinBox.setMaximum(3000.0)
        self.weightSpinBox.setObjectName("weightSpinBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 150, 61, 41))
        self.label_3.setObjectName("label_3")
        self.neckSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.neckSpinBox.setGeometry(QtCore.QRect(210, 190, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.neckSpinBox.setFont(font)
        self.neckSpinBox.setMinimum(10)
        self.neckSpinBox.setObjectName("neckSpinBox")
        self.waistSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.waistSpinBox.setGeometry(QtCore.QRect(20, 260, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.waistSpinBox.setFont(font)
        self.waistSpinBox.setMinimum(30)
        self.waistSpinBox.setMaximum(200)
        self.waistSpinBox.setObjectName("waistSpinBox")
        self.hipsSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.hipsSpinBox.setGeometry(QtCore.QRect(120, 260, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hipsSpinBox.setFont(font)
        self.hipsSpinBox.setMinimum(50)
        self.hipsSpinBox.setMaximum(200)
        self.hipsSpinBox.setObjectName("hipsSpinBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 150, 71, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 131, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 220, 111, 41))
        self.label_6.setObjectName("label_6")
        self.calculatePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculatePushButton.setGeometry(QtCore.QRect(210, 260, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calculatePushButton.setFont(font)
        self.calculatePushButton.setObjectName("calculatePushButton")
        self.savePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.savePushButton.setGeometry(QtCore.QRect(330, 260, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.savePushButton.setFont(font)
        self.savePushButton.setObjectName("savePushButton")
        self.birthDateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.birthDateEdit.setGeometry(QtCore.QRect(230, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.birthDateEdit.setFont(font)
        self.birthDateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Finnish, QtCore.QLocale.Finland))
        self.birthDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1900, 1, 1), QtCore.QTime(0, 0, 0)))
        self.birthDateEdit.setCalendarPopup(True)
        self.birthDateEdit.setObjectName("birthDateEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 10, 91, 41))
        self.label_7.setObjectName("label_7")
        self.genderComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.genderComboBox.setGeometry(QtCore.QRect(350, 50, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.genderComboBox.setFont(font)
        self.genderComboBox.setLocale(QtCore.QLocale(QtCore.QLocale.Finnish, QtCore.QLocale.Finland))
        self.genderComboBox.setObjectName("genderComboBox")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.bmiLabel = QtWidgets.QLabel(self.centralwidget)
        self.bmiLabel.setGeometry(QtCore.QRect(30, 350, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bmiLabel.setFont(font)
        self.bmiLabel.setObjectName("bmiLabel")
        self.fatFiLabel = QtWidgets.QLabel(self.centralwidget)
        self.fatFiLabel.setGeometry(QtCore.QRect(180, 350, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fatFiLabel.setFont(font)
        self.fatFiLabel.setObjectName("fatFiLabel")
        self.fatUsLabel = QtWidgets.QLabel(self.centralwidget)
        self.fatUsLabel.setGeometry(QtCore.QRect(360, 350, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fatUsLabel.setFont(font)
        self.fatUsLabel.setObjectName("fatUsLabel")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 320, 101, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(180, 310, 121, 41))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(360, 300, 151, 61))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(350, 10, 101, 41))
        self.label_14.setObjectName("label_14")
        self.testUiPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.testUiPushButton.setGeometry(QtCore.QRect(380, 140, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.testUiPushButton.setFont(font)
        self.testUiPushButton.setObjectName("testUiPushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 552, 22))
        self.menubar.setObjectName("menubar")
        self.menuTiedosto = QtWidgets.QMenu(self.menubar)
        self.menuTiedosto.setObjectName("menuTiedosto")
        self.menuJaa = QtWidgets.QMenu(self.menuTiedosto)
        self.menuJaa.setObjectName("menuJaa")
        self.menuAsetukset = QtWidgets.QMenu(self.menuTiedosto)
        self.menuAsetukset.setObjectName("menuAsetukset")
        self.menuMuokka = QtWidgets.QMenu(self.menubar)
        self.menuMuokka.setObjectName("menuMuokka")
        self.menuOhjeet = QtWidgets.QMenu(self.menubar)
        self.menuOhjeet.setObjectName("menuOhjeet")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTulosta = QtWidgets.QAction(MainWindow)
        self.actionTulosta.setObjectName("actionTulosta")
        self.actionsulje = QtWidgets.QAction(MainWindow)
        self.actionsulje.setObjectName("actionsulje")
        self.actionFacebook = QtWidgets.QAction(MainWindow)
        self.actionFacebook.setObjectName("actionFacebook")
        self.actionTwitter = QtWidgets.QAction(MainWindow)
        self.actionTwitter.setObjectName("actionTwitter")
        self.actionInstagram = QtWidgets.QAction(MainWindow)
        self.actionInstagram.setObjectName("actionInstagram")
        self.actionKieli = QtWidgets.QAction(MainWindow)
        self.actionKieli.setObjectName("actionKieli")
        self.actionUlkoasu = QtWidgets.QAction(MainWindow)
        self.actionUlkoasu.setObjectName("actionUlkoasu")
        self.actionAutomaattinen_tallennus = QtWidgets.QAction(MainWindow)
        self.actionAutomaattinen_tallennus.setCheckable(True)
        self.actionAutomaattinen_tallennus.setObjectName("actionAutomaattinen_tallennus")
        self.actionY_tila = QtWidgets.QAction(MainWindow)
        self.actionY_tila.setCheckable(True)
        self.actionY_tila.setObjectName("actionY_tila")
        self.actionPoista_k_ytt_j = QtWidgets.QAction(MainWindow)
        self.actionPoista_k_ytt_j.setObjectName("actionPoista_k_ytt_j")
        self.actionPalauta_oletukset = QtWidgets.QAction(MainWindow)
        self.actionPalauta_oletukset.setObjectName("actionPalauta_oletukset")
        self.actionOhje = QtWidgets.QAction(MainWindow)
        self.actionOhje.setObjectName("actionOhje")
        self.menuJaa.addAction(self.actionFacebook)
        self.menuJaa.addAction(self.actionTwitter)
        self.menuJaa.addAction(self.actionInstagram)
        self.menuJaa.addSeparator()
        self.menuAsetukset.addAction(self.actionKieli)
        self.menuAsetukset.addAction(self.actionUlkoasu)
        self.menuTiedosto.addAction(self.actionTulosta)
        self.menuTiedosto.addAction(self.menuJaa.menuAction())
        self.menuTiedosto.addAction(self.menuAsetukset.menuAction())
        self.menuTiedosto.addSeparator()
        self.menuTiedosto.addAction(self.actionsulje)
        self.menuMuokka.addAction(self.actionPalauta_oletukset)
        self.menuOhjeet.addAction(self.actionOhje)
        self.menubar.addAction(self.menuTiedosto.menuAction())
        self.menubar.addAction(self.menuMuokka.menuAction())
        self.menubar.addAction(self.menuOhjeet.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameLineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Syötä tähän oma nimesi</p></body></html>"))
        self.nameLabel.setText(_translate("MainWindow", "Nimi"))
        self.weighingDateEdit.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.label.setText(_translate("MainWindow", "Mittauspäivä"))
        self.label_2.setText(_translate("MainWindow", "Pituus"))
        self.label_3.setText(_translate("MainWindow", "Paino"))
        self.label_4.setText(_translate("MainWindow", "Kaula"))
        self.label_5.setText(_translate("MainWindow", "Vyötärö"))
        self.label_6.setText(_translate("MainWindow", "Lantio"))
        self.calculatePushButton.setText(_translate("MainWindow", "Laske"))
        self.savePushButton.setText(_translate("MainWindow", "Tallenna"))
        self.birthDateEdit.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.label_7.setText(_translate("MainWindow", "Syntymäaika"))
        self.genderComboBox.setPlaceholderText(_translate("MainWindow", "Valitse sukupuoli"))
        self.genderComboBox.setItemText(0, _translate("MainWindow", "Mies"))
        self.genderComboBox.setItemText(1, _translate("MainWindow", "Nainen"))
        self.bmiLabel.setText(_translate("MainWindow", "0"))
        self.fatFiLabel.setText(_translate("MainWindow", "0"))
        self.fatUsLabel.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "Painoindeksi"))
        self.label_12.setText(_translate("MainWindow", "Rasvaprosentti (FI)"))
        self.label_13.setText(_translate("MainWindow", "Rasvaprosentti (US)"))
        self.label_14.setText(_translate("MainWindow", "Sukupuoli"))
        self.testUiPushButton.setText(_translate("MainWindow", "Testaa"))
        self.menuTiedosto.setTitle(_translate("MainWindow", "Tiedosto"))
        self.menuJaa.setTitle(_translate("MainWindow", "Jaa"))
        self.menuAsetukset.setTitle(_translate("MainWindow", "Asetukset"))
        self.menuMuokka.setTitle(_translate("MainWindow", "Muokkaa"))
        self.menuOhjeet.setTitle(_translate("MainWindow", "Ohjeet"))
        self.actionTulosta.setText(_translate("MainWindow", "Tulosta..."))
        self.actionsulje.setText(_translate("MainWindow", "Sulje"))
        self.actionFacebook.setText(_translate("MainWindow", "Facebook"))
        self.actionTwitter.setText(_translate("MainWindow", "Twitter"))
        self.actionInstagram.setText(_translate("MainWindow", "Instagram"))
        self.actionKieli.setText(_translate("MainWindow", "Kieli"))
        self.actionUlkoasu.setText(_translate("MainWindow", "Ulkoasu"))
        self.actionAutomaattinen_tallennus.setText(_translate("MainWindow", "Automaattinen tallennus"))
        self.actionAutomaattinen_tallennus.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionY_tila.setText(_translate("MainWindow", "Yötila"))
        self.actionY_tila.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionPoista_k_ytt_j.setText(_translate("MainWindow", "Poista käyttäjä"))
        self.actionPalauta_oletukset.setText(_translate("MainWindow", "Palauta oletukset"))
        self.actionPalauta_oletukset.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionOhje.setText(_translate("MainWindow", "Ohje"))
        self.actionOhje.setShortcut(_translate("MainWindow", "Ctrl+H"))

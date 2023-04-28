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
        MainWindow.resize(651, 685)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setGeometry(QtCore.QRect(20, 50, 211, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(20, 10, 49, 41))
        self.nameLabel.setObjectName("nameLabel")
        self.weighingDateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.weighingDateEdit.setGeometry(QtCore.QRect(20, 110, 110, 41))
        self.weighingDateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Finnish, QtCore.QLocale.Finland))
        self.weighingDateEdit.setCalendarPopup(True)
        self.weighingDateEdit.setObjectName("weighingDateEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 191, 31))
        self.label.setObjectName("label")
        self.heightSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.heightSpinBox.setGeometry(QtCore.QRect(20, 190, 71, 31))
        self.heightSpinBox.setMinimum(100.0)
        self.heightSpinBox.setMaximum(400.0)
        self.heightSpinBox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 91, 71))
        self.label_2.setObjectName("label_2")
        self.weightSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.weightSpinBox.setGeometry(QtCore.QRect(120, 190, 81, 31))
        self.weightSpinBox.setMinimum(20.0)
        self.weightSpinBox.setMaximum(3000.0)
        self.weightSpinBox.setObjectName("weightSpinBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 140, 141, 71))
        self.label_3.setObjectName("label_3")
        self.neckSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.neckSpinBox.setGeometry(QtCore.QRect(230, 190, 61, 31))
        self.neckSpinBox.setMinimum(10)
        self.neckSpinBox.setObjectName("neckSpinBox")
        self.waistSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.waistSpinBox.setGeometry(QtCore.QRect(20, 260, 51, 31))
        self.waistSpinBox.setMinimum(30)
        self.waistSpinBox.setMaximum(200)
        self.waistSpinBox.setObjectName("waistSpinBox")
        self.hipsSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.hipsSpinBox.setGeometry(QtCore.QRect(120, 260, 71, 31))
        self.hipsSpinBox.setMinimum(50)
        self.hipsSpinBox.setMaximum(200)
        self.hipsSpinBox.setObjectName("hipsSpinBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 140, 141, 61))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 131, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 220, 111, 51))
        self.label_6.setObjectName("label_6")
        self.calculatePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculatePushButton.setGeometry(QtCore.QRect(230, 260, 111, 31))
        self.calculatePushButton.setObjectName("calculatePushButton")
        self.savePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.savePushButton.setGeometry(QtCore.QRect(370, 260, 111, 31))
        self.savePushButton.setObjectName("savePushButton")
        self.birthDateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.birthDateEdit.setGeometry(QtCore.QRect(250, 50, 110, 22))
        self.birthDateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Finnish, QtCore.QLocale.Finland))
        self.birthDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1900, 1, 1), QtCore.QTime(0, 0, 0)))
        self.birthDateEdit.setCalendarPopup(True)
        self.birthDateEdit.setObjectName("birthDateEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 10, 161, 41))
        self.label_7.setObjectName("label_7")
        self.genderComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.genderComboBox.setGeometry(QtCore.QRect(380, 50, 111, 22))
        self.genderComboBox.setLocale(QtCore.QLocale(QtCore.QLocale.Finnish, QtCore.QLocale.Finland))
        self.genderComboBox.setObjectName("genderComboBox")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.bmiLabel = QtWidgets.QLabel(self.centralwidget)
        self.bmiLabel.setGeometry(QtCore.QRect(20, 350, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bmiLabel.setFont(font)
        self.bmiLabel.setObjectName("bmiLabel")
        self.fatFiLabel = QtWidgets.QLabel(self.centralwidget)
        self.fatFiLabel.setGeometry(QtCore.QRect(20, 450, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fatFiLabel.setFont(font)
        self.fatFiLabel.setObjectName("fatFiLabel")
        self.fatUsLabel = QtWidgets.QLabel(self.centralwidget)
        self.fatUsLabel.setGeometry(QtCore.QRect(220, 450, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fatUsLabel.setFont(font)
        self.fatUsLabel.setObjectName("fatUsLabel")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 290, 211, 81))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 410, 231, 41))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(210, 400, 281, 61))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(380, 20, 201, 31))
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

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

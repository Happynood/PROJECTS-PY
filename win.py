# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Crypt(object):
    def setupUi(self, Crypt):
        Crypt.setObjectName("Crypt")
        Crypt.resize(327, 107)
        self.lineEdit = QtWidgets.QLineEdit(Crypt)
        self.lineEdit.setGeometry(QtCore.QRect(60, 20, 221, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Crypt)
        self.pushButton.setGeometry(QtCore.QRect(80, 50, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Crypt)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 50, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Crypt)
        QtCore.QMetaObject.connectSlotsByName(Crypt)

    def retranslateUi(self, Crypt):
        _translate = QtCore.QCoreApplication.translate
        Crypt.setWindowTitle(_translate("Crypt", "Crypt"))
        self.pushButton.setText(_translate("Crypt", "Зашифровать"))
        self.pushButton_2.setText(_translate("Crypt", "Расшифровать"))
        

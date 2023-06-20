from PyQt5 import QtCore, QtGui, QtWidgets
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QDialog, QPushButton
from functools import partial
import sqlite3
# import datetime as DT
# print(DT.datetime.now())
# print(str(DT.datetime.now())[:10])
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import datetime as DT
import openpyxl
import os
import docxtpl
# from docxtpl import Table


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(727, 451)
        Dialog.setStyleSheet("background-image: url(OJ91CN0.jpg);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(600, 50, 41, 41))
        self.pushButton.setStyleSheet("font: 12pt \"OCR A Extended\";\n"
"border: 2px solid #ddd;\n"
"border-radius: 20px;\n"
"color:rgb(170, 255, 11);\n"
"background: #fff;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 110, 41, 41))
        self.pushButton_2.setStyleSheet("font: 12pt \"OCR A Extended\";\n"
"border: 2px solid #ddd;\n"
"border-radius: 20px;\n"
"color:rgb(255, 0, 0);\n"
"background: #fff;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 390, 93, 28))
        self.pushButton_3.setStyleSheet("background:rgb(0, 170, 255);\n"
"border-radius: 20px;\n"
"border: 2px solid #ddd;\n"
"color: #fff;\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 390, 93, 28))
        self.pushButton_4.setStyleSheet("background:rgb(0, 170, 255);\n"
"border-radius: 20px;\n"
"border: 2px solid #ddd;\n"
"color: #fff;\n"
"\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(580, 10, 141, 28))
        self.pushButton_5.setStyleSheet("background:rgb(0, 170, 255);\n"
"border-radius: 20px;\n"
"border: 2px solid #ddd;\n"
"color: #fff;\n"
"\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 100, 25))
        self.comboBox.setStyleSheet("background:#8cbaff;")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 11, 191, 21))
        self.label.setStyleSheet("color: #42abc3;\n"
                                 "font: 75 11pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "+"))
        self.pushButton_2.setText(_translate("Dialog", "-"))
        self.pushButton_3.setText(_translate("Dialog", "Применить"))
        self.pushButton_4.setText(_translate("Dialog", "Отменить"))
        self.pushButton_5.setText(_translate("Dialog", "Загрузить документ"))
        self.label.setText(_translate("Dialog", "Выбрать склад"))
        self.pushButton_4.clicked.connect(Dialog.close)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
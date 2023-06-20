from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QDialog, QPushButton
from functools import partial
import sqlite3
from geopy.geocoders import Nominatim
# import datetime as DT
# print(DT.datetime.now())
# print(str(DT.datetime.now())[:10])
import os
import docxtpl

global geolocator
geolocator = Nominatim(user_agent="AIzaSyDDMUpXVY_MU1Z0m0ZTBLzZdI9BkYboBpA")


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(577, 387) # спайсеры
        Dialog.setStyleSheet("background-image: url(\"OJ91CN0.jpg\");")
        db = sqlite3.connect("warehouse.db")
        self.accept_pushButton = QtWidgets.QPushButton(Dialog)
        self.accept_pushButton.setGeometry(QtCore.QRect(10, 340, 101, 41))
        self.accept_pushButton.setStyleSheet("color: #fff;\n" "\n" "background:rgb(120, 192, 255)")
        self.accept_pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 45, 113, 22)) # 1 координаты, 2 размеры
        self.lineEdit.setStyleSheet("border-radius:20px;\n" "border:2px solid #ffd;")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 10, 171, 31))
        self.label.setStyleSheet("color:#ffd;\n" "font: 12pt \"Simplex_IV50\";")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(330, 70, 191, 31))
        self.label_2.setStyleSheet("color:#ffd;\n" "font: 12pt \"Simplex_IV50\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 100, 113, 22))  # 1 координаты, 2 размеры
        self.lineEdit_3.setStyleSheet("border-radius:20px;\n" "border:2px solid #ffd;")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(330, 10, 191, 31))
        self.label_3.setStyleSheet("color:#ffd;\n" "font: 12pt \"Simplex_IV50\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 45, 113, 22))
        self.lineEdit_2.setStyleSheet("border-radius:20px;\n" "border:2px solid #ffd;")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(330, 130, 191, 31))
        self.label_4.setStyleSheet("color:#ffd;\n" "font: 12pt \"Simplex_IV50\";" "background:rgb(255,255,255,0)")
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 160, 50, 22))  # 1 координаты, 2 размеры
        self.lineEdit_4.setStyleSheet("border-radius:20px;\n" "border:2px solid #ffd;" "background:rgb(255,255,255,0)")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 340, 101, 41))
        self.pushButton_3.setStyleSheet("color: #fff;\n" "background:rgb(120, 192, 255)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.accept_pushButton.setText(_translate("Dialog", "Подверить "))
        self.label.setText(_translate("Dialog", "Название склада"))
        self.label_2.setText(_translate("Dialog", "Улица:"))
        self.label_3.setText(_translate("Dialog", "Город:"))
        self.label_4.setText(_translate("Dialog", "№ дома:"))
        self.pushButton_3.setText(_translate("Dialog", "Отменить"))
        self.pushButton_3.clicked.connect(Dialog.close)
        self.accept_pushButton.clicked.connect(partial(self.save_stock))

    def save_stock(self):
        location = geolocator.geocode(f"{self.lineEdit_2.text()},{self.lineEdit_3.text()},{self.lineEdit_4.text()}")
        print(location.address)
        print((location.latitude, location.longitude))

        conn = sqlite3.connect('warehouse.db')
        with conn:
            conn.execute("INSERT OR IGNORE INTO Stock (name, address, geo_text, geo_coordinates) values(?, ?, ?, ?)",
                         (self.lineEdit.text(), self.lineEdit_2.text(), location.address, f'{location.latitude}, {location.longitude}' ))
        conn.commit()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()










if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QDialog, QPushButton
from functools import partial
import sqlite3
# import datetime as DT
# print(DT.datetime.now())
# print(str(DT.datetime.now())[:10])
import os
import docxtpl


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
        self.lineEdit.setGeometry(QtCore.QRect(100, 70, 113, 22)) # 1 координаты, 2 размеры
        self.lineEdit.setStyleSheet("border-radius:20px;\n" "border:2px solid #ffd;")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 30, 171, 31))
        self.label.setStyleSheet("color:#ffd;\n" "font: 12pt \"Simplex_IV50\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 30, 191, 31))
        self.label_3.setStyleSheet("color:#ffd;\n" "font: 12pt \"Simplex_IV50\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 70, 113, 22))
        self.lineEdit_2.setStyleSheet("border-radius:20px;\n" "border:2px solid #ffd;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 340, 101, 41))
        self.pushButton_3.setStyleSheet("color: #fff;\n" "\n" "background:rgb(120, 192, 255)")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #     info_staff = cursor.fetchall()
    #     # list_of_names = [i[1] for i in list(info_staff)]
    #     # list_of_phones = [i[5] for i in list(info_staff)]
    # for i in range(0, len(list(info_staff))) :
    #     self.doctor_last_name.addItem("")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.accept_pushButton.setText(_translate("Dialog", "Подверить "))
        self.label.setText(_translate("Dialog", "Название"))
        self.label_3.setText(_translate("Dialog", "Введите адрес"))
        self.pushButton_3.setText(_translate("Dialog", "Отменить"))
        self.pushButton_3.clicked.connect(Dialog.close)
        self.accept_pushButton.clicked.connect(partial(self.save_stock))

    def save_stock(self):
        conn = sqlite3.connect('warehouse.db')
        with conn:
            conn.execute("INSERT OR IGNORE INTO Stock (name, address) values(?, ?)",
                         (self.lineEdit.text(), self.lineEdit_2.text()))
        conn.commit()
        self.lineEdit.clear()
        self.lineEdit_2.clear()









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

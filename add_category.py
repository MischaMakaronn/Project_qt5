# -*- coding: utf-8 -*-
from functools import partial
import push_product
# Form implementation generated from reading ui file 'add_category.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

conn = sqlite3.connect('warehouse.db')
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(605, 395)
        Dialog.setStyleSheet("background-image: url(\'OJ91CN0.jpg\');")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 20, 361, 31))
        self.label.setStyleSheet("color: #fff;\n"
"\n"
"font: 14pt \"Monotxt\";\n"
"\n"
"")
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 350, 101, 31))
        self.pushButton_5.setStyleSheet("border: 2px solid #ddd;\n"
"font: 63 9pt \"Yu Gothic UI Semibold\";\n"
"border-radius: 20px;\n"
"background: #fff;\n"
"color: #8cbaff;\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 350, 101, 31))
        self.pushButton_3.setStyleSheet("border: 2px solid #ddd;\n"
"font: 63 9pt \"Yu Gothic UI Semibold\";\n"
"color: #8cbaff;\n"
"border-radius: 20px;\n"
"background: #fff;\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 241, 31))
        self.label_2.setStyleSheet("color: #fff;\n"
"\n"
"\n"
"font: 75 10pt \"Myanmar Text\";\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(310, 110, 181, 31))
        self.label_3.setStyleSheet("color: #fff;\n"
"\n"
"\n"
"font: 75 10pt \"Myanmar Text\";\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(290, 150, 201, 111))
        self.textEdit_2.setStyleSheet("background: #ffd;\n"
"border: 2px solid #fff;\n"
"border-radius: 15px;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 150, 201, 111))
        self.textEdit_3.setStyleSheet("background: #ffd;\n"
"border: 2px solid #fff;\n"
"border-radius: 15px;")
        self.textEdit_3.setObjectName("textEdit_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Добавление категории"))
        self.pushButton_5.setText(_translate("Dialog", "Отменить"))
        self.pushButton_3.setText(_translate("Dialog", "Применить"))
        self.label_2.setText(_translate("Dialog", "Введите название категории"))
        self.label_3.setText(_translate("Dialog", "Описание категории"))
        self.pushButton_5.clicked.connect(Dialog.close)
        self.pushButton_3.clicked.connect(partial(self.create_new_category_goods))
        self.pushButton_3.clicked.connect(partial(self.result_create_category))
        self.pushButton_3.clicked.connect(Dialog.close)



    def create_new_category_goods(self):
        name_category = self.textEdit_3.toPlainText()
        description_category = self.textEdit_2.toPlainText()
        print(name_category)
        print(description_category)
        add_category_in_db = 'INSERT OR IGNORE INTO Category(name, description) values(?,?)'
        with conn:
            conn.execute(add_category_in_db, [f'{name_category}', f'{description_category}'])
        conn.commit()
        print(name_category)
        self.textEdit_2.clear()
        self.textEdit_3.clear()


    def result_create_category(self):
            Dialog = QtWidgets.QDialog()
            ui2 = push_product.Ui_Dialog()
            ui2.setupUi(Dialog)
            Dialog.show()
            Dialog.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-
from functools import partial

from PyQt5.QtWidgets import QWidget

import mainwindow as main_window
# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(775, 460)
        Dialog.setStyleSheet("background-image: url(\"OJ91CN0.jpg\");")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 50, 191, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 0, 171, 41))
        self.label.setStyleSheet("color: #fff;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"\n"
"\n"
"\n"
"")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(230, 90, 291, 87))
        self.textEdit.setStyleSheet("border:3px solid #ddd;\n"
"font: \"8514oem\";\n"
"background: #fff;\n"
"color: #8cbaff;\n"
"border-radius: 20px;")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 370, 111, 41))
        self.pushButton_2.setStyleSheet("border-radius: 20px;\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"font: 63 9pt \"Yu Gothic UI Semibold\";\n"
"background: #8ccfff;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 370, 111, 41))
        self.pushButton_4.setStyleSheet("border-radius: 20px;\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"font: 63 9pt \"Yu Gothic UI Semibold\";\n"
"background: #8ccfff;")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Выберите товар"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Введите информацию о товаре</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Применить"))
        self.pushButton_4.setText(_translate("Dialog", "Главная"))
        self.pushButton_4.clicked.connect(Dialog.close)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

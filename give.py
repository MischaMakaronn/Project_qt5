# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'give_product.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(594, 397)
        Dialog.setStyleSheet("background-image: url(\"OJ91CN0.jpg\");")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 30, 281, 41))
        self.label.setStyleSheet("color: #fff;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(172, 80, 251, 101))
        self.lineEdit.setStyleSheet("border: 2px solid #ddd;\n"
"border-radius: 20px;\n"
"background: #fff;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 360, 101, 31))
        self.pushButton_3.setStyleSheet("border: 2px solid #ddd;\n"
"font: 63 9pt \"Yu Gothic UI Semibold\";\n"
"color: #8cbaff;\n"
"border-radius: 20px;\n"
"background: #fff;\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 360, 101, 31))
        self.pushButton_5.setStyleSheet("border: 2px solid #ddd;\n"
"font: 63 9pt \"Yu Gothic UI Semibold\";\n"
"border-radius: 20px;\n"
"background: #fff;\n"
"color: #8cbaff;\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Введите номер перемещения"))
        self.pushButton_3.setText(_translate("Dialog", "Применить"))
        self.pushButton_5.setText(_translate("Dialog", "Отменить"))
        self.pushButton_5.clicked.connect(Dialog.close)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

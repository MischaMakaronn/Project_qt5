# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registernewsclad.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(577, 387)
        Dialog.setStyleSheet("background-image: url(\'C:/Users/admin/Desktop/OJ91CN0.jpg\');")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 340, 101, 41))
        self.pushButton.setStyleSheet("color: #fff;\n"
"\n"
"background:rgb(120, 192, 255)")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 70, 113, 22))
        self.lineEdit.setStyleSheet("border-radius:20px;\n"
"border:2px solid #ffd;")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 30, 171, 31))
        self.label.setStyleSheet("color:#ffd;\n"
"font: 12pt \"Simplex_IV50\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 30, 191, 31))
        self.label_3.setStyleSheet("color:#ffd;\n"
"font: 12pt \"Simplex_IV50\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 70, 113, 22))
        self.lineEdit_2.setStyleSheet("border-radius:20px;\n"
"border:2px solid #ffd;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 340, 101, 41))
        self.pushButton_3.setStyleSheet("color: #fff;\n"
"\n"
"background:rgb(120, 192, 255)")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Подверить "))
        self.label.setText(_translate("Dialog", "Название"))
        self.label_3.setText(_translate("Dialog", "Введите адрес"))
        self.pushButton_3.setText(_translate("Dialog", "Отменить"))
        self.pushButton_3.clicked.connect(Dialog.close)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

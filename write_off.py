# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'push_product111.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(605, 395)
        Dialog.setStyleSheet("background-image: url(\'C:/Users/admin/Desktop/OJ91CN0.jpg\');")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 10, 191, 21))
        self.label.setStyleSheet("color: #fff;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
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
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 30, 161, 31))
        self.pushButton_6.setStyleSheet("border: 2px solid #ddd;\n"
"font: 63 9pt \"Yu Gothic UI Semibold\";\n"
"color: #8cbaff;\n"
"border-radius: 20px;\n"
"background: #fff;\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 521, 261))
        self.tableWidget.setStyleSheet("\n"
"background:rgb(253, 255, 233)")
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("2")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(False)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(540, 100, 61, 51))
        self.pushButton_7.setStyleSheet("border: 2px solid #ddd;\n"
"font: 75 26pt \"MS Shell Dlg 2\";\n"
"\n"
"color: rgb(196, 255, 0);\n"
"border-radius: 20px;\n"
"background: #fff;\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(540, 170, 61, 51))
        self.pushButton_8.setStyleSheet("border: 2px solid #ddd;\n"
"font: 75 26pt \"MS Shell Dlg 2\";\n"
"\n"
"color: rgb(255, 64, 0);\n"
"border-radius: 20px;\n"
"background: #fff;\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Списание"))
        self.pushButton_5.setText(_translate("Dialog", "Отменить"))
        self.pushButton_3.setText(_translate("Dialog", "Применить"))
        self.pushButton_6.setText(_translate("Dialog", "Загрузить документ"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Cклад"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Категория"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Товар"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Количество"))
        self.pushButton_7.setText(_translate("Dialog", "+"))
        self.pushButton_8.setText(_translate("Dialog", "-"))
        self.pushButton_5.clicked.connect(Dialog.close)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

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
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 630)
        Dialog.setStyleSheet("background-image: url(OJ91CN0.jpg);")
        conn = sqlite3.connect('warehouse.db')
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 30, 400, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #46728a; font: bold 20pt MS Shell Dlg 2; background: transparent")
        self.label.setObjectName("label")
        self.category_combobox = QtWidgets.QComboBox(Dialog)
        self.category_combobox.setGeometry(QtCore.QRect(21, 375, 200, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.category_combobox.setFont(font)
        self.category_combobox.setStyleSheet("font: bold 10pt \"OCR A Extended\";\n"
                                             "border-radius: 12px;\n"
                                             "border: 5px solid #42abc3;\n"
                                             "color: #42abc3;\n"
                                             "background:#cddff3")
        self.category_combobox.setObjectName("comboBox")
        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Category")
            info_positions = cursor.fetchall()
            # list_of_names = [i[1] for i in list(info_staff)]
            # list_of_phones = [i[5] for i in list(info_staff)]
        for i in range(0, len(list(info_positions))):
            self.category_combobox.addItem("")

        self.goods_combobox = QtWidgets.QComboBox(Dialog)
        self.goods_combobox.setGeometry(QtCore.QRect(250, 375, 200, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.goods_combobox.setFont(font)
        self.goods_combobox.setStyleSheet("font: bold 10pt \"OCR A Extended\";\n"
                                          "border-radius: 12px;\n"
                                          "border: 5px solid #42abc3;\n"
                                          "color: #42abc3;\n"
                                          "background:#cddff3")
        self.goods_combobox.setObjectName("comboBox")
        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Goods")
            info_positions = cursor.fetchall()
            # list_of_names = [i[1] for i in list(info_staff)]
            # list_of_phones = [i[5] for i in list(info_staff)]
        for i in range(0, len(list(info_positions))):
            self.goods_combobox.addItem("")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 350, 144, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #46728a; font: bold 11pt MS Shell Dlg 2; background: transparent")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(470, 350, 144, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #46728a; font: bold 11pt MS Shell Dlg 2; background: transparent")
        self.label_3.setObjectName("label_3")
        self.goods_count_spinbox = QtWidgets.QSpinBox(Dialog)
        self.goods_count_spinbox.setGeometry(QtCore.QRect(470, 375, 200, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.goods_count_spinbox.setFont(font)
        self.goods_count_spinbox.setMaximum(1000000)
        self.goods_count_spinbox.setStyleSheet("font: bold 10pt \"OCR A Extended\";\n"
                                   "border-radius: 12px;\n"
                                   "border: 5px solid #42abc3;\n"
                                   "color: #42abc3;\n"
                                   "background:#cddff3")
        self.goods_count_spinbox.setObjectName("spinBox")

        self.price_spinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.price_spinBox.setGeometry(QtCore.QRect(700, 375, 200, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.price_spinBox.setFont(font)
        self.price_spinBox.setMaximum(1000000)
        self.price_spinBox.setStyleSheet("font: bold 10pt \"OCR A Extended\";\n"
                                         "border-radius: 12px;\n"
                                         "border: 5px solid #42abc3;\n"
                                         "color: #42abc3;\n"
                                         "background:#cddff3")
        self.price_spinBox.setObjectName("spinBox")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(920, 350, 144, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #46728a; font: bold 11pt MS Shell Dlg 2; background: transparent")
        self.label_4.setObjectName("label_4")
        self.warehouse_combobox = QtWidgets.QComboBox(Dialog)
        self.warehouse_combobox.setGeometry(QtCore.QRect(920, 375, 200, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.warehouse_combobox.setFont(font)
        self.warehouse_combobox.setStyleSheet("font: bold 10pt \"OCR A Extended\";\n"
                                              "border-radius: 12px;\n"
                                              "border: 5px solid #42abc3;\n"
                                              "color: #42abc3;\n"
                                              "background:#cddff3")
        self.warehouse_combobox.setObjectName("comboBox_2")
        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Stock")
            info_positions = cursor.fetchall()
            # list_of_names = [i[1] for i in list(info_staff)]
            # list_of_phones = [i[5] for i in list(info_staff)]
        for i in range(0, len(list(info_positions))):
            self.warehouse_combobox.addItem("")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(21, 430, 144, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #46728a; font: bold 11pt MS Shell Dlg 2; background: transparent")
        self.label_5.setObjectName("label_5")
        self.expiration_date_dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Dialog)
        self.expiration_date_dateTimeEdit_2.setGeometry(QtCore.QRect(270, 455, 230, 37))
        current_date = QtCore.QDate.currentDate()
        current_time = QtCore.QTime.currentTime()
        self.expiration_date_dateTimeEdit_2.setDate(current_date)
        self.expiration_date_dateTimeEdit_2.setTime(current_time)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.expiration_date_dateTimeEdit_2.setFont(font)
        self.expiration_date_dateTimeEdit_2.setCalendarPopup(True)
        self.expiration_date_dateTimeEdit_2.setStyleSheet("font: bold 10pt \"OCR A Extended\";\n"
                                          "border-radius: 12px;\n"
                                          "border: 5px solid #42abc3;\n"
                                          "color: #42abc3;\n"
                                          "background:#cddff3")
        self.expiration_date_dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(270, 430, 144, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #46728a; font: bold 11pt MS Shell Dlg 2; background: transparent")
        self.label_6.setObjectName("label_6")

        self.label_category = QtWidgets.QLabel(Dialog)
        self.label_category.setGeometry(QtCore.QRect(21, 350, 144, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_category.setFont(font)
        self.label_category.setStyleSheet("color: #46728a; font: bold 11pt MS Shell Dlg 2; background: transparent")
        self.label_category.setObjectName("label_category")

        self.price_label = QtWidgets.QLabel(Dialog)
        self.price_label.setGeometry(QtCore.QRect(700, 350, 144, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.price_label.setFont(font)
        self.price_label.setStyleSheet("color: #46728a; font: bold 11pt MS Shell Dlg 2; background: transparent")
        self.price_label.setObjectName("label_3")

        self.supply_date_dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.supply_date_dateTimeEdit.setGeometry(QtCore.QRect(21, 455, 230, 37))
        current_date = QtCore.QDate.currentDate()
        current_time = QtCore.QTime.currentTime()
        self.supply_date_dateTimeEdit.setDate(current_date)
        self.supply_date_dateTimeEdit.setTime(current_time)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.supply_date_dateTimeEdit.setFont(font)
        self.supply_date_dateTimeEdit.setCalendarPopup(True)
        self.supply_date_dateTimeEdit.setStyleSheet("font: bold 11pt \"OCR A Extended\";\n"
                                          "border-radius: 12px;\n"
                                          "border: 5px solid #42abc3;\n"
                                          "color: #42abc3;\n"
                                          "background:#cddff3")
        self.supply_date_dateTimeEdit.setObjectName("dateTimeEdit_3")
        self.accept_button_pushButton = QtWidgets.QPushButton(Dialog)
        self.accept_button_pushButton.setEnabled(False)
        self.accept_button_pushButton.setGeometry(QtCore.QRect(21, 550, 100, 42))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.accept_button_pushButton.setFont(font)
        self.accept_button_pushButton.setStyleSheet("font: bold 11pt \"OCR A Extended\";\n"
                                                    "border-radius: 12px;\n"
                                                    "border: 2px solid #42abc3;\n"
                                                    "color: #42abc3;\n"
                                                    "background:#cddff3")
        self.accept_button_pushButton.setObjectName("pushButton")
        self.cancel_button_pushButton = QtWidgets.QPushButton(Dialog)
        self.cancel_button_pushButton.setEnabled(False)

        self.cancel_button_pushButton.setGeometry(QtCore.QRect(150, 550, 100, 42))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_button_pushButton.setFont(font)
        self.cancel_button_pushButton.setStyleSheet("font: bold 10pt \"OCR A Extended\";\n"
                                                    "border-radius: 12px;\n"
                                                    "border: 2px solid #42abc3;\n"
                                                    "color: #42abc3;\n"
                                                    "background:#cddff3")
        self.cancel_button_pushButton.setObjectName("pushButton_2")
        self.load_doc_pushButton = QtWidgets.QPushButton(Dialog)
        self.load_doc_pushButton.setEnabled(False)
        self.load_doc_pushButton.setGeometry(QtCore.QRect(970, 530, 150, 55))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.load_doc_pushButton.setFont(font)
        self.load_doc_pushButton.setStyleSheet("font: bold 11pt \"OCR A Extended\";\n"
                                               "border-radius: 12px;\n"
                                               "border: 2px solid #42abc3;\n"
                                               "color: #42abc3;\n"
                                               "background:#cddff3")
        self.load_doc_pushButton.setObjectName("pushButton_3")

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(25, 80, 800, 261))
        self.tableWidget.setStyleSheet("background: ")
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        # self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setFixedSize(1100, 260)

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
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setItalic(True)
        item.setFont(font)

        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.add_button_pushButton = QtWidgets.QPushButton(Dialog)
        self.add_button_pushButton.setGeometry(QtCore.QRect(1130, 80, 61, 51))
        self.add_button_pushButton.setStyleSheet("border: 2px solid #ddd;\n"
                                                 "font: 75 26pt \"Arial Black\";\n"
                                                 "\n"
                                                 "color: rgb(196, 255, 0);\n"
                                                 "border-radius: 20px;\n"
                                                 "background: #fff;\n"
                                                 "")
        self.add_button_pushButton.setObjectName("pushButton_7")
        self.delete_button_pushButton = QtWidgets.QPushButton(Dialog)
        self.delete_button_pushButton.setGeometry(QtCore.QRect(1130, 140, 61, 51))
        self.delete_button_pushButton.setStyleSheet("border: 2px solid #ddd;\n"
                                                    "font: 75 26pt \"Arial Black\";\n"
                                                    "\n"
                                                    "color: rgb(255, 64, 0);\n"
                                                    "border-radius: 20px;\n"
                                                    "background: #fff;\n"
                                                    "")
        self.delete_button_pushButton.setObjectName("pushButton_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        conn = sqlite3.connect('warehouse.db')
        self.label.setText(_translate("Dialog", "Оформление поставки товара"))
        self.label_2.setText(_translate("Dialog", "Выбрать товар:"))
        self.label_3.setText(_translate("Dialog", "Количество:"))
        self.label_4.setText(_translate("Dialog", "Выбрать склад:"))
        self.label_5.setText(_translate("Dialog", "Дата поставки:"))
        self.price_label.setText(_translate("Dialog", "Цена, руб.:"))
        self.expiration_date_dateTimeEdit_2.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd HH:mm"))
        self.label_6.setText(_translate("Dialog", "Срок годности:"))
        self.label_category.setText(_translate("Dialog", "Категория:"))
        self.supply_date_dateTimeEdit.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd HH:mm"))
        self.accept_button_pushButton.setText(_translate("Dialog", "Принять"))
        self.cancel_button_pushButton.setText(_translate("Dialog", "Отменить"))
        self.load_doc_pushButton.setText(_translate("Dialog", "Загрузить\nдокумент"))
        self.add_button_pushButton.setText(_translate("Dialog", "+"))
        self.delete_button_pushButton.setText(_translate("Dialog", "-"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Категория"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Товар"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Количество"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Цена"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Склад"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Дата поставки"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Срок годности"))

        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Category")
            info_category = cursor.fetchall()
            list_of_categories = [i[1] for i in list(info_category)]  # список категорий товара
        for num in range(0, len(list(info_category))):  # заполняем комбо виджет из списка категорий
            self.category_combobox.setItemText(num, _translate("Dialog", f"{list_of_categories[num]}"))
        print("Текущая категория", self.category_combobox.currentText())
        category_name = self.category_combobox.currentText()
        with conn:
            cat_id = [i[0] for i in conn.execute(f"SELECT * FROM Category WHERE name = '{category_name}'")][0]
        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Stock")
            info_warehouse = cursor.fetchall()
            list_of_warehouses = [i[1] for i in list(info_warehouse)]  # список складов
        for num in range(0, len(list(info_warehouse))):  # заполняем комбо виджет из списка складов
            self.warehouse_combobox.setItemText(num, _translate("Dialog", f"{list_of_warehouses[num]}"))
        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Goods where category_id = {cat_id}")
            info_goods = cursor.fetchall()
            list_of_goods = [i[2] for i in list(info_goods)]  # список товаров
        for num in range(0, len(list(info_goods))):  # заполняем комбо виджет из списка товаров
            self.goods_combobox.setItemText(num, _translate("Dialog", f"{list_of_goods[num]}"))

            # self.tableWidget.insertRow(0)
            self.tableWidget.setItem(0, 0, QTableWidgetItem(self.category_combobox.currentText()))
            self.tableWidget.setItem(0, 1, QTableWidgetItem(self.goods_combobox.currentText()))
            self.tableWidget.setItem(0, 2, QTableWidgetItem(self.goods_count_spinbox.text()))
            self.tableWidget.setItem(0, 3, QTableWidgetItem(self.price_spinBox.text()))
            self.tableWidget.setItem(0, 4, QTableWidgetItem(self.warehouse_combobox.currentText()))
            self.tableWidget.setItem(0, 5, QTableWidgetItem(self.supply_date_dateTimeEdit.text()))
            self.tableWidget.setItem(0, 6, QTableWidgetItem(self.expiration_date_dateTimeEdit_2.text()))


        self.category_combobox.currentIndexChanged.connect(partial(self.update_goods_combobox))
        self.add_button_pushButton.clicked.connect(self.add_raw)
        self.delete_button_pushButton.clicked.connect(partial(self.delete_row))  # по клику на "-" удаляем строку
        self.goods_combobox.currentIndexChanged.connect(partial(self.update_good_from_combobox))
        self.warehouse_combobox.currentIndexChanged.connect(partial(self.update_warehouse_from_combobox))
        self.goods_count_spinbox.valueChanged.connect(partial(self.update_count_from_spinbox))
        self.price_spinBox.valueChanged.connect(partial(self.update_price_from_spinbox))
        self.tableWidget.cellDoubleClicked.connect(partial(self.cell_double_clicked))  # по даблклику на ячейку активируем "Отменить" и "Принять"
        self.supply_date_dateTimeEdit.dateTimeChanged.connect(partial(self.update_supply_date_from_dateTimeEdit))
        self.expiration_date_dateTimeEdit_2.dateTimeChanged.connect(partial(self.update_expiration_date_dateTimeEdit_2))
        self.accept_button_pushButton.clicked.connect(partial(self.save_goods_supply))
        self.load_doc_pushButton.clicked.connect(partial(self.load_supply_act))
        self.cancel_button_pushButton.clicked.connect(Dialog.close)

    def update_goods_combobox(self, index):
        _translate = QtCore.QCoreApplication.translate
        conn = sqlite3.connect('warehouse.db')
        self.goods_combobox.clear()
        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Goods where category_id = {index + 1}")
            info_goods = cursor.fetchall()
            print(info_goods)
            list_of_goods = [i[2] for i in list(info_goods)]  # список товаров
        self.goods_combobox.addItems(list_of_goods)
        self.tableWidget.setItem(self.tableWidget.currentRow(), 0,
                                 QTableWidgetItem(self.category_combobox.currentText()))
        self.tableWidget.setItem(self.tableWidget.currentRow(), 1, QTableWidgetItem(self.goods_combobox.currentText()))
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)

    # def save_goods_supply(self):  # функция для сохранения изменений в базе данных
    #     conn = sqlite3.connect('warehouse.db')
    #     print("Товар", self.goods_combobox.currentText())
    #     print("Склад", self.warehouse_combobox.currentText())
    #     print("Количество", self.goods_count_spinbox.text())
    #     print("Цена", self.price_spinBox.text())
    #     print("Дата и время поставки", self.supply_date_dateTimeEdit.text())
    #     print("Срок годности до", self.expiration_date_dateTimeEdit_2.text())
    #     try:
    #         with conn:
    #             good_id = [i[0] for i in conn.execute(f"SELECT * FROM Goods WHERE name = '{self.goods_combobox.currentText()}'")][0]
    #             stock_id = [i[0] for i in conn.execute(f"SELECT * FROM Stock WHERE name = '{self.warehouse_combobox.currentText()}'")][0]
    #             count_in = int(self.goods_count_spinbox.text())
    #             count_current = int(self.goods_count_spinbox.text())
    #             supply_date = self.supply_date_dateTimeEdit.text()
    #             expiration_date = self.expiration_date_dateTimeEdit_2.text()
    #             price = float(self.price_spinBox.text().replace(',', '.'))
    #             print([i[0] for i in conn.execute(f"SELECT * FROM Supply")])
    #             if len([i[0] for i in conn.execute(f"SELECT * FROM Supply")]) != 0:
    #                 supply_id = [i[0] for i in conn.execute(f"SELECT * FROM Supply")][-1]
    #             else:
    #                 supply_id = 0
    #             date_current = DT.datetime.now()
    #             print(date_current)
    #             year = str(date_current)[:4]
    #             month = str(date_current)[5:7]
    #             day = str(date_current)[8:10]
    #             calendar_dict = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая',
    #                              '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября',
    #                              '11': 'ноября', '12': 'декабря'}
    #             global document
    #             document = f'act_{str(date_current)[:19].replace(":", "_").replace(" ", "_")}.docx'
    #             conn.execute("INSERT OR IGNORE INTO Supply (good_id, price, stock_id, count_in, count_current, supply_date, expiration_date, document) values(?, ?, ?, ?, ?, ?, ?, ?)",
    #                          (good_id, price, stock_id, count_in, count_current, supply_date, expiration_date, document))
    #         conn.commit()
    #         doc_in = docxtpl.DocxTemplate('supplydocs/template_supply.docx')
    #         context = {"name": self.goods_combobox.currentText(),
    #                    'stock': self.warehouse_combobox.currentText(),
    #                    'expiration_date': self.supply_date_dateTimeEdit.text(),
    #                    'count': int(self.goods_count_spinbox.text()),
    #                    'price': price,
    #                    'total_price': price * count_in,
    #                    'year': year,
    #                    'month': calendar_dict[month],
    #                    'day': day,
    #                    'act_number': (supply_id + 1),
    #                    "position": "Директор",
    #                    'director': "К.Каліноўскі"}
    #         doc_in.render(context)
    #         doc_in.save(f"supplydocs//{document}")
    #         time.sleep(2)
    #     except Exception as e:
    #         print(e)
    #     self.cancel_button_pushButton.setEnabled(False)
    #     self.accept_button_pushButton.setEnabled(False)
    #     self.load_doc_pushButton.setEnabled(True)

    def update_good_from_combobox(self, index):
        _translate = QtCore.QCoreApplication.translate
        # self.tableWidget.selectRow(raw)
        self.tableWidget.setItem(self.tableWidget.currentRow(), 1, QTableWidgetItem(self.goods_combobox.currentText()))
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)


    def update_warehouse_from_combobox(self, index):
        _translate = QtCore.QCoreApplication.translate
        # self.tableWidget.selectRow(raw)
        self.tableWidget.setItem(self.tableWidget.currentRow(), 4,
                                 QTableWidgetItem(self.warehouse_combobox.currentText()))
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)


    def update_count_from_spinbox(self, value):
        _translate = QtCore.QCoreApplication.translate
        # self.tableWidget.selectRow(raw)
        self.tableWidget.setItem(self.tableWidget.currentRow(), 2, QTableWidgetItem(str(value)))
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)


    def update_price_from_spinbox(self, value):
        _translate = QtCore.QCoreApplication.translate
        # self.tableWidget.selectRow(raw)
        self.tableWidget.setItem(self.tableWidget.currentRow(), 3, QTableWidgetItem(str(value)))
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)


    def add_raw(self):  # для добавления нового ряда в таблицу
        self.tableWidget.insertRow(self.tableWidget.rowCount())  # Добавляем новый ряд в таблицу
        self.tableWidget.setCurrentCell(self.tableWidget.rowCount() - 1, 0)  # Устанавливаем фокус на новый ряд
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)


    def delete_row(self, table_name):  # функция для удаления выбранной строки из таблицы
        row = self.tableWidget.currentRow()  # получаем индекс выбранной строки
        self.tableWidget.removeRow(row)  # удаляем строку из таблицы
        # self.cancel_button.setEnabled(True)
        # self.accept_button.setEnabled(True)


    def cell_double_clicked(self):
        print("Активируеи кнопки Отменить и Применить при даблклике в ячейке")
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)


    def update_supply_date_from_dateTimeEdit(self, date):
        _translate = QtCore.QCoreApplication.translate
        # self.tableWidget.selectRow(raw)
        self.tableWidget.setItem(self.tableWidget.currentRow(), 5,
                                 QTableWidgetItem(self.supply_date_dateTimeEdit.text()))
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)

    def update_expiration_date_dateTimeEdit_2(self, date):
        _translate = QtCore.QCoreApplication.translate
        # self.tableWidget.selectRow(raw)
        self.tableWidget.setItem(self.tableWidget.currentRow(), 6,
                                 QTableWidgetItem(self.expiration_date_dateTimeEdit_2.text()))
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)


    # def load_supply_act(self):
    #     ddoc = "C://Users//voyag//PycharmProjects//Project_qt5//supplydocs//" + document
    #     os.startfile(ddoc)


    def save_goods_supply(self):  # функция для сохранения изменений в базе данных
        try:
            rows = self.tableWidget.rowCount()  # получаем количество строк и столбцов таблицы
            print('rows', rows)
            columns = self.tableWidget.columnCount()
            data = []  # создаем список для хранения данных из таблицы
            for i in range(rows):  # перебираем все строки и столбцы таблицы
                row_data = []
                for j in range(columns):
                    item = self.tableWidget.item(i, j)  # получаем значение из каждой ячейки
                    value = item.text()
                    row_data.append(value)  # добавляем значение в список для текущей строки
                data.append(row_data)  # добавляем список для текущей строки в общий список
                print('row data', row_data)
                print("data", data)
        except Exception as e:
            print(e)
        conn = sqlite3.connect('warehouse.db')
        try:
            global document_list
            document_list = []
            for row in data:  # вставляем данные из списка в базу данных
                print("Категория", row[0])
                print("Товар", row[1])
                print("Склад", row[4])
                print("Количество", row[2])
                print("Цена", row[3])
                print("Дата и время поставки", row[5])
                print("Срок годности до", row[6])
                with conn:
                    good_id = [i[0] for i in conn.execute(f"SELECT * FROM Goods WHERE name = '{row[1]}'")][0]
                    stock_id = [i[0] for i in conn.execute(f"SELECT * FROM Stock WHERE name = '{row[4]}'")][0]
                    count_in = int(row[2])
                    count_current = int(row[2])
                    supply_date = row[5]
                    expiration_date = row[6]
                    price = float(row[3].replace(',', '.'))
                    print([i[0] for i in conn.execute(f"SELECT * FROM Supply")])
                    if len([i[0] for i in conn.execute(f"SELECT * FROM Supply")]) != 0:
                        supply_id = [i[0] for i in conn.execute(f"SELECT * FROM Supply")][-1]
                    else:
                        supply_id = 0
                    date_current = DT.datetime.now()
                    print(date_current)
                    year = str(date_current)[:4]
                    month = str(date_current)[5:7]
                    day = str(date_current)[8:10]
                    calendar_dict = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая',
                                     '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября',
                                     '11': 'ноября', '12': 'декабря'}
                    global document
                    document = f'act_{str(date_current)[:19].replace(":", "_").replace(" ", "_")}.docx'
                    document_list.append(document)
                    conn.execute("INSERT OR IGNORE INTO Supply (good_id, price, stock_id, count_in, count_current, "
                                 "supply_date, expiration_date, document) values(?, ?, ?, ?, ?, ?, ?, ?)",
                                 (good_id, price, stock_id, count_in, count_current, supply_date, expiration_date, document))
                conn.commit()
                # """Открываем шаблон документа и заполняем теги"""
                doc_in = docxtpl.DocxTemplate('supplydocs/template_supply.docx')
                context = {"name": row[1],
                           'stock': row[4],
                           'expiration_date': row[6],
                           'count': int(row[2]),
                           'price': price,
                           'total_price': price * count_in,
                           'year': year,
                           'month': calendar_dict[month],
                           'day': day,
                           'act_number': (supply_id + 1),
                           "position": "Директор",
                           'director': "К.Каліноўскі"}
                doc_in.render(context)
                doc_in.save(f"supplydocs//{document}")
                time.sleep(2)
        except Exception as e:
            print("аааа", e)
        self.cancel_button_pushButton.setEnabled(False)
        self.accept_button_pushButton.setEnabled(False)
        self.load_doc_pushButton.setEnabled(True)

    def load_supply_act(self):
        print(document_list)
        for doc in document_list:
            doc_to_open = "C://Users//voyag//PycharmProjects//Project_qt5//supplydocs//" + doc
            os.startfile(doc_to_open)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

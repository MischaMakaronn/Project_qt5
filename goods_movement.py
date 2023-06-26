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


class ComboBox(QtWidgets.QComboBox):
    popupAboutToBeShown = QtCore.pyqtSignal()

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        super(ComboBox, self).showPopup()


class Ui_Dialog(object):
    # def __init__(self):
    #     super().__init__()
    #
    #     self.setupUi()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 630)
        Dialog.setStyleSheet("background-image: url(\"OJ91CN0.jpg\");")
        conn = sqlite3.connect('warehouse.db')
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 10, 295, 37))
        self.label.setStyleSheet("color: #46728a; font: bold 17pt MS Shell Dlg 2; background: transparent")
        self.label.setObjectName("label")
        self.label_category = QtWidgets.QLabel(Dialog)
        self.label_category.setGeometry(QtCore.QRect(190, 350, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_category.setFont(font)
        self.label_category.setStyleSheet("color: #46728a; font: bold 12pt MS Shell Dlg 2; background: transparent")
        self.label_category.setObjectName("label_category")
        self.label_warehouse = QtWidgets.QLabel(Dialog)
        self.label_warehouse.setGeometry(QtCore.QRect(20, 350, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_warehouse.setFont(font)
        self.label_warehouse.setStyleSheet("color: #46728a; font: bold 12pt MS Shell Dlg 2; background: transparent")
        self.label_warehouse.setObjectName("label_warehouse")

        self.label_warehouse_out = QtWidgets.QLabel(Dialog)
        self.label_warehouse_out.setGeometry(QtCore.QRect(20, 420, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_warehouse_out.setFont(font)
        self.label_warehouse_out.setStyleSheet(
            "color: #46728a; font: bold 12pt MS Shell Dlg 2; background: transparent")
        self.label_warehouse_out.setObjectName("label_warehouse")

        self.label_goods = QtWidgets.QLabel(Dialog)
        self.label_goods.setGeometry(QtCore.QRect(360, 350, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_goods.setFont(font)
        self.label_goods.setStyleSheet("color: #46728a; font: bold 12pt MS Shell Dlg 2; background: transparent")
        self.label_goods.setObjectName("label_goods")
        self.label_goods_count = QtWidgets.QLabel(Dialog)
        self.label_goods_count.setGeometry(QtCore.QRect(360, 420, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_goods_count.setFont(font)
        self.label_goods_count.setStyleSheet("color: #46728a; font: bold 12pt MS Shell Dlg 2; background: transparent")
        self.label_goods_count.setObjectName("label_goods_count")
        self.label_supply_number = QtWidgets.QLabel(Dialog)
        self.label_supply_number.setGeometry(QtCore.QRect(530, 350, 420, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_supply_number.setFont(font)
        self.label_supply_number.setStyleSheet(
            "color: #46728a; font: bold 12pt MS Shell Dlg 2; background: transparent")
        self.label_supply_number.setObjectName("label_goods_count")

        self.label_supply_date = QtWidgets.QLabel(Dialog)
        self.label_supply_date.setGeometry(QtCore.QRect(530, 420, 420, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_supply_date.setFont(font)
        self.label_supply_date.setStyleSheet("color: #46728a; font: bold 12pt MS Shell Dlg 2; background: transparent")
        self.label_supply_date.setObjectName("label_goods_count")

        self.supply_date_dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.supply_date_dateTimeEdit.setGeometry(QtCore.QRect(530, 450, 240, 37))
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
        self.supply_date_dateTimeEdit.setStyleSheet("font: bold 11pt \"Arial Black\";\n"
                                                    "border-radius: 12px;\n"
                                                    "border: 5px solid #42abc3;\n"
                                                    "color: #42abc3;\n"
                                                    "background:#cddff3")
        self.supply_date_dateTimeEdit.setObjectName("dateTimeEdit_3")

        self.cancel_button_pushButton = QtWidgets.QPushButton(Dialog)
        self.cancel_button_pushButton.setEnabled(False)
        self.cancel_button_pushButton.setGeometry(QtCore.QRect(140, 580, 115, 42))
        self.cancel_button_pushButton.setStyleSheet("font: bold 10pt \"Arial Black\";\n"
                                                    "border-radius: 12px;\n"
                                                    "border: 2px solid #42abc3;\n"
                                                    "color: #42abc3;\n"
                                                    "background:#cddff3")
        self.cancel_button_pushButton.setObjectName("pushButton_5")
        self.accept_button_pushButton = QtWidgets.QPushButton(Dialog)
        self.accept_button_pushButton.setEnabled(False)
        self.accept_button_pushButton.setGeometry(QtCore.QRect(20, 580, 115, 42))
        self.accept_button_pushButton.setStyleSheet("font: bold 10pt \"Arial Black\";\n"
                                                    "border-radius: 12px;\n"
                                                    "border: 2px solid #42abc3;\n"
                                                    "color: #42abc3;\n"
                                                    "background:#cddff3")
        self.accept_button_pushButton.setObjectName("pushButton_3")
        self.load_doc_pushButton = QtWidgets.QPushButton(Dialog)
        self.load_doc_pushButton.setEnabled(False)
        self.load_doc_pushButton.setGeometry(QtCore.QRect(1050, 10, 120, 60))
        self.load_doc_pushButton.setStyleSheet("font: bold 11pt \"Arial Black\";\n"
                                               "border-radius: 12px;\n"
                                               "border: 2px solid #42abc3;\n"
                                               "color: #42abc3;\n"
                                               "background:#cddff3")

        # self.pushButton_6.setStyleSheet("border: 2px solid #ddd; font: 63 9pt Yu Gothic UI Semibold; color: #8cbaff; border-radius: 20px; background: #fff;")
        self.load_doc_pushButton.setObjectName("pushButton_6")

        self.category_combobox = QtWidgets.QComboBox(Dialog)
        self.category_combobox.setGeometry(QtCore.QRect(190, 380, 150, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.category_combobox.setFont(font)
        self.category_combobox.setStyleSheet("font: bold 11pt \"Arial Black\";\n"
                                             "border-radius: 12px;\n"
                                             "border: 5px solid #42abc3;\n"
                                             "color: #42abc3;\n"
                                             "background:#cddff3")
        self.category_combobox.setObjectName("comboBox")
        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Category")
            info_category = cursor.fetchall()
            # list_of_names = [i[1] for i in list(info_staff)]
            # list_of_phones = [i[5] for i in list(info_staff)]
        for i in range(0, len(list(info_category))):
            self.category_combobox.addItem("")

        self.warehouse_combobox = QtWidgets.QComboBox(Dialog)
        self.warehouse_combobox.setGeometry(QtCore.QRect(20, 380, 150, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.warehouse_combobox.setFont(font)
        self.warehouse_combobox.setStyleSheet("font: bold 11pt \"Arial Black\";\n"
                                              "border-radius: 12px;\n"
                                              "border: 5px solid #42abc3;\n"
                                              "color: #42abc3;\n"
                                              "background:#cddff3")
        self.warehouse_combobox.setObjectName("comboBox")
        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Stock")
            info_warehouse = cursor.fetchall()
            # list_of_names = [i[1] for i in list(info_staff)]
            # list_of_phones = [i[5] for i in list(info_staff)]
        for i in range(0, len(list(info_warehouse))):
            self.warehouse_combobox.addItem("")

        self.warehouse_combobox_out = QtWidgets.QComboBox(Dialog)
        self.warehouse_combobox_out.setGeometry(QtCore.QRect(20, 450, 150, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.warehouse_combobox_out.setFont(font)
        self.warehouse_combobox_out.setStyleSheet("font: bold 11pt \"Arial Black\";\n"
                                                  "border-radius: 12px;\n"
                                                  "border: 5px solid #42abc3;\n"
                                                  "color: #42abc3;\n"
                                                  "background:#cddff3")
        self.warehouse_combobox_out.setObjectName("comboBox")
        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Stock")
            info_warehouse_out = cursor.fetchall()
            # list_of_names = [i[1] for i in list(info_staff)]
            # list_of_phones = [i[5] for i in list(info_staff)]
        for i in range(0, len(list(info_warehouse_out))):
            self.warehouse_combobox_out.addItem("")

        self.goods_combobox = QtWidgets.QComboBox(Dialog)
        self.goods_combobox.setGeometry(QtCore.QRect(360, 380, 150, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.goods_combobox.setFont(font)
        self.goods_combobox.setStyleSheet("font: bold 11pt \"Arial Black\";\n"
                                          "border-radius: 12px;\n"
                                          "border: 5px solid #42abc3;\n"
                                          "color: #42abc3;\n"
                                          "background:#cddff3")
        self.goods_combobox.setObjectName("comboBox")
        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Goods")
            info_goods = cursor.fetchall()
            # list_of_names = [i[1] for i in list(info_staff)]
            # list_of_phones = [i[5] for i in list(info_staff)]
        for i in range(0, len(list(info_goods))):
            self.goods_combobox.addItem("")

        self.supply_number_combobox = ComboBox(Dialog)
        self.supply_number_combobox.setGeometry(QtCore.QRect(530, 380, 420, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.supply_number_combobox.setFont(font)
        self.supply_number_combobox.setStyleSheet("font: bold 11pt \"Arial Black\";\n"
                                                  "border-radius: 12px;\n"
                                                  "border: 5px solid #42abc3;\n"
                                                  "color: #42abc3;\n"
                                                  "background:#cddff3")
        self.supply_number_combobox.setObjectName("supply_number_combobox")
        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Supply")
            info_supply = cursor.fetchall()
        for i in range(0, len(list(info_supply))):
            self.supply_number_combobox.addItem("")

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 521, 261))
        self.tableWidget.setStyleSheet("background: ")
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        # self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setFixedSize(1000, 260)

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
        self.add_button_pushButton.setGeometry(QtCore.QRect(1050, 80, 61, 51))
        self.add_button_pushButton.setStyleSheet("border: 2px solid #ddd;\n"
                                                 "font: 75 26pt \"Arial Black\";\n"
                                                 "\n"
                                                 "color: rgb(196, 255, 0);\n"
                                                 "border-radius: 20px;\n"
                                                 "background: #fff;\n"
                                                 "")
        self.add_button_pushButton.setObjectName("pushButton_7")
        self.delete_button_pushButton = QtWidgets.QPushButton(Dialog)
        self.delete_button_pushButton.setGeometry(QtCore.QRect(1110, 80, 61, 51))
        self.delete_button_pushButton.setStyleSheet("border: 2px solid #ddd;\n"
                                                    "font: 75 26pt \"Arial Black\";\n"
                                                    "\n"
                                                    "color: rgb(255, 64, 0);\n"
                                                    "border-radius: 20px;\n"
                                                    "background: #fff;\n"
                                                    "")
        self.delete_button_pushButton.setObjectName("pushButton_8")
        self.goods_count_spinbox = QtWidgets.QSpinBox(Dialog)
        self.goods_count_spinbox.setGeometry(QtCore.QRect(360, 450, 150, 37))
        self.goods_count_spinbox.setMaximum(1000000)
        self.goods_count_spinbox.setValue(0)
        self.goods_count_spinbox.setStyleSheet("font: bold 11pt \"Arial Black\";\n"
                                               "border-radius: 12px;\n"
                                               "border: 5px solid #42abc3;\n"
                                               "color: #42abc3;\n"
                                               "background:#cddff3;")
        self.goods_count_spinbox.setObjectName("good_count_spinbox")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        conn = sqlite3.connect('warehouse.db')
        self.label.setText(_translate("Dialog", "Переместить товар"))
        self.label_category.setText(_translate("Dialog", "Категория:"))
        self.label_warehouse.setText(_translate("Dialog", "Со склада:"))
        self.label_warehouse_out.setText(_translate("Dialog", "На склад:"))
        self.label_goods.setText(_translate("Dialog", "Товар:"))
        self.label_goods_count.setText(_translate("Dialog", "Количество:"))
        self.label_supply_number.setText(_translate("Dialog", "Номер и дата поставки / перемещения:"))
        self.label_supply_date.setText(_translate("Dialog", "Дата текущего перемещения:"))
        self.cancel_button_pushButton.setText(_translate("Dialog", "Отменить"))
        self.accept_button_pushButton.setText(_translate("Dialog", "Применить"))
        self.load_doc_pushButton.setText(_translate("Dialog", "Загрузить\nакт"))
        self.supply_date_dateTimeEdit.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd HH:mm"))

        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Со склада"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Категория"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Товар"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Количество"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Номер и дата поставки"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "На склад"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Дата перемещения"))

        self.add_button_pushButton.setText(_translate("Dialog", "+"))
        self.delete_button_pushButton.setText(_translate("Dialog", "-"))

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
            self.warehouse_combobox_out.setItemText(num, _translate("Dialog", f"{list_of_warehouses[num]}"))

        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM Goods WHERE category_id = {cat_id}")
                info_goods = cursor.fetchall()
                list_of_goods = [i[2] for i in list(info_goods)]  # список товаров
        except Exception as e:
            print(e)
        for num in range(0, len(list(info_goods))):  # заполняем комбо виджет из списка товаров
            self.goods_combobox.setItemText(num, _translate("Dialog", f"{list_of_goods[num]}"))
        print("Текущий товар", self.goods_combobox.currentText())
        good_name = self.goods_combobox.currentText()
        with conn:
            good_id = [i[0] for i in conn.execute(f"SELECT * FROM Goods WHERE name = '{good_name}'")][0]
            cursor = conn.cursor()
            # cursor.execute(f"SELECT * FROM Supply WHERE good_id = '{good_id}'")
            cursor.execute(f"SELECT * FROM Supply")
            info_supplies = cursor.fetchall()
            list_of_supplies = [f"{i[0]}. {i[6]}" for i in list(info_supplies)]  # список поставок
            print(list_of_supplies)
        if len(list_of_supplies) != 0:
            for num in range(0, len(list(info_supplies))):  # заполняем комбо виджет из списка поставок
                self.supply_number_combobox.setItemText(num, _translate("Dialog", f"{list_of_supplies[num]}"))
        else:
            self.supply_number_combobox.setItemText(0, _translate("Dialog", f"поставок нет"))

        # self.tableWidget.insertRow(0)
        self.tableWidget.setItem(0, 0, QTableWidgetItem(self.warehouse_combobox.currentText()))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(self.category_combobox.currentText()))
        self.tableWidget.setItem(0, 2, QTableWidgetItem(self.goods_combobox.currentText()))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("0"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("указать"))
        self.tableWidget.setItem(0, 5, QTableWidgetItem(self.warehouse_combobox_out.currentText()))
        self.tableWidget.setItem(0, 6, QTableWidgetItem(self.supply_date_dateTimeEdit.text()))


        self.add_button_pushButton.clicked.connect(self.add_raw)
        self.delete_button_pushButton.clicked.connect(partial(self.delete_row))  # по клику на "-" удаляем строку
        self.category_combobox.currentIndexChanged.connect(partial(self.update_goods_combobox))
        self.goods_combobox.currentIndexChanged.connect(partial(self.update_good_from_combobox))
        self.supply_number_combobox.popupAboutToBeShown.connect(partial(self.update_supply_combobox))
        self.warehouse_combobox.currentIndexChanged.connect(partial(self.update_warehouse_from_combobox))
        self.goods_count_spinbox.valueChanged.connect(partial(self.update_count_from_spinbox))
        self.tableWidget.cellDoubleClicked.connect(partial(self.cell_double_clicked))  # по даблклику на ячейку активируем "Отменить" и "Принять"
        self.supply_number_combobox.currentIndexChanged.connect(partial(self.update_table_supply_number_from_combobox))
        self.supply_date_dateTimeEdit.dateTimeChanged.connect(partial(self.update_supply_date_from_dateTimeEdit))
        self.warehouse_combobox_out.currentIndexChanged.connect(partial(self.update_warehouse_out_from_combobox))
        self.accept_button_pushButton.clicked.connect(partial(self.save_write_off))
        self.cancel_button_pushButton.clicked.connect(Dialog.close)
        self.load_doc_pushButton.clicked.connect(partial(self.load_movement_act))

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
        # for num in range(0, len(list(info_goods))):  # заполняем комбо виджет из списка товаров
        #     self.goods_combobox.setItemText(num, _translate("Dialog", f"{list_of_goods[num]}"))
        self.goods_combobox.addItems(list_of_goods)
        # self.tableWidget.selectRow(raw)
        self.tableWidget.setItem(self.tableWidget.currentRow(), 1,
                                 QTableWidgetItem(self.category_combobox.currentText()))
        self.tableWidget.setItem(self.tableWidget.currentRow(), 2, QTableWidgetItem(self.goods_combobox.currentText()))
        # self.tableWidget.setItem(self.tableWidget.currentRow(), 0, QTableWidgetItem(self.warehouse_combobox.currentText()))
        # self.tableWidget.setItem(self.tableWidget.currentRow(), 1, QTableWidgetItem(self.category_combobox.currentText()))
        # self.tableWidget.setItem(self.tableWidget.currentRow(), 3, QTableWidgetItem("0"))
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)

    def update_good_from_combobox(self, index):
        _translate = QtCore.QCoreApplication.translate
        # self.tableWidget.selectRow(raw)
        self.tableWidget.setItem(self.tableWidget.currentRow(), 2, QTableWidgetItem(self.goods_combobox.currentText()))
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)

    def update_supply_combobox(self):
        _translate = QtCore.QCoreApplication.translate
        conn = sqlite3.connect('warehouse.db')
        self.supply_number_combobox.clear()
        print(self.goods_combobox.currentText())
        print("text")
        good_id = [i[0] for i in conn.execute(f"SELECT * FROM Goods WHERE name = '{self.goods_combobox.currentText()}'")]
        stock_id = [i[0] for i in conn.execute(f"SELECT * FROM Stock WHERE name = '{self.warehouse_combobox.currentText()}'")][0]
        print("айди товара", good_id, "айди склада", stock_id)
        with conn:
            # список первичных поставок, где на первом складе текущее количество товара не равно 0
            list_of_supplies = [f"{i[0]}. {i[6]} поставка" for i in
                                conn.execute(f"SELECT * FROM Supply WHERE good_id = '{good_id[0]}' AND count_current != 0")]
            # список перемещений товара между складами, где на вторичном складе текущее количество товара не равно 0
            list_of_movements = [f"{i[0]}. {i[7]} перемещение" for i in
                                 conn.execute(f"SELECT * FROM MovementOfGoods WHERE goods_name = '{self.goods_combobox.currentText()}' "
                                              f"AND count_current > 0 "
                                              f"AND stock_out_id = '{stock_id}'")]
            # list_of_movements = [f"{i[0]}. {i[6]}" for i in
            #                      conn.execute(
            #                          f"SELECT * FROM MovementOfGoods")]

            print("supplies", list_of_supplies)
            print("movements", self.goods_combobox.currentText(), self.warehouse_combobox.currentText(), list_of_movements)
        # for num in range(0, len(list(list_of_supplies))):  # заполняем комбо виджет из списка поставок
        #     self.supply_number_combobox.setItemText(num, _translate("Dialog", f"{list_of_supplies[num]}"))
        if len(list_of_supplies + list_of_movements) != 0:
            self.supply_number_combobox.addItems(list_of_supplies+list_of_movements)
        else:
            self.supply_number_combobox.addItems(["поставок нет"])
        # raw = self.tableWidget.currentRow()
        # self.tableWidget.selectRow(raw)
        print("0 номер поставки в комбобоксе:", self.supply_number_combobox.currentText())
        self.tableWidget.setItem(self.tableWidget.currentRow(), 4, QTableWidgetItem(self.supply_number_combobox.currentText()))
        # self.tableWidget.setItem(self.tableWidget.currentRow(), 2, QTableWidgetItem(self.goods_combobox.currentText()))
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)

    def update_warehouse_from_combobox(self, index):
        _translate = QtCore.QCoreApplication.translate
        # self.tableWidget.selectRow(raw)
        self.tableWidget.setItem(self.tableWidget.currentRow(), 0,
                                 QTableWidgetItem(self.warehouse_combobox.currentText()))
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)


    def update_warehouse_out_from_combobox(self, index):
        _translate = QtCore.QCoreApplication.translate
        # self.tableWidget.selectRow(raw)
        self.tableWidget.setItem(self.tableWidget.currentRow(), 5,
                                 QTableWidgetItem(self.warehouse_combobox_out.currentText()))
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)

    def update_count_from_spinbox(self, value):
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
        print("2 номер поставки в комбобоксе:", self.supply_number_combobox.currentText())


    def update_table_supply_number_from_combobox(self):
        print("3 номер поставки в комбобоксе:", self.supply_number_combobox.currentText())
        self.tableWidget.setItem(self.tableWidget.currentRow(), 4, QTableWidgetItem(self.supply_number_combobox.currentText()))
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)




    # def update_supply_number_from_combobox(self, index):
    #     _translate = QtCore.QCoreApplication.translate
    #     # self.tableWidget.selectRow(raw)
    #     self.tableWidget.setItem(self.tableWidget.currentRow(), 4, QTableWidgetItem(self.supply_number_combobox.currentText()))
    #     self.cancel_button_pushButton.setEnabled(True)
    #     self.accept_button_pushButton.setEnabled(True)

    def update_supply_date_from_dateTimeEdit(self, date):
        _translate = QtCore.QCoreApplication.translate
        # self.tableWidget.selectRow(raw)
        self.tableWidget.setItem(self.tableWidget.currentRow(), 6,
                                 QTableWidgetItem(self.supply_date_dateTimeEdit.text()))
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)

    def save_write_off(self):  # функция для сохранения изменений в базе данных
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
                movement_supply_id = int(row[4].split(".")[0])
                supply_or_movement = row[4].split(" ")[3]
                print("перемещение или поставка:", supply_or_movement)
                stock_in_id = [i[0] for i in conn.execute(f"SELECT * FROM Stock WHERE name = '{row[0]}'")][0]
                stock_out_id = [i[0] for i in conn.execute(f"SELECT * FROM Stock WHERE name = '{row[5]}'")][0]
                good_id = [i[0] for i in conn.execute(f"SELECT * FROM Goods WHERE name = '{row[2]}'")][0]
                # good_count = [i[8] for i in conn.execute(f"SELECT * FROM Goods WHERE name = '{row[2]}'")][0]
                print("1")
                count_in = int(row[3])
                count_current = int(row[3])
                movement_date = row[6]
                movement_status = 'в процессе перемещения'
                goods_name = row[2]
                price = [i[5] for i in conn.execute(f"SELECT * FROM Goods WHERE name = '{row[2]}'")][0]
                if len([i[0] for i in conn.execute(f"SELECT * FROM MovementOfGoods")]) != 0:
                    movement_id = [i[0] for i in conn.execute(f"SELECT * FROM MovementOfGoods")][-1]
                else:
                    movement_id = 0
                date_off = DT.datetime.now()
                print(date_off)
                year = str(date_off)[:4]
                month = str(date_off)[5:7]
                day = str(date_off)[8:10]
                calendar_dict = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая',
                                 '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября',
                                 '11': 'ноября', '12': 'декабря'}
                document = f'act_{str(date_off)[:19].replace(":", "_").replace(" ", "_")}.docx'
                document_list.append(document)
                print("2")

                with conn:
                    if supply_or_movement == "поставка":
                        conn.execute(
                            "INSERT OR IGNORE INTO MovementOfGoods (supply_id, stock_in_id, stock_out_id, count_in, "
                            "count_current, movement_date, movement_status, document, goods_name) values(?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (movement_supply_id, stock_in_id, stock_out_id, count_in, count_current, movement_date, movement_status, document, goods_name))
                    if supply_or_movement == "перемещение":
                        conn.execute(
                            "INSERT OR IGNORE INTO MovementOfGoods (movement_id, stock_in_id, stock_out_id, count_in, "
                            "count_current, movement_date, movement_status, document, goods_name) values(?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (movement_supply_id, stock_in_id, stock_out_id, count_in, count_current, movement_date, movement_status, document, goods_name))
                conn.commit()
                # """Открываем шаблон документа и заполняем теги"""
                doc_in = docxtpl.DocxTemplate('movementdocs/template_movement.docx')
                context = {"stock_in": row[0],
                           'stock_out': row[5],
                           'supply_date': row[4],
                           'good_name': row[2],
                           'count': int(row[3]),
                           'price': price,
                           'total_price': price * count_in,
                           'year': year,
                           'month': calendar_dict[month],
                           'day': day,
                           'act_number': (movement_id + 1),
                           "position": "Директор",
                           'director': "К.Каліноўскі"}
                doc_in.render(context)
                doc_in.save(f"movementdocs//{document}")
                time.sleep(2)
        except Exception as e:
            print("аааа", e)
        self.cancel_button_pushButton.setEnabled(False)
        self.accept_button_pushButton.setEnabled(False)
        self.load_doc_pushButton.setEnabled(True)

    def load_movement_act(self):
        print(document_list)
        for doc in document_list:
            doc_to_open = "C://Users//voyag//PycharmProjects//Project_qt5//movementdocs//" + doc
            os.startfile(doc_to_open)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

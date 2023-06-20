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
        Dialog.resize(799, 575)
        Dialog.setStyleSheet("background-image: url(OJ91CN0.jpg);")
        conn = sqlite3.connect('warehouse.db')
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 30, 400, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #fff; font: bold 20pt MS Shell Dlg 2; background: transparent")
        self.label.setObjectName("label")
        self.category_combobox = QtWidgets.QComboBox(Dialog)
        self.category_combobox.setGeometry(QtCore.QRect(121, 115, 200, 37))
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
        self.goods_combobox.setGeometry(QtCore.QRect(121, 191, 230, 37))
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
        self.label_2.setGeometry(QtCore.QRect(121, 161, 144, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #fff; font: bold 11pt MS Shell Dlg 2; background: transparent")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(365, 161, 118, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #fff; font: bold 11pt MS Shell Dlg 2; background: transparent")
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(365, 191, 125, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(1000000)
        self.spinBox.setStyleSheet("font: bold 10pt \"OCR A Extended\";\n"
                                   "border-radius: 12px;\n"
                                   "border: 5px solid #42abc3;\n"
                                   "color: #42abc3;\n"
                                   "background:#cddff3")
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(510, 161, 147, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #fff; font: bold 11pt MS Shell Dlg 2; background: transparent")
        self.label_4.setObjectName("label_4")
        self.warehouse_combobox = QtWidgets.QComboBox(Dialog)
        self.warehouse_combobox.setGeometry(QtCore.QRect(510, 191, 220, 37))
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
        self.label_5.setGeometry(QtCore.QRect(121, 271, 144, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #fff; font: bold 11pt MS Shell Dlg 2; background: transparent")
        self.label_5.setObjectName("label_5")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(510, 310, 220, 37))
        current_date = QtCore.QDate.currentDate()
        current_time = QtCore.QTime.currentTime()
        self.dateTimeEdit_2.setDate(current_date)
        self.dateTimeEdit_2.setTime(current_time)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dateTimeEdit_2.setFont(font)
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setStyleSheet("font: bold 10pt \"OCR A Extended\";\n"
                                          "border-radius: 12px;\n"
                                          "border: 5px solid #42abc3;\n"
                                          "color: #42abc3;\n"
                                          "background:#cddff3")
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(510, 270, 143, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #fff; font: bold 11pt MS Shell Dlg 2; background: transparent")
        self.label_6.setObjectName("label_6")

        self.label_category = QtWidgets.QLabel(Dialog)
        self.label_category.setGeometry(QtCore.QRect(121, 91, 144, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_category.setFont(font)
        self.label_category.setStyleSheet("color: #fff; font: bold 11pt MS Shell Dlg 2; background: transparent")
        self.label_category.setObjectName("label_category")

        self.dateTimeEdit_3 = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit_3.setGeometry(QtCore.QRect(121, 310, 230, 37))
        current_date = QtCore.QDate.currentDate()
        current_time = QtCore.QTime.currentTime()
        self.dateTimeEdit_3.setDate(current_date)
        self.dateTimeEdit_3.setTime(current_time)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dateTimeEdit_3.setFont(font)
        self.dateTimeEdit_3.setCalendarPopup(True)
        self.dateTimeEdit_3.setStyleSheet("font: bold 11pt \"OCR A Extended\";\n"
                                          "border-radius: 12px;\n"
                                          "border: 5px solid #42abc3;\n"
                                          "color: #42abc3;\n"
                                          "background:#cddff3")
        self.dateTimeEdit_3.setObjectName("dateTimeEdit_3")
        self.accept_button_pushButton = QtWidgets.QPushButton(Dialog)
        self.accept_button_pushButton.setEnabled(False)
        self.accept_button_pushButton.setGeometry(QtCore.QRect(121, 461, 100, 42))
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

        self.cancel_button_pushButton.setGeometry(QtCore.QRect(246, 461, 100, 42))
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
        self.load_doc_pushButton.setGeometry(QtCore.QRect(510, 461, 220, 42))
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
        self.dateTimeEdit_2.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd HH:mm"))
        self.label_6.setText(_translate("Dialog", "Срок годности:"))
        self.label_category.setText(_translate("Dialog", "Категория:"))
        self.dateTimeEdit_3.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd HH:mm"))
        self.accept_button_pushButton.setText(_translate("Dialog", "Принять"))
        self.cancel_button_pushButton.setText(_translate("Dialog", "Отменить"))
        self.load_doc_pushButton.setText(_translate("Dialog", "Загрузить документ"))
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
        self.category_combobox.currentIndexChanged.connect(partial(self.update_goods_combobox))
        self.accept_button_pushButton.clicked.connect(partial(self.save_write_off))
        self.cancel_button_pushButton.clicked.connect(Dialog.close)
        # self.load_doc_pushButton.clicked.connect(partial(self.load_write_off_act))


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
        self.cancel_button_pushButton.setEnabled(True)
        self.accept_button_pushButton.setEnabled(True)


    def save_write_off(self):  # функция для сохранения изменений в базе данных
        conn = sqlite3.connect('warehouse.db')
        print("Дата и время поставки", self.dateTimeEdit_2.text())
        print("Срок годности до", self.dateTimeEdit_3.text())
        print("Склад", self.warehouse_combobox.currentText())
        print("Товар", self.goods_combobox.currentText())
        print("Количество", self.spinBox.text())

        # try:
        #     global document_list
        #     document_list = []
        #     for row in data:  # вставляем данные из списка в базу данных
        #         category_id = [i[0] for i in conn.execute(f"SELECT * FROM Category WHERE name = '{row[1]}'")][0]
        #         stock_id = [i[0] for i in conn.execute(f"SELECT * FROM Stock WHERE name = '{row[0]}'")][0]
        #         good_id = [i[0] for i in conn.execute(f"SELECT * FROM Goods WHERE name = '{row[2]}'")][0]
        #         good_count = [i[8] for i in conn.execute(f"SELECT * FROM Goods WHERE name = '{row[2]}'")][0]
        #         count = int(row[3])
        #         reason = row[4]
        #         price = [i[5] for i in conn.execute(f"SELECT * FROM Goods WHERE name = '{row[2]}'")][0]
        #         write_off_id = [i[0] for i in conn.execute(f"SELECT * FROM WriteOff")][-1]
        #         date_off = DT.datetime.now()
        #         print(date_off)
        #         year = str(date_off)[:4]
        #         month = str(date_off)[5:7]
        #         day = str(date_off)[8:10]
        #         calendar_dict = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая',
        #                          '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября',
        #                          '11': 'ноября', '12': 'декабря'}
        #         document = f'act_{str(date_off)[:19].replace(":", "_").replace(" ", "_")}.docx'
        #         document_list.append(document)
        #         fin_count = good_count - count
        #         print(good_count, count, fin_count)
        #         with conn:
        #             conn.execute(
        #                 "INSERT OR IGNORE INTO WriteOff (category_id, stock_id, good_id, count, reason, document, date_off) values(?, ?, ?, ?, ?, ?, ?)",
        #                 (category_id, stock_id, good_id, count, reason, document, date_off))
        #             conn.execute(f"UPDATE Goods SET count = ? WHERE id = ?", (fin_count, good_id))
        #         conn.commit()
        #
        #         doc_in = docxtpl.DocxTemplate('wroffdocs/template_write_off.docx')
        #
        #         # Создаем объект таблицы с тремя строками и двумя столбцами
        #         # table = docxtpl.Table([["A1", "B1"], ["A2", "B2"], ["A3", "B3"]], style="Table Grid")
        #
        #         context = {"name": row[2],
        #                    'stock': row[0],
        #                    'reason': row[4],
        #                    'count': int(row[3]),
        #                    'price': price,
        #                    'total_price': price * count,
        #                    'year': year,
        #                    'month': calendar_dict[month],
        #                    'day': day,
        #                    'act_number': (write_off_id + 1),
        #                    "position": "Директор",
        #                    'director': "К.Каліноўскі"}
        #         doc_in.render(context)
        #         doc_in.save(f"wroffdocs//{document}")
        #         time.sleep(2)
        #         # ddoc = "C://Users//voyag//PycharmProjects//Project_qt5//wroffdocs//" + document
        #         # os.startfile(ddoc)
        # except Exception as e:
        #     print(e)
        # self.cancel_button_pushButton.setEnabled(False)
        # self.accept_button_pushButton.setEnabled(False)
        # self.load_doc_pushButton.setEnabled(True)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
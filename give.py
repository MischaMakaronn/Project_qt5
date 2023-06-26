from PyQt5 import QtCore, QtGui, QtWidgets
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton, QLabel
from PyQt5.QtCore import Qt
import sqlite3
from functools import partial


class Ui_Dialog(object):
    def __init__(self):
        # Создаем список для хранения чекбоксов
        self.checkboxes = []

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 600)
        Dialog.setStyleSheet("background-image: url(\"OJ91CN0.jpg\");")
        conn = sqlite3.connect('warehouse.db')
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 30, 450, 45))
        self.label.setStyleSheet("color: #fff; font: 75 16pt MS Shell Dlg 2;")
        self.label.setObjectName("label")

        # Создаем метку для отображения сообщения
        self.message_label = QtWidgets.QLabel(Dialog)
        # self.message_label.move(460, 500)
        self.message_label.setGeometry(QtCore.QRect(620, 100, 300, 40))
        self.message_label.setStyleSheet("color: green; font: bold 12pt MS Shell Dlg 2; background: transparent")
        self.message_label.setObjectName("message_label")

        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(40, 100, 550, 370))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 468, 204))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM MovementOfGoods WHERE movement_status = 'в процессе перемещения'")
            info_movement_status = cursor.fetchall()
            print(len(list(info_movement_status)), (list(info_movement_status)))
            for movement in list(info_movement_status):
                # Создаем чекбокс с именем товара
                product_name = movement[10]
                movement_id = movement[0]
                stock_in_id = movement[3]
                stock_in_name = [i[1] for i in conn.execute(f"SELECT * FROM Stock WHERE id = '{stock_in_id}'")][0]
                stock_out_id = movement[4]
                stock_out_name = [i[1] for i in conn.execute(f"SELECT * FROM Stock WHERE id = '{stock_out_id}'")][0]
                count_in = movement[5]
                movement_date = movement[7]
                first_supply = movement[1]
                movement_supply = movement[2]
                print("поставка?", first_supply)
                print("перемещение?", movement_supply)
                if first_supply == None:
                    supply_text = "Вторичное"
                    movement_id_to_change = movement_supply
                else:
                    supply_text = "Первичное"
                    movement_id_to_change = first_supply


                result = f"{movement_id}:{stock_in_id}:{stock_out_id}:{count_in}:{movement_date}:{product_name}:{supply_text}:{movement_id_to_change}"
                checkbox = QCheckBox(result, self.scrollAreaWidgetContents)
                checkbox.setObjectName(f"checkBox_{movement}")
                # Устанавливаем текст чекбокса с информацией о перемещении
                checkbox.setText(f"{movement_id}.\n"
                                 f"Со склада: {stock_in_name},"
                                 f"На склад: {stock_out_name},\n "
                                 f"Товар: {product_name}, "
                                 f"Количество: {count_in},\n "
                                 f"Дата: {movement_date},\n"
                                 f"Вид перемещения: {supply_text}")
                checkbox.setStyleSheet("color: black; font: bold 10pt MS Shell Dlg 2; background: transparent")
                # Подключаем сигнал stateChanged к функции update_status с аргументом product_name
                checkbox.stateChanged.connect(partial(self.update_status, result))
                # Добавляем чекбокс в список и в макет
                self.checkboxes.append(checkbox)
                self.verticalLayout.addWidget(checkbox)
            # Устанавливаем макет на виджет scrollAreaWidgetContents
            self.scrollAreaWidgetContents.setLayout(self.verticalLayout)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.accept_button_pushButton = QtWidgets.QPushButton(Dialog)
            self.accept_button_pushButton.setGeometry(QtCore.QRect(50, 500, 120, 42))
            self.accept_button_pushButton.setStyleSheet("font: bold 11pt \"Arial Black\";\n"
                                                        "border-radius: 12px;\n"
                                                        "border: 2px solid #42abc3;\n"
                                                        "color: #42abc3;\n"
                                                        "background:#cddff3")
            self.accept_button_pushButton.setObjectName("pushButton_3")
            self.cancel_button_pushButton = QtWidgets.QPushButton(Dialog)
            self.cancel_button_pushButton.setGeometry(QtCore.QRect(180, 500, 120, 42))
            self.cancel_button_pushButton.setStyleSheet("font: bold 11pt \"Arial Black\";\n"
                                                        "border-radius: 12px;\n"
                                                        "border: 2px solid #42abc3;\n"
                                                        "color: #42abc3;\n"
                                                        "background:#cddff3")
            self.cancel_button_pushButton.setObjectName("pushButton_5")
            self.retranslateUi(Dialog)
            QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Выбрать и принять перемещение"))
        # self.message_label.setText(_translate("Dialog", "Изменения сохранены"))
        self.accept_button_pushButton.setText(_translate("Dialog", "Применить"))
        self.cancel_button_pushButton.setText(_translate("Dialog", "Отменить"))
        self.cancel_button_pushButton.clicked.connect(Dialog.close)
        self.accept_button_pushButton.clicked.connect(partial(self.save_changes))

    def update_status(self, result, state):
        conn = sqlite3.connect('warehouse.db')
        print(result, state)  # Выводим данные конкретного чекбокса и состояние чекбокса
        movement_id = int(result.split(":")[0])  # айди перемещения в таблице MovementOfGoods
        movement_id_to_change = int(result.split(":")[8])  # айди поставки или перемещения, где надо изменять колиечество товара
        if state == 2:
            movement_status = "завершено"
            with conn:
                conn.execute(f"UPDATE MovementOfGoods SET movement_status = ? WHERE id = ?",
                             (movement_status, movement_id))
                if result.split(":")[7] == "Первичное":
                    count = [i[5] for i in conn.execute(f"SELECT * FROM Supply WHERE id = {movement_id_to_change}")][0]
                    count_current = count - int(result.split(":")[3])
                    conn.execute(f"UPDATE Supply SET count_current = ? WHERE id = ?", (count_current, movement_id_to_change))
                if result.split(":")[7] == "Вторичное":
                    count = [i[6] for i in conn.execute(f"SELECT * FROM MovementOfGoods WHERE id = '{movement_id_to_change}'")][0]
                    count_current = count - int(result.split(":")[3])
                    conn.execute(f"UPDATE MovementOfGoods SET count_current = ? WHERE id = ?",
                                 (count_current, movement_id_to_change))
        if state == 0:
            movement_status = "в процессе перемещения"
            with conn:
                conn.execute(f"UPDATE MovementOfGoods SET movement_status = ? WHERE id = ?", (movement_status, movement_id))
                if result.split(":")[7] == "Первичное":
                    count = [i[5] for i in conn.execute(f"SELECT * FROM Supply WHERE id = '{movement_id_to_change}'")][0]
                    count_current = count + int(result.split(":")[3])
                    conn.execute(f"UPDATE Supply SET count_current = ? WHERE id = ?", (count_current, movement_id_to_change))
                if result.split(":")[7] == "Вторичное":
                    count = [i[6] for i in conn.execute(f"SELECT * FROM MovementOfGoods WHERE id = '{movement_id_to_change}'")][0]
                    count_current = count + int(result.split(":")[3])
                    conn.execute(f"UPDATE MovementOfGoods SET count_current = ? WHERE id = ?", (count_current, movement_id_to_change))
        # conn.commit()

    def save_changes(self):
        # Сохраняем изменения в базе данных и показываем сообщение
        conn = sqlite3.connect('warehouse.db')
        conn.commit()
        self.message_label.setText("Изменения сохранены")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

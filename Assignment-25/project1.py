import sys
import threading
import time
import sqlite3

from PySide6.QtWidgets import *
from alarm_ui import Ui_MainWindow
from functools import partial


class MyUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.read_from_db()
        self.cach = ""
        self.ui.chk_active_1.clicked.connect(
            partial(
                self.update_active,
                self.ui.chk_active_1,
                "1",
                self.ui.alarm_text_1,
                self.ui.alarm_time_1,
            )
        )
        self.ui.chk_active_2.clicked.connect(
            partial(
                self.update_active,
                self.ui.chk_active_2,
                "2",
                self.ui.alarm_text_2,
                self.ui.alarm_time_2,
            )
        )
        self.ui.chk_active_3.clicked.connect(
            partial(
                self.update_active,
                self.ui.chk_active_3,
                "3",
                self.ui.alarm_text_3,
                self.ui.alarm_time_3,
            )
        )

        self.ui.btn_edit_1.clicked.connect(partial(self.call_time, "1"))
        self.ui.btn_edit_2.clicked.connect(partial(self.call_time, "2"))
        self.ui.btn_edit_3.clicked.connect(partial(self.call_time, "3"))
        self.ui.btn_edit_alarm.clicked.connect(self.edit_alarm)

    def read_from_db(self):
        self.con = sqlite3.connect("alarm.db")
        self.cursor = self.con.cursor()
        query = "SELECT * FROM alarm WHERE 1"
        result = self.cursor.execute(query)
        alarm_data = result.fetchall()
        self.ui.alarm_text_1.setText(alarm_data[0][1])
        self.ui.alarm_time_1.setText(
            str(alarm_data[0][2]) + ":" + str(alarm_data[0][3])
        )
        self.ui.alarm_text_2.setText(alarm_data[1][1])
        self.ui.alarm_time_2.setText(
            str(alarm_data[1][2]) + ":" + str(alarm_data[1][3])
        )
        self.ui.alarm_text_3.setText(alarm_data[2][1])
        self.ui.alarm_time_3.setText(
            str(alarm_data[2][2]) + ":" + str(alarm_data[2][3])
        )

        if alarm_data[0][4] == "1":
            self.ui.chk_active_1.setChecked(True)
            self.ui.chk_active_1.setText("فعال")
            self.ui.alarm_text_1.setStyleSheet("color:blue")
            self.ui.alarm_time_1.setStyleSheet("color:blue")
        else:
            self.ui.chk_active_1.setChecked(False)
            self.ui.chk_active_1.setText("غیر فعال")
            self.ui.alarm_text_1.setStyleSheet("color:black")
            self.ui.alarm_time_1.setStyleSheet("color:black")

        if alarm_data[1][4] == "1":
            self.ui.chk_active_2.setChecked(True)
            self.ui.chk_active_2.setText("فعال")
            self.ui.alarm_text_2.setStyleSheet("color:blue")
            self.ui.alarm_time_2.setStyleSheet("color:blue")
        else:
            self.ui.chk_active_2.setChecked(False)
            self.ui.chk_active_2.setText("غیر فعال")
            self.ui.alarm_text_2.setStyleSheet("color:black")
            self.ui.alarm_time_2.setStyleSheet("color:black")

        if alarm_data[2][4] == "1":
            self.ui.chk_active_3.setChecked(True)
            self.ui.chk_active_3.setText("فعال")
            self.ui.alarm_text_3.setStyleSheet("color:blue")
            self.ui.alarm_time_3.setStyleSheet("color:blue")
        else:
            self.ui.chk_active_3.setChecked(False)
            self.ui.chk_active_3.setText("غیر فعال")
            self.ui.alarm_text_3.setStyleSheet("color:black")
            self.ui.alarm_time_3.setStyleSheet("color:black")

    def update_active(self, btn, id, alarm_text, alarm_time):
        pos = btn.isChecked()
        if pos == True:
            active = "1"
            btn.setText("فعال")
            alarm_text.setStyleSheet("color:blue")
            alarm_time.setStyleSheet("color:blue")
        else:
            active = "0"
            btn.setText("غیر فعال")
            alarm_text.setStyleSheet("color:black")
            alarm_time.setStyleSheet("color:black")

        query = "UPDATE `alarm` SET `active` = " + active + " WHERE `id` = " + id
        self.cursor.execute(query)
        self.con.commit()

    def call_time(self, id):
        query = "SELECT * FROM `alarm` WHERE `id` = " + id
        result = self.cursor.execute(query)
        data = result.fetchall()
        message = data[0][1]
        hour = data[0][2]
        minute = data[0][3]
        self.ui.alarm_name.setText(message)
        self.ui.alarm_hour_set.setValue(int(hour))
        self.ui.alarm_minute_set.setValue(int(minute))
        self.ui.alarm_name.setEnabled(True)
        self.ui.alarm_hour_set.setEnabled(True)
        self.ui.alarm_minute_set.setEnabled(True)
        self.ui.btn_edit_alarm.setEnabled(True)
        self.cach = id
        self.ui.edit_widget.show()

    def edit_alarm(self):
        id = self.cach
        message = self.ui.alarm_name.text()
        hour = self.ui.alarm_hour_set.text()
        minute = self.ui.alarm_minute_set.text()
        query = (
            "UPDATE `alarm` SET `message` = '"
            + message
            + "',`hour`="
            + hour
            + ",minute="
            + minute
            + " WHERE `id` = "
            + id
        )
        self.cursor.execute(query)
        self.con.commit()
        msgtext = "هشدار با موفقیت ویرایش شد"
        msg = QMessageBox(text=msgtext)
        msg.show()
        msg.exec()
        self.ui.edit_widget.hide()
        self.read_from_db()
        


class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(10):
            print(self.name)
            time.sleep(0.5)


app = QApplication(sys.argv)
window = MyUI()
window.show()
app.exec()

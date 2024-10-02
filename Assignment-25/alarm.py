import sqlite3
from functools import partial
from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import QMessageBox
from alarm_class import AlarmClass
import time


class Alarm(QThread):
    signal_alarm = Signal(str, str, bool)

    def __init__(self, window):
        super().__init__()
        self.init_settings(window)
        # self.timer1 = AlarmClass(t1_h, t1_m)
        self.timer2 = AlarmClass(self.t2_h, self.t2_m, "timer2")
        # self.timer3 = AlarmClass(t3_h, t3_m)
        self.t1_h = "0"
        self.t1_m = "0"
        self.t2_h = "0"
        self.t2_m = "0"
        self.t1_active = ""
        self.t2_active = ""
        self.t3_h = "0"
        self.t3_m = "0"
        self.t3_active = ""
        self.check_value1 = ""
        self.check_value2 = ""
        self.check_value3 = ""

    def init_settings(self, win):
        self.read_from_db(win)
        global cach
        win.chk_active_1.clicked.connect(
            partial(
                self.update_active,
                win.chk_active_1,
                "1",
                win.alarm_text_1,
                win.alarm_time_1,
            )
        )
        win.chk_active_2.clicked.connect(
            partial(
                self.update_active,
                win.chk_active_2,
                "2",
                win.alarm_text_2,
                win.alarm_time_2,
            )
        )
        win.chk_active_3.clicked.connect(
            partial(
                self.update_active,
                win.chk_active_3,
                "3",
                win.alarm_text_3,
                win.alarm_time_3,
            )
        )

        win.btn_edit_1.clicked.connect(partial(self.call_time, win, "1"))
        win.btn_edit_2.clicked.connect(partial(self.call_time, win, "2"))
        win.btn_edit_3.clicked.connect(partial(self.call_time, win, "3"))
        win.btn_edit_alarm.clicked.connect(partial(self.edit_alarm, win))
        win.alarm_name.setEnabled(False)
        win.alarm_hour_set.setEnabled(False)
        win.alarm_minute_set.setEnabled(False)
        win.btn_edit_alarm.setEnabled(False)

    def read_from_db(self, win):

        self.con = sqlite3.connect("alarm.db")
        self.cursor = self.con.cursor()
        query = "SELECT * FROM alarm WHERE 1"
        result = self.cursor.execute(query)
        alarm_data = result.fetchall()
        win.alarm_text_1.setText(alarm_data[0][1])
        win.alarm_time_1.setText(str(alarm_data[0][2]) + ":" + str(alarm_data[0][3]))
        win.alarm_text_2.setText(alarm_data[1][1])
        win.alarm_time_2.setText(str(alarm_data[1][2]) + ":" + str(alarm_data[1][3]))
        win.alarm_text_3.setText(alarm_data[2][1])
        win.alarm_time_3.setText(str(alarm_data[2][2]) + ":" + str(alarm_data[2][3]))

        if alarm_data[0][4] == "1":
            win.chk_active_1.setChecked(True)
            win.chk_active_1.setText("فعال")
            win.alarm_text_1.setStyleSheet("color:blue")
            win.alarm_time_1.setStyleSheet("color:blue")
            self.t1_h = alarm_data[0][2]
            self.t1_m = alarm_data[0][3]
            self.check_value1 = "True"
        else:
            win.chk_active_1.setChecked(False)
            win.chk_active_1.setText("غیر فعال")
            win.alarm_text_1.setStyleSheet("color:black")
            win.alarm_time_1.setStyleSheet("color:black")
            self.t1_h = ""
            self.t1_m = ""
            self.check_value1 = "False"

        if alarm_data[1][4] == "1":
            win.chk_active_2.setChecked(True)
            win.chk_active_2.setText("فعال")
            win.alarm_text_2.setStyleSheet("color:blue")
            win.alarm_time_2.setStyleSheet("color:blue")
            self.t2_h = alarm_data[1][2]
            self.t2_m = alarm_data[1][3]
            self.check_value2 = "True"
        else:
            win.chk_active_2.setChecked(False)
            win.chk_active_2.setText("غیر فعال")
            win.alarm_text_2.setStyleSheet("color:black")
            win.alarm_time_2.setStyleSheet("color:black")
            self.t2_h = ""
            self.t2_m = ""
            self.check_value2 = "False"

        if alarm_data[2][4] == "1":
            win.chk_active_3.setChecked(True)
            win.chk_active_3.setText("فعال")
            win.alarm_text_3.setStyleSheet("color:blue")
            win.alarm_time_3.setStyleSheet("color:blue")
            self.t3_h = alarm_data[2][2]
            self.t3_m = alarm_data[2][3]
            self.check_value3 = "True"
        else:
            win.chk_active_3.setChecked(False)
            win.chk_active_3.setText("غیر فعال")
            win.alarm_text_3.setStyleSheet("color:black")
            win.alarm_time_3.setStyleSheet("color:black")
            self.t3_h = ""
            self.t3_m = ""
            self.check_value3 = "False"

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
        
        match id:
            case 1:
                if active == "1":
                    self.check_value1 = "True"
                    self.run()
                else:
                    self.check_value1 = "False"
            case 2:
                if active == "1":
                    self.check_value2 = "True"
                    self.run()
                else:
                    self.check_value2 = "False"
            case 3:
                if active == "1":
                    self.check_value3 = "True"
                    self.run()
                else:
                    self.check_value3 = "False"
                
            

    def call_time(self, win, id):
        global cach
        cach = id
        query = "SELECT * FROM `alarm` WHERE `id` = " + id
        result = self.cursor.execute(query)
        data = result.fetchall()
        message = data[0][1]
        hour = data[0][2]
        minute = data[0][3]
        win.alarm_name.setText(message)
        win.alarm_hour_set.setValue(int(hour))
        win.alarm_minute_set.setValue(int(minute))
        win.alarm_name.setEnabled(True)
        win.alarm_hour_set.setEnabled(True)
        win.alarm_minute_set.setEnabled(True)
        win.btn_edit_alarm.setEnabled(True)
        win.edit_widget.show()

    def edit_alarm(self, win):
        global cach
        id = cach
        message = win.alarm_name.text()
        hour = win.alarm_hour_set.text()
        minute = win.alarm_minute_set.text()

        if int(hour) < 10:
            hours = "0" + hour
        else:
            hours = hour

        if int(minute) < 10:
            minutes = "0" + minute
        else:
            minutes = minute

        query = (
            "UPDATE `alarm` SET `message` = '"
            + message
            + "',`hour`='"
            + hours
            + "',minute='"
            + minutes
            + "' WHERE `id` = "
            + id
        )
        self.cursor.execute(query)
        self.con.commit()
        msgtext = "هشدار با موفقیت ویرایش شد"
        msg = QMessageBox(text=msgtext)
        msg.show()
        msg.exec()
        win.alarm_name.setEnabled(False)
        win.alarm_hour_set.setEnabled(False)
        win.alarm_minute_set.setEnabled(False)
        win.btn_edit_alarm.setEnabled(False)
        self.read_from_db(win)

    def run(self):
        while True:
            if self.check_value2 == "False":
                break
            else:
                self.check_value2 = self.timer2.check_alarm()
                self.signal_alarm.emit(self.t2_h, self.t2_m, self.check_value2)
            time.sleep(1)

    def stop(self):
        self.check_value2 = "False"

        # while True:
        #     if len(t3_h) > 0 and len(t3_m) > 0 and t3_active == "ok":
        #         check_value3 = self.timer3.check_alarm()
        #         time.sleep(1)
        #         if check_value3 == False:
        #             break
        #     else:
        #         break

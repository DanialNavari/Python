# System library
import sys

# Qt library
from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import *
import arcade
from functools import partial
import sqlite3

# Program file
from Ui import *
from stopwatch import *
from timer import *
from global_time import GlobalTime
from alarm import alarm

# Make app
app = QApplication(sys.argv)

# Instance of UI
window = UI()
window.show()

# cach
cach = ""


########################## Start of STOPWATCH ##########################
# Show number of stopwatch
def show_timer_stopwatch(time):
    window.ui.lbl_stopwatch.setText(f"{time.hour}:{time.minute}:{time.second}")


# Reset stopwatch thread
def reset_stopwatch():
    thread_stopwatch.reset()
    window.ui.lbl_stopwatch.setText("0:0:0")


# Start the thread of stopwatch
def start_stopwatch():
    thread_stopwatch.start()


# Stop the thread of stopwatch
def stop_stopwatch():
    thread_stopwatch.terminate()


# Related to stopwatch
thread_stopwatch = StopWatchThread()
thread_stopwatch.signal_show_stopwatch.connect(show_timer_stopwatch)
window.ui.btn_start_stopwatch.clicked.connect(start_stopwatch)
window.ui.btn_stop_stopwatch.clicked.connect(stop_stopwatch)
window.ui.btn_reset_stopwatch.clicked.connect(reset_stopwatch)
########################## End of STOPWATCH ##########################


########################## Start of timer ##########################
# default input value
tb_hour = 0
tb_minute = 15
tb_second = 30


# Show number of timer
def show_timer_timer(times, pos):
    window.ui.tb_hour_timer.setText(f"{times.hour}")
    window.ui.tb_minute_timer.setText(f"{times.minute}")
    window.ui.tb_second_timer.setText(f"{times.second}")
    if pos == False:
        gameover_sound = arcade.load_sound("sound/alarm.wav", False)
        music = arcade.play_sound(sound=gameover_sound, volume=1, pan=0, looping=True)

        msgbox = QMessageBox()
        msgbox.setText("زمان به پایان رسید")
        ret = msgbox.exec()
        if ret == 1024:
            arcade.stop_sound(music)
        stop_timer()


# Start the thread of timer
def start_timer():
    global tb_hour, tb_minute, tb_second
    tb_hour = int(window.ui.tb_hour_timer.text())
    tb_minute = int(window.ui.tb_minute_timer.text())
    tb_second = int(window.ui.tb_second_timer.text())
    window.ui.tb_hour_timer.setReadOnly(True)
    window.ui.tb_minute_timer.setReadOnly(True)
    window.ui.tb_second_timer.setReadOnly(True)
    thread_timer.reset(tb_hour, tb_minute, tb_second)
    thread_timer.start()


# Stop the thread of timer
def stop_timer():
    thread_timer.terminate()
    window.ui.tb_hour_timer.setReadOnly(False)
    window.ui.tb_minute_timer.setReadOnly(False)
    window.ui.tb_second_timer.setReadOnly(False)


# Reset the thread of timer
def reset_timer():
    thread_timer.reset(tb_hour, tb_minute, tb_second)
    window.ui.tb_hour_timer.setText(str(tb_hour))
    window.ui.tb_minute_timer.setText(str(tb_minute))
    window.ui.tb_second_timer.setText(str(tb_second))


thread_timer = TimerThread()
thread_timer.signal_show_timer.connect(show_timer_timer)
window.ui.btn_start_timer.clicked.connect(start_timer)
window.ui.btn_stop_timer.clicked.connect(stop_timer)
window.ui.btn_reset_timer.clicked.connect(reset_timer)

########################## End of timer ##########################


##########################  Start of Global Time ##########################
def show_global_time(ir_time, us_time, de_time, ir_zone, us_zone, de_zone):
    window.ui.ir_time.setText(ir_time)
    window.ui.us_time.setText(us_time)
    window.ui.de_time.setText(de_time)
    window.ui.ir_timezone.setText(ir_zone)
    window.ui.us_timezone.setText(us_zone)
    window.ui.de_timezone.setText(de_zone)


global_country_time = GlobalTime()
global_country_time.signal_show_country.connect(show_global_time)
global_country_time.start()


##########################  End of Global Time ##########################

##########################  Start of Alarm ##########################


def init_settings(win):
    read_from_db(win)
    global cach
    win.chk_active_1.clicked.connect(
        partial(
            update_active,
            win.chk_active_1,
            "1",
            win.alarm_text_1,
            win.alarm_time_1,
        )
    )
    win.chk_active_2.clicked.connect(
        partial(
            update_active,
            win.chk_active_2,
            "2",
            win.alarm_text_2,
            win.alarm_time_2,
        )
    )
    win.chk_active_3.clicked.connect(
        partial(
            update_active,
            win.chk_active_3,
            "3",
            win.alarm_text_3,
            win.alarm_time_3,
        )
    )

    win.btn_edit_1.clicked.connect(partial(call_time, win, "1"))
    win.btn_edit_2.clicked.connect(partial(call_time, win, "2"))
    win.btn_edit_3.clicked.connect(partial(call_time, win, "3"))
    win.btn_edit_alarm.clicked.connect(partial(edit_alarm, win))
    win.alarm_name.setEnabled(False)
    win.alarm_hour_set.setEnabled(False)
    win.alarm_minute_set.setEnabled(False)
    win.btn_edit_alarm.setEnabled(False)


def read_from_db(win):
    global con, cursor
    con = sqlite3.connect("alarm.db")
    cursor = con.cursor()
    query = "SELECT * FROM alarm WHERE 1"
    result = cursor.execute(query)
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
    else:
        win.chk_active_1.setChecked(False)
        win.chk_active_1.setText("غیر فعال")
        win.alarm_text_1.setStyleSheet("color:black")
        win.alarm_time_1.setStyleSheet("color:black")

    if alarm_data[1][4] == "1":
        win.chk_active_2.setChecked(True)
        win.chk_active_2.setText("فعال")
        win.alarm_text_2.setStyleSheet("color:blue")
        win.alarm_time_2.setStyleSheet("color:blue")
    else:
        win.chk_active_2.setChecked(False)
        win.chk_active_2.setText("غیر فعال")
        win.alarm_text_2.setStyleSheet("color:black")
        win.alarm_time_2.setStyleSheet("color:black")

    if alarm_data[2][4] == "1":
        win.chk_active_3.setChecked(True)
        win.chk_active_3.setText("فعال")
        win.alarm_text_3.setStyleSheet("color:blue")
        win.alarm_time_3.setStyleSheet("color:blue")
    else:
        win.chk_active_3.setChecked(False)
        win.chk_active_3.setText("غیر فعال")
        win.alarm_text_3.setStyleSheet("color:black")
        win.alarm_time_3.setStyleSheet("color:black")


def update_active(btn, id, alarm_text, alarm_time):
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
    cursor.execute(query)
    con.commit()


def call_time(win, id):
    global cach
    cach = id
    query = "SELECT * FROM `alarm` WHERE `id` = " + id
    result = cursor.execute(query)
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


def edit_alarm(win):
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
    cursor.execute(query)
    con.commit()
    msgtext = "هشدار با موفقیت ویرایش شد"
    msg = QMessageBox(text=msgtext)
    msg.show()
    msg.exec()
    win.alarm_name.setEnabled(False)
    win.alarm_hour_set.setEnabled(False)
    win.alarm_minute_set.setEnabled(False)
    win.btn_edit_alarm.setEnabled(False)
    read_from_db(win)


init_settings(window.ui)
read_from_db(window.ui) 

##########################  End of Alarm ##########################


# Application execute
app.exec()

# System library
import sys

# Qt library
from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import *

# Program file
from Ui import *
from stopwatch import *
from timer import *


# Make app
app = QApplication(sys.argv)

# Instance of UI
window = UI()
window.show()


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
def show_timer_timer(time):
    window.ui.tb_hour_timer.setText(f"{time.hour}")
    window.ui.tb_minute_timer.setText(f"{time.minute}")
    window.ui.tb_second_timer.setText(f"{time.second}")


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

# Application execute
app.exec()

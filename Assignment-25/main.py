import sys
import time
from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from main_window import Ui_MainWindow


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class MyThread(QThread):
    signal_dani = Signal(int)

    def __init__(self):
        super().__init__()
        self.second = 0

    def run(self):
        while True:
            self.second += 1
            self.signal_dani.emit(self.second)
            time.sleep(1)

    def reset(self):
        self.second = 0


def show_number(s):
    window.ui.lbl_stopwatch.setText(str(s))


def start_stopwatch():
    thread_stopwatch.start()


def stop_stopwatch():
    thread_stopwatch.terminate()


def reset_stopwatch():
    thread_stopwatch.reset()
    show_number(0)


app = QApplication(sys.argv)
window = UI()
window.show()
thread_stopwatch = MyThread()
thread_stopwatch.signal_dani.connect(show_number)
window.ui.btn_start_stopwatch.clicked.connect(start_stopwatch)
window.ui.btn_stop_stopwatch.clicked.connect(stop_stopwatch)
window.ui.btn_reset_stopwatch.clicked.connect(reset_stopwatch)
app.exec()

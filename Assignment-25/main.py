import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QThread
from main_window import Ui_MainWindow


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_start_stopwatch.clicked.connect(MyThread.start_stopwatch)


class MyThread(QThread):
    def __init__(self):
        super().__init__()
        self.second = 0

    def run(self):
        while True:
            self.second += 1
            print(self.second)
            time.sleep(1)

    def start_stopwatch(self):
        thread_stopwatch.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    thread_stopwatch = MyThread()
    app.exec()

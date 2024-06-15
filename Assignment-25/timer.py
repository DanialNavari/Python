import time
from PySide6.QtCore import QObject, QThread, Signal
from mytime import MyTime


class TimerThread(QThread):
    signal_show_timer = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 15, 30)

    def run(self):
        while True:
            self.time.minus()
            self.signal_show_timer.emit(self.time)
            time.sleep(1)

    def reset(self, hh, mm, ss):
        self.time.reset_timer(hh, mm, ss)

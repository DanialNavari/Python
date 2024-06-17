import time
from PySide6.QtCore import QObject, QThread, Signal
from mytime import MyTime


class TimerThread(QThread):
    signal_show_timer = Signal(MyTime, bool)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 15, 30)
        self.pos_loop = True

    def run(self):

        while True:
            self.pos_loop = self.time.minus()
            self.signal_show_timer.emit(self.time, self.pos_loop)
            time.sleep(1)
            if self.pos_loop == False:
                break

    def reset(self, hh, mm, ss):
        self.time.reset_timer(hh, mm, ss)

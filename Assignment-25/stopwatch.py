import time
from PySide6.QtCore import QObject, QThread, Signal
from mytime import MyTime


class StopWatchThread(QThread):
    signal_show_stopwatch = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 0, 0)

    def run(self):
        while True:
            self.time.plus()
            self.signal_show_stopwatch.emit(self.time)
            time.sleep(1)

    def reset(self):
        self.time.reset_stopwatch()



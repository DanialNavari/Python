from PySide6.QtCore import QObject, QThread, Signal

class Winalarm(QThread):
    signal_alarm = Signal(str)

    def __init__(self):
        super().__init__()

    def run():
        ...
import time
from PySide6.QtCore import QObject, QThread, Signal
import datetime
from pytz import *


class GlobalTime(QThread):
    signal_show_country = Signal(str, str, str)

    def __init__(self):
        super().__init__()
        self.local_time = datetime.datetime.now()
        self.fmt = "%H:%M:%S"
        self.zone = "%Z"
        self.ir = timezone("Asia/Tehran")
        self.us = timezone("US/Eastern")
        self.de = timezone("Europe/Berlin")
        self.ir_time = self.local_time.strftime(self.fmt)

    def run(self):
        while True:
            iran_time = self.ir_time
            us_time = self.country_time(self.us)
            de_time = self.country_time(self.de)
            self.signal_show_country.emit(iran_time, us_time, de_time)
            time.sleep(1)

    def country_time(self, country):
        country_time = (
            utc.localize(self.local_time).astimezone(country).strftime(self.fmt)
        )
        return country_time

    def country_zone(self, country):
        country_zone = (
            utc.localize(self.local_time).astimezone(country).strftime(self.zone)
        )
        return country_zone

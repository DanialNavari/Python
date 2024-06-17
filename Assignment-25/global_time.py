import time
from PySide6.QtCore import QObject, QThread, Signal
import datetime
from pytz import *


class GlobalTime(QThread):
    signal_show_country = Signal(str, str, str, str, str, str)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            self.local_time = datetime.datetime.now()
            self.fmt = "%H:%M:%S"
            self.zone = "%z"
            self.ir = timezone("Asia/Tehran")
            self.us = timezone("US/Eastern")
            self.de = timezone("Europe/Berlin")
            self.ir_time = self.local_time.strftime(self.fmt)
            iran_time = str(self.ir_time)
            us_time = str(self.country_time(self.us))
            de_time = str(self.country_time(self.de))

            iran_zone = str(self.country_zone(self.ir))
            us_zone = str(self.country_zone(self.us))
            de_zone = str(self.country_zone(self.de))
            self.signal_show_country.emit(
                iran_time, us_time, de_time, iran_zone, us_zone, de_zone
            )
            time.sleep(1)

    def country_time(self, country):
        return utc.localize(self.local_time).astimezone(country).strftime(self.fmt)

    def country_zone(self, country):
        return utc.localize(self.local_time).astimezone(country).strftime(self.zone)

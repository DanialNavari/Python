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
            self.local_time = datetime.datetime.now(datetime.timezone.utc)
            self.fmt = "%H:%M:%S"
            self.zone = "%z"
            self.ir = timezone("Asia/Tehran")
            self.us = timezone("US/Eastern")
            self.de = timezone("Europe/Berlin")
            iran_time = str(self.country_time(self.ir))  # str(self.ir_time)
            us_time = str(self.country_time(self.us))
            de_time = str(self.country_time(self.de))

            ir_time_h = str(int(str(self.country_time(self.ir))[:2]) + 1)
            ir_time_m = str(self.country_time(self.ir))[2:5]
            ir_time_s = str(self.country_time(self.ir))[5:]
            ir_times = ir_time_h + ir_time_m + ir_time_s
            
            de_time_h = str(int(str(self.country_time(self.de))[:2]) + 1)
            de_time_m = str(self.country_time(self.de))[2:5]
            de_time_s = str(self.country_time(self.de))[5:]
            de_times = de_time_h + de_time_m + de_time_s
            
            us_time_h = str(int(str(self.country_time(self.us))[:2]) + 1)
            us_time_m = str(self.country_time(self.us))[2:5]
            us_time_s = str(self.country_time(self.us))[5:]
            us_times = us_time_h + us_time_m + us_time_s

            iran_zone = (
                str(self.country_zone(self.ir))[0:3]
                + ":"
                + str(self.country_zone(self.ir))[3:]
            )
            us_zone = (
                str(self.country_zone(self.us))[0:3]
                + ":"
                + str(self.country_zone(self.us))[3:]
            )
            de_zone = (
                str(self.country_zone(self.de))[0:3]
                + ":"
                + str(self.country_zone(self.us))[3:]
            )
            self.signal_show_country.emit(
                ir_times, us_times, de_times, iran_zone, us_zone, de_zone
            )
            time.sleep(1)

    def country_time(self, country):
        return self.local_time.astimezone(country).strftime(self.fmt)

    def country_zone(self, country):
        return self.local_time.astimezone(country).strftime(self.zone)

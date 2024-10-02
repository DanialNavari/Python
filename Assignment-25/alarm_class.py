from datetime import datetime


class AlarmClass:
    def __init__(self, hour, minute, element):
        self.h = hour
        self.m = minute

    def check_alarm(self):
        current_time = datetime.now()
        saat = str(current_time.time())
        sep = saat.split(":")
        if self.h == sep[0] and self.m == sep[1]:
            print("False")
        

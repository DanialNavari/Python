class MyTime:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    # For Stopwatch section
    def plus(self):
        self.second += 1
        if self.second >= 60:
            self.minute += 1
            self.second = 0
        if self.minute >= 60:
            self.hour += 1
            self.minute = 0

    # For Timer section
    def minus(self):
        self.second -= 1
        if self.second <= 0:
            if self.minute > 0:
                self.minute -= 1
                self.second += 59
            elif self.hour > 0 and self.minute <= 0:
                self.hour -= 1
                self.minute = 59
                self.second = 59

    # For timer section
    def reset_timer(self, hh, mm, ss):
        self.hour = hh
        self.minute = mm
        self.second = ss

    # For stopwatch section
    def reset_stopwatch(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

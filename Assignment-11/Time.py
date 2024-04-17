class Time:
    def __init__(self, hh, mm, ss):
        self.s = ss
        self.m = mm
        self.h = hh
        self.fix()

    # sum two times
    def sum(self, time2):
        s_new = self.s + time2.s
        m_new = self.m + time2.m
        h_new = self.h + time2.h
        result = Time(h_new, m_new, s_new)
        self.fix()
        return result

    # sub two times
    def sub(self, time2):
        s_new = self.s - time2.s
        m_new = self.m - time2.m
        h_new = self.h - time2.h
        result = Time(h_new, m_new, s_new)
        self.fix()
        return result

    # convert seconds to time
    @staticmethod
    def convert_second_to_time(second):
        # for example : 4256 s
        hour = second // 3600
        second = second - (hour * 3600)
        minute = second // 60
        seconds = second - (minute * 60)
        t = Time(hour, minute, seconds)
        return t

    # convert time to seconds
    def convert_time_to_second(self):
        result = (self.h * 3600) + (self.m * 60) + (self.s)
        return result

    # convert GMT to Tehran time
    def convert_gmt_to_tehran(self):
        t = Time(3, 30, 0)
        tehran_time = self.sum(t)
        return tehran_time

    # fix time
    def fix(self):
        if self.s >= 60:
            self.s -= 60
            self.m += 1

        if self.m >= 60:
            self.m -= 60
            self.h += 1

        if self.s < 0:
            self.s += 60
            self.m -= 1

        if self.m < 0:
            self.m += 60
            self.h -= 1

    # show time
    def show(self):
        print(self.h, ":", self.m, ":", self.s)

    # check digital format
    def convert_to_digital(self):
        if self.s < 10:
            sss = str(self.s)
            self.s = "0" + sss

        if self.m < 10:
            mmm = str(self.m)
            self.m = "0" + mmm

        if self.h < 10:
            hhh = str(self.h)
            self.h = "0" + hhh


""" zaman1 = Time(4, 36, 45)
zaman1.show()

zaman2 = Time(2, 26, 17)

zaman3 = zaman1.sum(zaman2)
zaman3.convert_to_digital()
zaman3.show()

zaman4 = zaman1.convert_time_to_second()
print(zaman4)

zaman5 = zaman1.convert_gmt_to_tehran()
zaman5.convert_to_digital()
zaman5.show() """

z = Time.convert_second_to_time(4550)
z.show()

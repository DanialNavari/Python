#import library
import re

#give time
zaman = input("Enter time (hh:mm:ss): ")

#splite string by : delimiter
zaman_sp = re.split(':',zaman)
hour = int(zaman_sp[0])
minute = int(zaman_sp[1])
second = int(zaman_sp[2])

#convert time to second
converted_time = (hour * 3600) + (minute * 60) + second

#print converted time to second
print("⏱ : ",converted_time,"second")

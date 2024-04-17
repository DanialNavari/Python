#give time
zaman = int(input("Enter second: "))

#convert second to hour , minute and second
second_to_hour = round(zaman / 3600,3)                # ex:3800 / 3600 = 1.055
hour = int(second_to_hour)                            # ex: 1 hour
minute = (second_to_hour - int(hour))* 60             # ex: 1.055 - 1 = 0.055 * 60 = 3 minute
second = (minute - int(minute)) * 60                  # ex: 3.3 - 3 = 0.3 * 60 = 18 second

#convert time to "hh:mm:ss" format
if hour<10:
    saat = "0" + str(hour)
else:
    saat = str(hour)

if int(minute)<10:
    daghighe = "0" + str(int(minute))
else:
    daghighe = str(int(minute))

if int(second)<10:
    saniye = "0" + str(int(second))
else:
    saniye = str(int(second))


#print converted time to H:m:s
print("⏱ : ",saat,":",daghighe,":",saniye)

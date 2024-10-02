import random

print("Turn 🎲 : d")
txt = input("Turn Dic... : ")

while(txt!="exit"):
    dic_num = random.randint(1,6)
    
    if dic_num == 6:
        print("🎲 : ",dic_num)
        print("🎉🎉🎉 P R I Z E 🎉🎉🎉")
        txt = input("Turn Dic Again... : ")
    else:
        print("🎲 : ",dic_num)
        break

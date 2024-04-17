#import library
import random

#define variables
computer_choise = ''
user_point = 0
computer_point = 0
round = 0

#loop
for i in range(3):
    round = i + 1
    print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦ Round ",round,"♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
    x = random.choice(["p","s","c"])
    print("c : ✂")
    print("p : 📄")
    print("s : 🧱")
    items = {"c": "✂", "p":"📄", "s":"🧱"}
    user_choise = input("Choose: ")

#print computer and user choise
    print("🧞 => ",items[user_choise])
    print("💻 => ",items[x])

#conditions
    if user_choise=="c" or user_choise=="p" or user_choise=="s":
        if x == "c":
            computer_choise = "c"
        elif x=="p":
            computer_choise = "p"
        elif x=="s":
            computer_choise = "s"
        else:
            computer_choise = random.choice(["c","s","p"])
    
    else:
        user_choise = random.choice(["c","s","p"])
    
    if computer_choise == user_choise:
        user_point = user_point +0
        computer_point = computer_point +0

    elif user_choise =="c":
        if computer_choise == "p":
            user_point = user_point + 1

        if computer_choise == "s":
            computer_point = computer_point + 1

    elif user_choise == "s":
        if computer_choise == "p":
            computer_point = computer_point + 1

        elif computer_choise =="c":
            user_point = user_point +1

    elif user_choise == "p" :
        if computer_choise == "s":
            user_point = user_point + 1

        elif computer_choise =="c":
            computer_choise = computer_choise +1

#print user and computer scores    
    print("user : ",user_point)
    print("computer : ",computer_point)

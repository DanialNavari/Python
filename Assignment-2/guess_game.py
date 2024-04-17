#import library
import random

#determine limitation
computer_number = random.randint(10,40)

#define variables
pos = True
guess_number = 0

#loop
while pos==True :
    user_number = int(input("Guess your number Between 10 and 40 :"))
#win
    if user_number == computer_number :
        guess_number = guess_number + 1
        print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉 Y o u W i n !! 🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
        print("You win after",guess_number,"guess")
        break
#go up
    elif user_number < computer_number :
        guess_number = guess_number + 1
        print("go up")
#go down
    elif user_number > computer_number :
        guess_number = guess_number + 1
        print("go down")

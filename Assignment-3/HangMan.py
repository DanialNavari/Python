#import library
import random

#define word bank
word_bank= ["Create","use","vocabulary","recall","Universal","learned","online","instantly","summary","topic"]

#random choice
word = random.choice(word_bank).lower()

#define variables
mistake = 0
good_word = []
bad_word = []

#max time user can mistake is 6
while mistake<6:

    #check user guess word or not
        for i in range(len(word)):
            if word[i] in good_word:
                print(word[i],end="")
            else:
                print('-',end=' ')

        if len(good_word) != len(word):
        
            #give user word
            user_word = input(" Guess letter: ")

            #user must enter one charachter
            if len(user_word)==1:

                #user guess true
                if user_word in word:
                    good_word.append(user_word)
                    print("✅")

                #user guess false
                else:
                    bad_word.append(user_word)
                    mistake +=1
                    print("❌")

            else:
                print("Enter Only One Charachter")

            #user win
        else:
            print("\n🎉 🎉 🎉 Y O U  W I N 🎉 🎉 🎉")
            break


#user lost
if mistake == 6:
    print("\n⛔ ⛔ ⛔ G A M E  O V E R ⛔ ⛔ ⛔")
    print("Word is : ",word)
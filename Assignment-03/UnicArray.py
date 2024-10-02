#import library
import random

#define emprty array
array = []

#give array member from user
user_len = int(input("Enter Array Members: "))

#loop
for i in range(user_len):

    #make random number between 0 , 100
    ran_num = random.randint(0,100)
    if ran_num in array:
        continue
    else:
        array.append(ran_num)    

#print array
print(array)
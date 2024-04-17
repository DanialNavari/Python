#import library
import re

#give array from user
array = input("Enter array Like: 1,2,3 :")

#splite string to list by , delimiter
array_member = re.split(",",array)

#define emprty array
check = 0

#loop
for i in range(len(array_member)):

    #check array number is greater than ckeck variable
    if int(array_member[i])>check:
        check = int(array_member[i])
        if i == len(array_member) -1 :
            print("🎉 🎉 🎉 Array is an ordered 🎉 🎉 🎉")
    else:
        print("❌ ❌ ❌ Array is not an ordered ❌ ❌ ❌")

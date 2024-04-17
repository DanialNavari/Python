#import library
import re

#give array from user
array = input("Enter array Like: 1,2,3 :")

#splite string to list by , delimiter
array_member = re.split(",",array)
new_array = []

for item in array_member:
    if item not in new_array:
        new_array.append(item)
    else:
        continue

print(new_array)
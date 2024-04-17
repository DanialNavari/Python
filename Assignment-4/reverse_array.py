#import library
import re

#give array from user
array = input("Enter array Like: 1,2,3 :")

#splite string to list by , delimiter
array_member = re.split(",",array)

print(array_member[::-1])
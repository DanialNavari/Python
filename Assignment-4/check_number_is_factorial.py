number = int(input("Enter number: "))

mul = 1
start_num = 1

while(True):
    mul = mul * start_num
    start_num +=1

    if mul == number:
        print("Yes!!")
        break
    elif mul> number:
        print("No..")
        break

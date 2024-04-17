#Give three side of triangle
a = int(input("Enter First side: "))
b = int(input("Enter Second side: "))
c = int(input("Enter Third side: "))

#Condition : sides aren't zero
if a<=0 or b<=0 or c<=0 :
    print("Numbers must be greater than zero")
elif a+b<c or b+c<a or a+c<b :
    print("Impossible to draw this triangle")
else:
    print("Good...Possible to draw.")
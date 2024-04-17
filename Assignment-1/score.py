#Give name & family & 3 lesson scores
name = input("Enter Student Name: ")
family = input("Enter Student Family: ")
l1 = float(input("Enter First Lession Score: "))
l2 = float(input("Enter Second Lession Score: "))
l3 = float(input("Enter Third Lession Score: "))

#calculate average
avg = (l1+l2+l3) / 3
if avg>=17:
    result = "Great"
elif avg<17 and avg>=12:
    result = "Normal"
elif avg<12:
    result = "Fail"

print("Student :",name,family,"| Average Scores: ",round(avg,2),"| Educational status:",result)
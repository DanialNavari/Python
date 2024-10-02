#set variables
point = 0
lession_num = 0
pos = True

#while loop
while (pos == True):
    #give input
    score = input("Enter Student's Score: ");
    if score == "exit":
        break
    else:
        point = point + float(score)
        lession_num = lession_num + 1


#calculate average
avg = round(point / lession_num,2)
print("Average Scores: ",avg)
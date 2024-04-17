#variable for rows and columns
n=0
m = 0

#check n and m must be greater than 0
while n<=0 or m<=0:
    n = int(input("Enter Satr: "))   #rows
    m = int(input("Enter Sotoon: "))   #columns

#final mull table
y = []

#temp array
z = []

for num in range(1,m+1):
    z.append(num)
y.append(z)
z = []

for nums in range(2,n+1):
    for num in range(m):
        z.append(nums * y[0][num])
    y.append(z)
    z = []

for item in y:
    table = '   '.join(str(x) for x in item)
    print(table)
#variable for rows and columns
n=0
m = 0
star = '*'
sharp = '#'

#check n and m must be greater than 0
while n<=0 or m<=0:
    n = int(input("Enter Satr: "))   #rows
    m = int(input("Enter Sotoon: "))   #columns

#final mull table
y = []

#temp array
z = []

for num in range(1,m+1):
    if num%2==0:
        z.append(sharp)
    else:
        z.append(star)
y.append(z)
z = []

for nums in range(2,n+1):
    for num in range(m):
        if num%2==0:
            z.append(star)
        else:
            z.append(sharp)
    y.append(z)
    z = []

for item in y:
    chess = ''.join(item)
    print(chess)
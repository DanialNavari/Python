row=int(input("Enter the number of row:"))
mat=[[1 for i in range(row)] for ij in range(row)]

for i in range(row):
    for j in range(1,i):
        mat[i][j]=mat[i-1][j]+mat[i-1][j-1]

for i in range(row):
    for j in range(i+1):
        print(mat[i][j],end=" ")
    print("")
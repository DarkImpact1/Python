m = int(input("enter number of rows  :\t"))
n = int(input("enter number of columns : \t"))
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)
print(matrix)



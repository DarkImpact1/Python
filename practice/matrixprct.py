# row=column=int(input())
# matrix=[]
# for i in range(row):
#     sub=[]
#     for j in range(column):
#         n=int(input())
#         sub.append(n)
#     matrix.append(sub)
# print(matrix)

# diagonal=[]
# for i in range(row):
#     for j in range(column):
#         if i ==j:
#             diagonal.append(matrix[i][j])
# print(diagonal)
# i=0
# j=len(matrix[0])-1
# d=[]
# while i < len(matrix) and j >=0:
#     d.append(matrix[i][j])
#     i+=1
#     j-=1
# print(d)
A=[]
Ar=int(input("row of matrix A: "))
Ac=int(input("column of matrix A: "))
for i in range(Ar):
    subA=[]
    for j in range(Ac):
        # n=int(input())
        subA.append(j)
    A.append(subA)

print(A)

B=[]
Br=int(input("row of matrix B: "))
Bc=int(input("column of matrix B: "))
for i in range(Br):
    subB=[]
    for j in range(Bc):
        # n=int(input())
        subB.append(j)
    B.append(subB)
print(B)

# multi=[]
# if Ac==Br and Ar==Bc:
#     print("multiplication is possible")
#     for i in range(Ar):
#         submulti=[]
#         add=0
#         for j in range(Br):
#             add+=(A[i][j]*B[j][i])
#         submulti.append(add)
#         multi.append(submulti)
#     print(multi)
# else:
#     print("multiplication is not possible")


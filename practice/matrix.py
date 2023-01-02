Mrow= int(input())
Mcolumn = int(input())

mat = []
for i in range(Mrow):
    localmat = []
    for i in range(Mcolumn):
        localmat.append(i)
    mat.append(localmat)

print(mat)


Transpose=[]
Trow=Mcolumn
Tcolumn=Mrow
for i in range(Trow):
    subt=[]
    for j in range(Tcolumn):
        subt.append(mat[j][i])
    Transpose.append(subt)
print(Transpose)


# mainlist = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     mainlist.append([name, score])
# print(mainlist)
# sortt = []
# for i in range(len(mainlist)):
#     sortt.append(mainlist[i][1])
# print(sortt)


# def mod(a, b):
#     return int([a-b if a > b else b-a][0])


# print(mod(5, 7))
# print(mod(7, 5))

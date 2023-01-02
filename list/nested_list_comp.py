# our objective ----- create a list which contain [[1,2,3],[1,2,3],[1,2,3]]
# Normal method
x = []
y = []
for i in range(1, 4):
    y.append(i)
    x.append(y)
print(x)

# using list comprehension

x = [[i for i in range(1, 4)] for i in range(1, 4)]
print(x)

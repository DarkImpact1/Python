# Normal method
num = list(range(1, 11))
x = []
for i in num:
    if i % 2 == 0:
        x.append(i)
print(x)
# Now using list comprehension
# Note---- sirf space use krna hai comprehension me
# x=[hmein append krna hai ek number..i.. jo num me present hai..for loop.. or tb jn vo even ho..if condition..]
x = [i for i in num if i % 2 == 0]
print(x)
y = [i for i in range(1, 11) if i % 2 == 0]
print(y)
# -------odd numbers
x = [i for i in num if i % 2 != 0]
print(x)
y = [i for i in range(1, 11) if i % 2 != 0]
print(y)

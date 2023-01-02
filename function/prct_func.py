def greater(a, b):
    if a > b:
        return a
    return b


n1, n2 = int(input("first number\t")), int(input("Second number\t"))
bigger = greater(n1, n2)
print(f"{bigger} is greater")


# here we have to built a program which will tell the biggest of the following number

def greatest(a, b, c):
    bigger = greater(a, b)
    return greater(bigger, c)


print(greatest(10, 200, 30))

# just abovve code in short


def greatest(a, b, c):
    return greater(greater(a, b), c)


print(greatest(10, 200, 30))

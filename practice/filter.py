def prime1(a):
    for i in range(2, a):
        if a % i == 0:
            return False
        else:
            return True


l = [1, 2, 3, 4, 13, 244, 101, 239, 157]
filtered = filter(prime1, l)
print(list(filtered))

filterd2 = list(filter(prime1, range(1, 100)))
print(filterd2)

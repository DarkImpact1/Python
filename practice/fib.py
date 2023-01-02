def fib(n):
    n1 = 0
    n2 = 1
    if n == 1:
        print(n1)
    elif n == 2:
        print(n1, n2)
    else:
        print(n1, n2, end=" ")
        for i in range(n-2):
            nth = n1+n2
            print(nth, end=" ")
            n1 = n2
            n2 = nth


n = int(input())
fib(n)

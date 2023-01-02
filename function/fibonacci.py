def fibonacci(num):
    n1, n2 = 0, 1
    if num == 1:
        print(n1)
    elif num == 2:
        print(n1, n2)
    else:
        print(n1, n2, end=" ")
        for i in range(num-2):
            n3 = n1+n2
            n1 = n2
            n2 = n3
            print(n2, end=" ")


num = int(input("Enter the number upto which you want to print fibonacci series"))
print(fibonacci(num))

def is_prime(a):
    if a < 0:
        print("enter positive number")
    elif a == 1:
        print("it's not a prime number")
    else:
        fact = 0
        for i in range(1, a+1):
            if a % i == 0:
                fact += 1

        if fact == 2:
            return ("It's a prime number")
        else:
            return ("it's not a prime number")


print(is_prime(101))

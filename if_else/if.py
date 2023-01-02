""" several method to write code in a single line using if else ..."""

a = 10
b = 20
print("a is greater than b") if a > b else print("b is greater than a")

if 2012 % 4 == 0:
    print("it's a leap year")
if 2013 % 4 == 0:
    print("it's not a leap year")

print("it's a leap year") if int(
    input()) % 4 == 0 else print("it's not a leap year")

print("it's a even number ") if int(
    input()) % 2 == 0 else print("it's an odd number")

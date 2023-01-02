# it is very useful for any programming language
# we had already used many functons but we are not aware of the actual definition of how to make function
# for example
# name="mohit"
# print(len(name))
# here len is the pre defined funtion which we we using to calculate the length of string

# lets define a funtion by our self
# here's the syntax

# def name_of_funtion(variables to be pass):
#     you program to work with those variables
#     return what do you want to return

def add(a, b):  # here a and b is parameter
    return a+b  # we can write print instead of return to directy print the output


num1, num2 = int(input("Enter first number: \t")), int(
    input("enter second number: \t"))
fname, lname = input("enter first name: \t"), input("Enter last name: \t")
# time to call funtion
# here it will add both numbers & remember num1 and num2 are arguments
total = add(num1, num2)
name = add(fname, lname)  # here it will concatenate both name
print(total)
print(name)


# we can also define a funtion which would not take any input but give output
# example
def song():
    return "Swalla la la "


print(song())

# ------------------------------------------------------------------------------------
# we can also define funtion inside a function
# for more info open prct_func

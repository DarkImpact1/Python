# decorators - engance the functionality of other functions
# it is type of function which is used to enhance the functionality of other function 
def decorator_function(any_function):
    def executor():
        print("executing now")
        any_function()
        print("executed")
    return executor

def func1():
    print("Hello this function is used in decorator")

x=decorator_function(func1)
x()

# instead of writing line 13 we can use @ symbol just before the program
@decorator_function
def func2():
    print("Hello this function2 is used in decorator")

func2()
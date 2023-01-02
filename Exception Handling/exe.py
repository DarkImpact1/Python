def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return ("You can't divide a number by zero..")
    except TypeError as msg:
        return msg
    except:
        return "unexpected error"
print(divide(10,0))

# Exceptions are those error which come into the picture during executions
# try and except are like if and else:
# and remember one try can have multiple except

# age = int(input("Enter your age:\t"))

# if age<18:
#     print("You're minor.....")
# else:
#     print("You're adult now")

    
    
    
    
try:
    age = int(input("Enter your age:\t"))#seven--- then except block will run and age variable will not be declared..
except:
    print("Invalid input")
if age<18:
    print("You're minor.....")
else:
    print("You're adult now")

while True:
    try:
        age=int(input("Enter your age:\t"))
        break
    # except when or which type of error.....
    except ValueError:
        print("Enter numeric value..")
    except:
        print("Unexpecter error...")

if age<18:
    print("You're minor.....")
else:
    print("You're adult now")
while True:
    try:
        age=int(input("Enter your age:\t"))
    # except when or which type of error.....
    except ValueError:
        print("Enter numeric value..")
    except:
        print("Unexpecter error...")
    #else: block will execute only then when try block is executed successfully....
    else:
        print("else block executing...")
        break
    #this block will be always executed either you're handling any exceptions.....
    finally:
            print("Finally block....")

if age<18:
    print("You're minor.....")
else:
    print("You're adult now")


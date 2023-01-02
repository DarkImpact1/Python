def validate(password):
    if len(password)<8:
        raise ValueError("Password is short")
pswrd=input("Enter your password:\t")
validate(pswrd)
print(f"Your password is {pswrd}")

class PasswordShortError(ValueError):
    pass



def validate(password):
    if len(password)<8:
        raise PasswordShortError("Password is short")
pswrd=input("Enter your password:\t")
validate(pswrd)
print(f"Your password is {pswrd}")
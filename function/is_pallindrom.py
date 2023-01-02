# 1.
def is_pallindrom1(name):
    reversed_name = name[::-1]
    if name == reversed_name:
        return True
    return False

# 2.


def is_pallindrom2(name):
    if name == name[::-1]:
        return True
    return False

# 3.


def is_pallindrom3(name):
    return name == name[::-1]


x = input()
print(x == x[::-1])

# print(is_pallindrom1("mohit"))  # ----False
# print(is_pallindrom1("naman"))  # ----True
# print(is_pallindrom2("mohit"))  # ----False
# print(is_pallindrom2("naman"))  # ----True
# print(is_pallindrom3("mohit"))  # ----False
# print(is_pallindrom3("naman"))  # ----True
# all the defined program will give same output

# name="Mohit"
# -- **Mohit**

# SYNTAX-- .center("length of string + number of character you want add", "what you want to add")

# print(name.center(9,"#"))#--- ##Mohit##
# print(name.center(7,"$"))#-- $Mohit$
# print(name.center(6,"%"))#-- Mohit%   it will add on the right side


# suppose we want a user to enter his full name with any way he want then we will modify his name and give design to his name by adding 4 stars both side

fname, lname = input("enter your full name separated by comma\n").split(",")
total = fname.strip()+" "+lname.strip()
name = total.title()
print(name)
print(name.center(len(name)+8, "*"))

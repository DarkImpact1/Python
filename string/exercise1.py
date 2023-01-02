# fname,lname,age=input("Enter your first name, last name and age separated by comma:- ").split(",")
# total=fname+" "+lname
# print(f"Your name is {total.title()}\nYour age is {age}")
# print(f"Length of your full name is {len(total)}")
# x=input("Input any character to find how many times it appears in your name:  ")
# print(f"{x} appears {total.lower().count(x.lower())} times")




#------------------------------------------------------------------------------------------------------

# it will take input from user then print the number of character asked by user to count even if he give space and is case insenstives
string,char=input("enter any string and character to be count from that string comma separated:-   ").split(",")
print(string.strip().lower().count(char.strip().lower()))
print(len(string))

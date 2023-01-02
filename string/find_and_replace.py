name="Suraj Gaurav Kuldeep Chanchal Vaibhav Mohit Harshit Umang Raunak"
# we can use replace method to replace any character by anything ---
#Syntax-- .replace("Old","new","how many")
print(name.replace(" ","_"))
print(name.replace(" " , "$", 5))

# find method is user to find position of any string or character from particular data
#syntax-- .find("what", "from where", "to where")
name="He is very intellgent as well as determined person. He is hardworking and responsible person"
print(name.find("is"))
print(name.find("is", 5))

#suppose we don't know the position of first "is" and want to find the position of second "is"

pos1=name.find("is") # it will give a position of first "is"
# Now to find the position of second is we will use the position of first is 
print(name.find("is", pos1+1))
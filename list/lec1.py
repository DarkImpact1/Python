# we can create a list in only one line

# # for example
cube = []
for i in range(1, 11):
    cube.append(i**3)
print(cube)


# Now with the use of list comprehension
# listname=[mujhe kya krna space hai kaise krna hai ]
cube2 = [i**3 for i in range(1, 11)]

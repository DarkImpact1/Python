name="       Mohit       "
dots="..................."
print(name + dots)
#-- lstrip() method is used to remove space from the left side
#-- rstrip() method is used to remove space from the right side
#-- strip() method is used to remove space from both side

print(name.lstrip() + dots)
print(name.rstrip() + dots)
print(name.strip() + dots)

# strip method will not remove space in between string 
# To remove space from in between string you can use --replace("what to replace","from what") method

name="Mo      hi  t"
print(name)
print(name.replace(" ",""))
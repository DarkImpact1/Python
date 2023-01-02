# ek list hai jisme kisi bhi type ka data store ho hmein usme se sirf integer and float ko print krwana hai or unka data type string ho

# Normal method
mixed = ["mohit", "harshit", 1, 2, 3.3, [
    "vaibhav", "ritik"], ("sunday", "monday")]
new_list = []
for i in mixed:
    if type(i) == int or type(i) == float:
        new_list.append(str(i))
print(new_list)

# Using list comprehension

new_list = [i for i in mixed if type(i) == int or type(i) == float]
print(new_list)
new_list = [str(i) for i in mixed if type(i) == int or type(i) == float]
print(new_list)

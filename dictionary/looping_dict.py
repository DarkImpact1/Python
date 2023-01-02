user_info = {
    "name": "Mohit",
    "age": 21,
    "fav. song": ["perfect", "Le Le rom rom"],
    "fav. game": ["Volleyball", "football"],
}

# # check if key exist in dictionary
if "name" in user_info:
    print("present")
else:
    print("not present")

# # check if value exist in dictionary
if "mohit" in user_info:
    print("present")
else:
    print("not present")
# # this is wrong because it will check key not values
if "mohit" in user_info.values():  # ------ VALUES METHOD
    print("present")
else:
    print("not present")


# #loops in dictionary

for i in user_info:
    print(i)  # ---> all keys

for i in user_info.value():
    print(i)  # ---> all values

# #another method
for i in user_info:
    print(user_info[i])  # -- all values

# # or to get directly all the values or keys directly use key() and values() method

print(user_info.values())  # -->type-- dict_values
print(user_info.keys())  # --> type-- dict_keys

# MOST IMPORTANT AND USEFUL METHOD IS .ITEM() METHOD

x = user_info.items()
print(x)  # --[(),(),()]
print(type(x))  # --> dict_items

for key, value in user_info.items():
    print(f"key is {key} value is {value}")
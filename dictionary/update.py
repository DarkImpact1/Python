user_info = {
    "name": "Mohit",
    "age": 21,
    "fav. song": ["perfect", "Le Le rom rom"],
    "fav. game": ["Volleyball", "football"],
}

# how to add data
user_info["key"] = ["value"]
print(user_info)

# how to delete data
# pop method
popped_item = user_info.pop("key")  # you have to pass atleast one argument
print(popped_item)  # return --- str because value is in string
print(user_info)

# popitem method
# don't need to pass any argument it will delete randomly
popped_item = user_info.popitem()
print(user_info)
print(popped_item)  # return --- tuple
# ------------------------------------------------------------------------------------------

more_info = {
    "name": "Harshit",  # will update the previous name
    "state": "Uttar pradesh",
    "District": "pratapgarh",
}
# if you want to add these data in user_info then user update(dictname)
user_info.update(more_info)
print(user_info)
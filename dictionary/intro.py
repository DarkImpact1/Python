# why python introduced dictionary when we have list as well as tuples
# it's because we can't update tuple and use of list is limited
# like you want to store user's info then we have to remember at which index we had stored users choice
user = ["mohit", '19', ["perfect", "le le rom rom"], ["volleyball", "football"]]
# in this list we can't know which one is user's fav. song or fav. game ...So to represent these in a better way python introduced dictionary
# Dictionary is unordered collection of data in key : value pair.
# syntax
user = {"name": "Mohit", "Age": 19}  # use {} brackets to create dictionary
print(user)
print(type(user))

# Another method to create dictionary
user = dict(name="Mohit", age=24)
print(user)

# HOW TO ACCESS DATA FROM DICTIONARY
# there is no indexing in dictionary
# we take help of key to access data
#syntax---- dictname["key"]
print(user["name"])

# WE CAN STORE ANYTHING IN DICTIONARY

user_info = {
    "name": "Mohit",
    "age": 21,
    "fav. song": ["perfect", "Le Le rom rom"],
    "fav. game": ["Volleyball", "football"],
}
print(user_info["fav. game"])

# CREATING DICTIONARY INSIDE DICTIONARY
users = {
    "user1": {
        "name": "Mohit",
        "age": 21,
        "fav. song": ["perfect", "Le Le rom rom"],
        "fav. game": ["Volleyball", "football"],
    },
    "user2": {
        "name": "Mohit",
        "age": 21,
        "fav. song": ["perfect", "Le Le rom rom"],
        "fav. game": ["Volleyball", "football"],
    }
}
print(users["user1"])

#  HOW TO ADD DATA TO YOUR DICTIONARY

user_info2 = {}
user_info2["key"] = "value"  # syntax
print(user_info2)

# IN MOST OF THE CASES WE USE STRING AND INTEGER AS A KEY IN DICTIONARY

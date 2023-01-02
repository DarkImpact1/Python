user_info = {
    "name": "Mohit",
    "age": 21,  # fist time
    "fav. song": ["perfect", "Le Le rom rom"],
    "fav. game": ["Volleyball", "football"],
    "age": 24,  # second time

}
print(user_info.get("name"))  # -- Mohit
print(user_info.get("state"))  # -- none
print(user_info.get("state", "not found"))  # -- not found
# -- 24 --- same key more than once can't exist in dictionary ..... last value will override that value
print(user_info.get("age"))

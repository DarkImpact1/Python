# make a dictionary and add data into it
user_info = {
    "name": "Mohit",
    "age": 21,
    "fav. song": ["perfect", "Le Le rom rom"],
    "fav. game": ["Volleyball", "football"],
}

# popped_item = user_info.pop('age')
# print(popped_item)
# print(user_info)
d = dict.fromkeys(range(1, 11), "unknown")
print(d)
# {1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown', 6: 'unknown', 7: 'unknown', 8: 'unknown', 9: 'unknown', 10: 'unknown'}
updated_d = {
    1: 'mohit',
    2: 'mohit2',
    3: 'mohit3',
    4: 'mohit4',
    5: 'mohit5',
    6: 'mohit6',
    7: 'mohit7',
    8: 'mohit8',
    9: 'mohit9',
    10: 'mohit10',
}
d.update(updated_d)
print(d)
# {1: 'mohit', 2: 'mohit2', 3: 'mohit3', 4: 'mohit4', 5: 'mohit5', 6: 'mohit6', 7: 'mohit7', 8: 'mohit8', 9: 'mohit8', 10: 'unknown'}

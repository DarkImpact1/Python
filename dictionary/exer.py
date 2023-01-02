user_info = {}
name, age = input("Your name : "), int(input("Your age : "))
fav_game = input("your favourite games separated by comma : ").split(",")
hobbies = input("your hobbies separated by comma : ").split(",")

user_info["name"] = name
user_info["age"] = age
user_info["fav_game"] = fav_game
user_info["hobbies"] = hobbies

for i, j in user_info.items():
    print(f"{i} : {j}")

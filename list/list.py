# list is a data structure of ordered collection of item which we use to store,
# syntax= [anything inside this bracket will be consider as a part of list]
# we can store any type of data in list
# example:
mixed = [1, 2, 3, [4, 5, 6], "seven", 8.0, None]
print(mixed[3])  # output----> [4,5,6]


# -------------------------HOW TO ADD DATA IN OUR LIST------------------------------------


# item = []
# # 1st method  .append(item)
# item.append("10")  # will add this at last
# print(item)  # ---->["10"]
# # 2 method .insert(position,item)
# item.insert(0, "Hello")  # -->["Hello","10"]
# # 3 method .extend(item)
# item2 = [1, 2, 3]
# item.append(item2)  # ---->["Hello","10",[1,2,3]]
# item.extend(item2)  # ---->["Hello","10",1,2,3]
# # you can easily join any list to any list and store that value in another variable

# # ------------------------HOW TO DELETE/REMOVE DATA FROM OUR LIST-----------------------------

# # 1 .pop() it will remove last data of our list and will return that value too
# # and you can also pass value in pop to remove data from particular position .pop(position)
# x = item.pop()  # --> ["Hello","10",[1,2,3],1,2] and x=3
# item.pop(0)  # -->["10",[1,2,3],1,2]
# # 2 .remove(value) if you don't know the position then use delete method
# item.remove(2)  # -->["10",[1,2,3],1]
# # 3 del name_of_list[position]
# del item[0]  # -->[[1,2,3],1]


# # ---------------------LOOP IN LIST--------------------------

# # same as loop we used in string

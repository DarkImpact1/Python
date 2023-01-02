# set is unordered collection of unique items
# set is use to remove duplicate item
# syntax----- s={1,3,4,5,6,7} use of curly brackets and same items can't be exist

s = {1, 2, 4, 5}
l = [1, 2, 2, 3, 4, 4, 5, 5, 6, 8, 7, 7, 6, 6, 5, 5, 4, 4, 4, 3, 3, 3, 3]
s2 = set(l)  # it will remove duplicate item
print(s2)


# Methods used in set
# s.add(item)
s.add(7)
# s.remove(item)
s.remove(4)  # if item is not in set it will show error
# s.discard(item)
s.discard(3)  # if item is not in set it won't show any error
# s.clear()
s.clear()  # it will clear the data of set
s.add(7)
# s.copy()
s1 = s.copy()

# which data type we can store in set
# string, integer, float,
# we can't store list, dict,tuple in our set and can't use indexing also

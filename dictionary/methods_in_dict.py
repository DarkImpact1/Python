# fromkeys
# x= {"name" : "unknown", "age": "unknown"}
# if you want to assign same values(it can be anything like list, string, integer....) to different keys then use fromkeys method
#---------------------------------dict.fromkeys(["key1","key2","key3"],"value")-------------------------------------------------------------------------------------------
# using paranthesis
d = dict.fromkeys(("name", "age", "state"), "unknown")
# using square bracket
d = dict.fromkeys(["name", "age", "state"], "unknown")
# it will assign unknown value to a, b, c, d
d = dict.fromkeys("abcd", "unknown")
# it will assign unknown value to 1 to 10 key
d = dict.fromkeys(range(1, 11), "unknown")

# --------------GET METHOD------------------
d = dict.fromkeys(("name", "age", "state"), "unknown")
print(d["name"])  # --- unknown
print(d["names"])  # --- error
# to get rid of error we use get method

print(d.get("name"))  # --- unknown
print(d.get("names"))  # --- none

if "name" in d:
    print("present")
else:
    print("not present")
# using get method
if d.get("name"):
    print("present")
else:
    print("not present")
# remember if none:------ it means condition is false therefore else part will be excute


# -----------------CLEAT METHOD------------
print(d.clear())  # it will clear all the data from dictionary

# --------------COPY METHOD------
d1 = d.copy()  # it will create a copy now if you work on d1 then d won't be affected
d1 = d  # in this either you work on d1 or d main dictionary will be affected

# objective--- {1:1, 2:4, 3:9}
# Normal method
square = {}
for i in range(1, 11):
    square[i] = i**2
print(square)


# Using dictionary comprehension
square = {i: i**2 for i in range(1, 11)}

for key, value in square.items():
    print(f"Square of {key} : {value}")

# same output using dictionary comprehension

square = {f"Square of {i}": i**2 for i in range(1, 11)}
print(square)

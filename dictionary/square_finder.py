def square_finder(n):
    square = {}
    for i in range(1,n+1):
        square[i]=i**2
    return square

print(square_finder(10))
print(square_finder(10).items())
# how to make a list of the first 10 square numbers
squares = [] # empty list to store the squares
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares) 

# make code more concise
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)
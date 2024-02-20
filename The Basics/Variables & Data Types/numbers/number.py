# intergers
# you can add(+), subtract(-), multiply(*) and divide(/) integers in python
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)

# use two multiplication signs for exponents

print(3 ** 2)

# python supports the order of operations too
print(2 + 3*4)
print((2+3) * 4)

# Floats - any number with a decimal point
print(0.1 + 0.1)
print(0.2 - 0.1)
print(2.4 * 0.1)

# underscores in numbers
# when writing long numbers, you can group digits using underscores to make the number more readable
total_population = 8_000_000_000
print(f"The population of the universe is approximately {total_population}")

# Python ignores the underscores
# Note: Even if you don't group the digits in threes, the value will still be unaffected

# Multiple assignment - assign values to more than one variable using just a single line
x,y,z = 0,1,2
print(x)
print(y)
print(z)

# constants - variable whose value stays the same throughout the life of a program
# Python doesn't have built-in constant types
# use all capital letters to indicate a variable should be treated as a constant 
MAX_CONNECTIONS = 5000
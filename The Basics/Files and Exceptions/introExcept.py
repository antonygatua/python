# Exception error: When syntax is correct but the code results in an error
# example : ZeroDivisionError
# print(0/0)

# Raising an exception in python 
number = 10

# if number > 5:
#     raise Exception(f'Number Greater than 5: {number}')
# print(number)

number = 1
assert (number < 5), f"The number should not exceed 5. ({number=})"
print(number)

number = 10
assert (number < 5), f"The number should not exceed 5. ({number=})"
print(number)

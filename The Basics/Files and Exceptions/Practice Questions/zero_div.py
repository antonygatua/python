"""
Write a program to handle a ZeroDivisionError Exception when diving a number by zero
"""

def divide_numbers(a, b):
    try:
        # attempt to perform the division operation
        result = a / b
        return result
    except ZeroDivisionError:
        print("The division by zero operation is not allowed.")


out = divide_numbers(12, 0)

print(f'Result: {out}')

"""
Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
"""

def enter_input():
    try:
        val = int(input("Enter a number: "))
        return val
    except ValueError:
        print("Please enter a number")

number = enter_input()

print(f'Number: {number}')
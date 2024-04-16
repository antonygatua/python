"""
Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
"""

def get_numeric_input(prompt):
    # use a repeated loop to prompt the user to enter a number
    limits = 3
    for i in range(limits):
        try:
            # attempt to ge numeric input 
            val = float(input(prompt))

            return val
        except ValueError:
            print("Error: Invalid input, expected a number.")

    print("Try again tomorrow, you have reached the max limit") 
            
n1 = get_numeric_input("Enter the first number: ")
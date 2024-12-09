"""
Write a program to handle ArithmeticError Execption when performing arithemtic operations.
"""

def arithmetic_operations(a, b, symbol):
    try:
        # perform arithmetic operation based on the symbol
        if symbol == "+":
            result = a + b
        elif symbol == "-":
            result = a - b
        elif symbol == "*":
            result = a * b
        elif symbol == "/":
            result = a / b
        else:
            print('Invalid operation symbol. Please use "*", "+", "-", or "/"')
            return None
        return result
    except ArithmeticError:
        print("An Arithmetic error occured. Please check your operation.")
        return None
    
# Example Usage >> Arithmetic error
out = arithmetic_operations(12, 0, '/')
print(f'Result: {out}')

# Example Usage >> invalid symbol
out = arithmetic_operations(12, 0, '?')
print(f'Result: {out}')

# Example Usage >> valid operation
out = arithmetic_operations(12, 12, '+')
print(f'Result: {out}')
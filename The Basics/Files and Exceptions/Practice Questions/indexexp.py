"""
Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
"""
def test_index(data, index):
    try:
        # access an element 
        result = data[index] 

        return result
    except IndexError:
        print("Error: Index out of range")

nth_value = test_index([1, 2, 3, 4, 5, 6], 9)

print(nth_value)
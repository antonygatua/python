"""
Task:
Given an integer `n`, and `n` space-separated integers as input, create a tuple of those integers. 
Then compute and print the result of `hash(tuple)`.

Note:
The `hash()` function is built into Python and does not need to be imported.

Input Format:
- The first line contains an integer `n`, denoting the number of elements in the tuple.
- The second line contains `n` space-separated integers describing the elements of the tuple.

Output Format:
- Print the result of `hash(tuple)`.

Example:
Input:
3
1 2 3

Output:
2528502973977326415
"""

if __name__ == "__main__":
    # number elements in the tuple
    n = int(input())
    
    while True:
        # n space-separated 
        numbers_list = input().split()

        if len(numbers_list) != n:
            continue
        # convert to numbers
        numbers_list = [int(num) for num in numbers_list]
        # convert to tuple
        numbers_tuples = tuple(numbers_list)
        break
        
    print(hash(numbers_tuples))




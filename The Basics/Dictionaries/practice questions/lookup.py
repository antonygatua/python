"""
Task 1: Dictionary Lookup with Default Value
You are given a dictionary containing the names of students as keys and their scores as values.
Write a Python function that retrieves the score of a student using the `get()` method.
If the student is not found in the dictionary, return a default value of 0 instead of raising an error.

Input:
- A dictionary `scores` where keys are student names (strings) and values are their scores (integers).
- A string representing a student name.

Output:
- The score of the student, or 0 if the student is not found in the dictionary.

Example:
Input:
    scores = {'Alice': 90, 'Bob': 75, 'Charlie': 85}
    student_name = 'David'
Output:
    0
"""

if __name__ == "__main__":
    n = int(input('Enter Number of students: '))
    # empty dict to store the values
    students = {}

    for _ in range(n):
        # enter name and score
        name, score = input('Enter name and score: (e.g Alice 90) ').split()

        if name.lower() in list(students.keys()):
            raise ValueError(f'The key {name} already exists!')
        else:
            students[name.lower()] = int(score)
    
    name_to_get = input('Enter name to retrieve score: ').lower()

    # if name_to_get.lower() not in list(students.keys()):
    #     print(0)
    # else:
    #     out = students.get(name_to_get.lower())

    #     print(out)

    # use get() to retrive the score, defaulting to 0 if not found
    out = students.get(name_to_get, 0)

    print(out)
"""
    This script processes student names and their respective scores, calculates the average
    of scores for a queried student, and outputs the result rounded to 2 decimal places.

    Input:
        - The first line contains an integer `n`, the number of students.
        - The next `n` lines contain a student's name followed by their scores (space-separated).
        - The last line contains the name of the student to query.
    
    Output:
        - The average score of the queried student, rounded to 2 decimal places.
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        # single line of input, splits it into parts (separated by spaces), and assigns them to variables.
        name, *line = input().split() # The first part is assigned to name
        scores = list(map(float, line)) # remaining parts are collected into the line variable as a list of floats
        student_marks[name] = scores

    query_name = input() # Name of the student to query

    query_marks = student_marks.get(query_name) # Retrieve scores for the queried student 

    query_mean = round((sum(query_marks) / len(query_marks)), 2) # Calculate average, rounded to 2 decimal places

    print(query_mean)
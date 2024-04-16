"""
Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
"""
import os

def file_permision(file_path, file_name):
    try:
        with open(os.path.join(file_path, file_name), 'r') as files:
            lines = files.readlines() 
            for line in lines:
                print(line)
    except PermissionError:
        print('No permision to write to the file.')

file_permision('The Basics/Files and Exceptions/','programming.txt')

"""
Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
"""
import os

def open_file(file_path, file_name):
    try:
        with open(os.path.join(file_path, file_name), 'r') as files:
            lines = files.readlines() 
            return lines

    except FileNotFoundError as error:
        print(error)

data = open_file('The Basics/Files and Exceptions/', 'programmng.txt')

print(data)
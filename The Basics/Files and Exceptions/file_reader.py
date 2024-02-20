# reading an entire file
"""Program that opens the file pi_digits.txt
Reads the file and prints the contents of the file to the screen
"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# making a list of lines from a file
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.lstrip())
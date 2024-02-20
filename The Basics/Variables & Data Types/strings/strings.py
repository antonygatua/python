# strings - series of characters
# Anything in quotes is considered a string in python

"This is a string"
'This also is a string'

# Using apostrophes and quotes
'I told my friend, "Python is my favourite language!"'
"One of Python's strengths is its diverse and supportive community."

# changing case in a string with methods
# Method - an action that python can perform on a piece of data
name = "antonny muiko"
print(name.title()) # makes the first letter capital
print(name.upper()) # all uppercase
print(name.lower()) # all lower

# variables in strings
first_name = "antonny"
last_name = "muiko"
full_name = f"{first_name} {last_name}" # f-strings 
print(full_name)

# compose message with f-strings
print(f"Hello, {full_name.title()}!")

# Adding Whitespace to strings
# whitespace - Any non printing character ie space, tabs
print("Python")

print("\tPython") # add a tab next to text

print("Langauages:\nPython\nC\nJavaScript") # add a newline in a string

print("Langauages:\n\tPython\n\tC\n\tJavaScript") # combine tabs and newlines in a single string

# stripping Whitespace - Extra Whitespace can be confusing in much simpler situations ie checking people's username

favorite_language = "Python "
print(favorite_language.rstrip()) # remove whitespaces at the right end of a string

my_name = " Antonny"
print(my_name.lstrip()) # remove whitespaces at the end left end of a string

# try it yourself 
# Personal Message: use a variable to represent a person's name, and print
# a message to that person
person = "Jomo"
msg = "Have you done some make up today?"
print(f"Hello {person}, {msg}")

# Name cases: Use a variable to reperesent a person's name, and then print that person's name in
# lowercase, uppercase and title case
second_name = "mUiKo"

print(second_name.title())
print(second_name.upper())
print(second_name.lower())

# famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
print('Chambilecho wahenga, "Cha mkufuu mwanafu ha, na akila hu".')

# repeat the exercise above but this time represent the famous person's name using a variable called famaous_person.
# the compose your message and represent it with a new variable called message
# print your message

famous_person = "Wahenga"
message = f'Chambilecho {famous_person}, "Cha mkufuu mwanafu ha, na akila hu".'
print(message)
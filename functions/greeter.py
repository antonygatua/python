# simple function named greet_user() that prints a greetings 
def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")


greet_user("antonny")
greet_user("ruth")

# try it your self
"""8-1. Message: Write a function called display_message() that prints one sen-
tence telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly."""

def display_message(chapter,chapter_title):
    """Display message: What your learning in this chapter"""
    print(f"This is chapter {chapter} and we are learning about {chapter_title}.")


display_message(8, "functions")

"""8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call."""

def favorite_book(title):
    """Display message"""
    print(f"One of my favorite books is {title}.")


favorite_book("Alice in Wonderland")
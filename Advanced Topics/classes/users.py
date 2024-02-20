"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""
class User:
    """Modelling users"""
    
    def __init__(self, first_name, last_name):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Summary of the user's information"""
        print(f"\nFirst Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")

    def greet_user(self):
        """Prints personalized greetings to the user"""
        print(f"\nHello {self.first_name} {self.last_name}.")

# making an instance of a class 
my_person = User("Ruth", "Jomo")

# calling the methods of the class
my_person.describe_user()
my_person.greet_user()
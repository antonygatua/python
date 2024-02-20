"""
In object-oriented programming you write classes that represent real-world things and situations
And you create objects based on these classes.
Making an object from a class is called instantiation and you work with instances of a class.
"""
# creating the dog class
class Dog:
    """A simple attempt to model a dog"""
    
    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

# making an instance from a class
my_dog = Dog("Willie", 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Accessing Attributes 
print(my_dog.name)

# calling methods
"""
After creating an instance from the class Dog, 
use the dot notation to call any method defined in dog
"""
my_dog.sit()
my_dog.roll_over()

# creating multiple instances 
your_dog = Dog("lucy",3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
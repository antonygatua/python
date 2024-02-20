class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        # setting a default value for an attribute
        self.odometer_reading = 0

    def get_desciptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

# creating an instance
my_new_car = Car("audi", "a4", 2019)

# calling the methods of the class
print(my_new_car.get_desciptive_name())
my_new_car.read_odometer()

# modifying attributes values
modify_attributes = [
    "Change the value directly through an instance.", 
    "Set the value through a method.",
    "Increment the value (add a certain amount to it) through a method."
]
print("\nYou can change an attribute’s value in three ways:")
for modify in modify_attributes:
    print(f"*\t{modify}")

# Modify an Attribute's Value directly
you_car = Car("mercedes", "b180", 2020)
you_car.odometer_reading = 23
you_car.read_odometer()

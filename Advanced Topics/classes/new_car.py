# modifying an attribute's value through a method 
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        # setting a default value for an attribute
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
   
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

# create an instance of the class    
my_new_car = Car('audi', 'a4', 2019)

# Calling methods of the class
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(-1)
my_new_car.read_odometer()

# creating an instance of the class
my_used_car = Car("subaru", "outback", 2016)

# calling the methods
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
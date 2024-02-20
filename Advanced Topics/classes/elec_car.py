# Instance as Attribute
class Car:
    """Simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Declare the variables"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size = 75):
        """Intialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

# define child class
class ElectricCar(Car): # name of the paenthesesrent class must be included in par
    """Represents aspects of car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        # super() allows you to call a method from the parent class
        super().__init__(make, model, year)

        # create a new instance of Battery and assign that instance to the attribute self.battery
        self.battery = Battery()

my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
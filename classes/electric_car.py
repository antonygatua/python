# inheritance
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

# define child class
class ElectricCar(Car): # name of the paenthesesrent class must be included in par
    """Represents aspects of car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        # super() allows you to call a method from the parent class
        super().__init__(make, model, year)

        # defining attributes for the child class
        self.battery_size = 75

    # defining methods for the child class
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
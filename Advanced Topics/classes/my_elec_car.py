# Importing classes
# importing a single class
"""Already have a file named car.py
This file has a class Car
"""

# import car class and then create an instance from that class
from car import Car

my_new_car = Car("audi", 'a4', 2019)
print(my_new_car.get_desciptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# storing Multiple Classes in a module
from electric_car import ElectricCar

my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
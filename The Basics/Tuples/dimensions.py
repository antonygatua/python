# Tuples are immutable - values cannot change
# Use parantheses to create a tuple
# example
# having a rectangle that should always be a ceratin size
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# trying to change will result into an error 
# dimensions[0] = 250
'''
Traceback (most recent call last):
  File "/home/antonnym/Documents/python/Tuples/dimensions.py", line 10, in <module>
    dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment
'''

# tuples are generally defined by the presence of a comma
# if you want to define a tuple with one element, you need to include a trailing comma
my_t = (3,)
print(my_t)

# looping through all values in a tuple 
for dimension in dimensions:
    print(dimension)

# writing over a tuple
# although you can't modify a tuple, you can assign a new value to a variable that represents a tuple
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# try it yourself
# Buffet:Think for five simple foods and store them in a tuple
foods =("rice", "fish", "beef", "githeri", "pork")

# use a loop to print each food the restaurant offers
for food in foods:
    print(food)

# try to modify one of the items 
#  foods[2] = "chicken"
'''
Traceback (most recent call last):
  File "/home/antonnym/Documents/python/Tuples/dimensions.py", line 47, in <module>
    foods[2] = "chicken"
TypeError: 'tuple' object does not support item assignment
'''

# resturant changes its menu, replacing two of the items.
foods = ("rice", "chicken", "beef", "fries", "pork")
print("\nModified menu:")
for food in foods:
    print(food)


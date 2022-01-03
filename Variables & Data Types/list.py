# list - Collection of items in a particular order
# indicated using ([]) square brackets. 
# can contain multiple data types

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# accessing elements in a list
# list are ordered collections, index position starts at 0, not 1

print(bicycles[0]) # pull out the first bicycle in the list

# using string methods
print(bicycles[0].title()) # pull out first bicycle in the list including title() method

print(bicycles[1]) # pull out second item in the list

# negative indexing - accessing last element in the list
# starts at index -1
print(bicycles[-1]) # pull out last bicycle in the list

# using individual values from a list

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# try it yourself
# names: store the names of a few friends in a list called names
# print each person's name by accessing each element in the list, one at a time
friends = ["Karen", "Kevin", "Vickie", "Yvonne", "Tabeel"]
print(friends[0]) # pull out Karen
print(friends[1]) # pull out Kevin
print(friends[2]) # pull out Vickie
print(friends[3]) # pull out Yvonne
print(friends[-1]) # pull out Tabeel

# greetings: Print a message to your friends 
# message should be the same 
msg = f"Holla {friends[0]}! You are an awesome friend!"
print(msg)

# Modifying Elements in a list
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# change the value of the first item 
motorcycles[0] = "ducati"
print(motorcycles)

# adding elements to a list
motorcycles.append('honda') # append() method adds an item at the end of the list
print(motorcycles)

# append() method makes it easy to build lists dynamically.
motor_cycles = [] # an empty list

# adding items to the list using a series of append() calls
motor_cycles.append('honda')
motor_cycles.append('yamaha')
motor_cycles.append('suzuki')

print(motor_cycles) 
# building lists this way is very common, because you often won't know the data your users want to store in a program 
# until after the program is running 

# Inserting Elements into a list 
# add a new element at any position in the list using the insert() method
motor_cycles.insert(0, 'ducati') # inserts the value 'ducati' at the beginning of the list
# shifts every other value in the list one position to the right
print(motor_cycles) 

motor_cycles.insert(2, 'bmw') # inserts the value 'bmw' as the third item in the list
print(motor_cycles)

# Removing Elements from a list
# Using del statement to remove an item from a list when the item's position is known

del motor_cycles[3] # remove item 'yamaha'
print(motor_cycles)

# once removed, the value can not be accessed

# removing an item using the pop() Method
# pop() method removes the last item in a list, but it lets you work with an item after removing it
motors = ['honda', 'yamaha', 'suzuki']
print(motors)

popped_motor = motors.pop()
print(motors)
print(popped_motor)

# use pop() method to print a statement about the last motorcycle 
motors = ['honda', 'yamaha', 'suzuki']
last_owned = motors.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# pop() to remove an item from any position in a list by including the index of the item
first_owned = motors.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
# each time pop() is used, the item worked with is no longer stored in the list
# When you want to delete an item from a list and not use the item in any way, use the del statement
# If you want to use an item as you remove it, use the pop() method
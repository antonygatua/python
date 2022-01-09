# Dictionary is a collection of key-value pairs. 
# Each key is connected to a value and can use a key to access the value associated with that key
# disctionary is wrapped in {} with key separated from values using a :
# key-value pair are separated by a comma

alien_0 = {'color': 'green', 'points':5}

print(alien_0)

# accessing values in a Dictionary
# getting value associated with a key, give the name of the dictionary and 
# place the key inside a set of square brackets
print(alien_0['color'])
print(alien_0['points'])

# Adding New Key-Value Pairs
# Dictionaries are dynamic structures - can add new key-value pairs to a dictionary at any time.
# Elements appear in the same order in which they were added to the dictionary

alien_0['x_position'] = 0 # adding new key-value pair
alien_0['y_position'] = 25
print(alien_0)

# starting with an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# modifitying values in a dictionary
# changing alien color from green to yellow 
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'Yellow'
print(f"\nThe alien is now {alien_0['color']}")

# track the position of an alien that can move at different speeds. 
# store a value representing the alien's current speed 
# use it to determine how far to the right the alien should move

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# move the alien to the right
# determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# the new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Removing Key-Value Pairs using del
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points'] # delete the key 'points' from the dictionary and remove value associated
print(alien_0)

# deleted key-value pair is removed permanently





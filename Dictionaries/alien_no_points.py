# Using get() to access values
# Using keys in square brackets to retrieve the value you're interested in from a dictionary
# returns an error if the key doesn't exist

alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

'''
Traceback (most recent call last):
  File "/home/antonnym/Documents/python/Dictionaries/alien_no_points.py", line 6, in <module>
    print(alien_0['points'])
KeyError: 'points'
'''

# can use the get() method to set a default value that will be returned if the requested key doesn't exist
# get() method requires a key as a first argument
# second optional argument can pass the value to be returned

point_value = alien_0.get('points', 'No point value assigned')
print(point_value)

# if key exists you'll get the corresponding value

point_value = alien_0.get('color')
print(point_value)
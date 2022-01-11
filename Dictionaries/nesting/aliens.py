# nesting - Sometimes you'll want to store multiple dictionaries in a list
# or a list of items as a value in a dictionary
# List of dictionaries

# create three dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# store each dictionary in a list
aliens = [alien_0, alien_1, alien_2]

# loop through the list and print out each alien
for alien in aliens:
    print(alien)
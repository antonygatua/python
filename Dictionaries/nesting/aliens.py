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

# Try it userself
# People - Create a dictionary representing of people with first_name, last_name, age and city
# make more dictionaries representing different people, store all three dictionaries in a list called people
# loop through the list of people and print 
person_0 = {'first_name': 'antonny', 'second_name': 'muiko', 'age': 15, 'city': 'kitale'}
person_1 = {'first_name': 'rose', 'second_name': 'shiro', 'age': 20, 'city': 'nanyuki'}
person_2 = {'first_name': 'yvonne', 'second_name': 'gachara', 'age': 21, 'city': 'nairobi'}

people = [person_0, person_1, person_2]

for person in people:
    for user, user_info in person.items():
        if type(user_info) == int:
            print(f"{user.title()}: {user_info}")
        else:
            print(f"{user.replace('_',' ').title()}: {user_info.title()}")
    print("\n")
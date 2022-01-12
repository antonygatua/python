# can nest a dictionary inside another dictionary
# code can get complicated quickly when you do.
# Example - Several users for a website, each with a unique username, you can store the usernames as the keys in a dictionary
# store information about each user by using a dictionary as the value associated with their user name
# define a dictionary where the value associated with each key is a dictionary
# values dictionary contains user's first name, last name, and location.
users = {
    'aeinstein': {
        'first':'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

}

# loop through the users dictionary, assign each key to variable username 
# dictionary associated with each username is assigned to variable user_info
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    # accessing the inner dictionary
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
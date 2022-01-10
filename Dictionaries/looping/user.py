# Looping through All key-value pairs
# consider the following dictionary

user_0 = {
    'username': 'antonny',
    'first': 'muiko',
    'last': 'gatua'
}

# looping through the dictionary
# name of dictionary followed by method items(), returns a list of key-value pairs
for key, value in user_0.items(): # for k, v in user_0.items()
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# looping through all the keys in a dictionary
# keys() method is useful when you don't need to work with all of the values in a dictionary.

for name in favorite_language.keys(): # pull all the keys from the dictionary and assign one at a time to the variable name
    print(name.title())

# access value associated with any key you care about inside the loop by using the current key
friends = ["phil", "sarah"]
for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# use keys() method to check if key in dictionary
if 'erin' not in favorite_language.keys():
    print("Erin, please take our poll!")

# Looping through a dictionary's keys in a particular order
# looping through a dictionary returns the items in the same order they were inserted 
# using sorted() function to get a copy of the keys in order:

for name in sorted(favorite_language.keys()): # sorted() function wrapped around the dictionary.keys() method.
    print(f"{name.title()}, thank you for taking the poll.")

# looping through all values in a dictionary
# values() method returns a list of values without any keys.
print("\nThe following langauages have been mentioned:")
for language in favorite_language.values():
    print(language.title())

# pulls all values from the dictionary without checking for repeats
# use set to avoid repition of values
# set is a collection in which each item must be unique

print("\nThe following langauages have been mentioned:")
for language in set(favorite_language.values()):
    print(language.title())


# try it yourself
# rivers: make a dictionary containing three major rivers and the country each river runs through
rivers = {'nile': 'egypt', 'tana': 'Kenya', 'zambezi': 'zambia'}

# use a loop to print the name of each river included in the dictionary
print("\nNames of river mentioned are: ")
for river in rivers.keys():
    print(river.title())

# use a loop to print the name of each country included in the dictionary
print("\nNames of the countries: ")
for country_name in rivers.values():
    print(country_name.title())

# Polling - Make a list of people who should take the favorite languages poll
# iclude some names that are already in the dictionary and some that are not
polling_list = ['jen', 'james', 'peter', 'jomo', 'phil']

# Loop through the list of people who should take the poll
# if they have already taken the poll, print a message thanking them for responding.
# if they have not yet taken the poll, print a message inviting them to take the poll.

for name in polling_list:
    if name in sorted(favorite_language.keys()):
        print(f"Thank you {name.title()} for taking the poll.")
    else:
        print(f"Hello {name.title()}, you are invited to take the poll.")
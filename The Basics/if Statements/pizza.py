# using if statements with lists
# checking for special items

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

# what if the pizzeria runs out of green peppers

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green pepper right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

# checking that a list is not empty
# check whether the list or requested toppings is empty before building the pizza

requested_toppings = []

# when name of a list is used in an if statement, python returns True if the list contains at least one item;
# an empty list evaluates to false
if requested_toppings: 
    for requested_topping in requested_toppings:
        print(f"\nAdding {requested_topping}.")
    print("\nFinished making your pizza")
else:
    print("\nAre you sure you want a plain pizza?")

# using Multiple lists
# list of available toppings
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]

# list of toppings requested by customer 
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings: # check if requested toppings is actually in the list of available toppings
    if requested_topping in available_toppings: # add that topping to pizza
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.") # unavailable toppings

print("\nFinished making your pizza!")

# Try it yourself
# Hello Admin: Make a list of five or more usernames, including the name "admin".
# if the username is "admin", print a special greeting 
# otherwise, print a generic greeting

users = ["michelle", "kev", "admin", "karen", "tabeel"]

for user in users:
    if user == "admin":
        print(f"Hello {user.title()}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")
    
# no users: Add an if test to hello_admin.py to make sure the list of users is not empty
# if the list is empty, print the message we need to find some users!
# remove all of the usernames from your list, and make sure the correct message is printed
web_users = []

if web_users:
    for user in web_users:
        if user == "admin":
            print(f"\nHello {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("\nWe need to find some users!")

# checking usernames:
# make a list of five or more usernames called current_users

current_users = ["wandalash", "nkuhanchere", "baby elephant", "ruthie", "fwafwa", "Lanky"]

# make another list of five usernames called new_users. 
# Make sure one or two of the new usernames are also in the current_users list

new_users = ["muiks", "fwafwa", "ruthie", "top shelf", "lanky"]

# loop through new_users list to see if each username has already been used.
# if it has, print message that the person will need to enter a new username.
# if a username has not been used, print a message saying that the username is available

for new_user in new_users:
    if new_user in current_users:
        print(f"\nThe username '{new_user}' exists. Please try a different username")
    else:
        print(f"\nWelcome {new_user}")

# make sure your comparison is case sensitive
users = []

for user in current_users:
    users.append(user.lower())
    
for new_user in new_users:
    if new_user in users:
        print(f"\nThe username '{new_user}' exists. Please try a different username")
    else:
        print(f"\nWelcome {new_user}")

# Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd.
# Most ordinal numbers end in th, except 1,2, and 3
# store the numbers 1 through 9 in a list
numbers = [1,2,3,4,5,6,7,8,9]

# loop through the list
# use an if-elif-else chain inside the loop to print the proper ordinal ending for each number 
for number in numbers:
    if number == 1:
        print(f"\n{number}st.")
    elif number == 2:
        print(f"\n{number}nd.")
    elif number == 3:
        print(f"\n{number}rd.")
    else:
        print(f"\n{number}th.")
# runs as long as a ceratin condition is true
# use a while loop to count up through a series of numbers 

from email import message

from click import prompt


current_number = 1 # assigning current_number the value 1
while current_number <= 5: # creating a condition
    print(current_number)
    current_number += 1

# Using a Flag
# What about more complicated programs in which many different events could cause the program to stop runing?
# Trying to test many possible events that might cause the program to stop all in 
# one while statements becomes complicated and difficult
# define one variable that determine whether or not an entire program is active

active = True
while active:
    
    message = input("Enter word: ")

    if message == 'quit':
        active = False
    else:
        print("You guessed wrong, try again!")
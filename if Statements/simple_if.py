# Simple If statements 
# has one condition
# syntax
'''
if conditional_test:
    do something
'''
# if the conditional test evaluates to true, python excutes the code following the if statement
# if the test evaluates to False, python ignores the code following the if statement.

age = 19

if age >= 18:
    print("you are old enough to vote!")
    # can have many lines of code as you want in the block follwing the if statement
    print("Have you registered to vote yet?")

# Try it yourself
# create a variable called alien_color and assign it a value of green, yellow or red
# Write an if statement to test whether the alien's color is green. 
# If it is, print a message that the player just earned 5 points
# write one version of this program that passs the if test and and another that fails
# The version that fails will have no output.

alien_color = "green"

alien_shot = "green"

if alien_shot == alien_color:
    print("You just earned 5 points")

alien_shot = "blue"

if alien_shot == alien_color:
    print("you just earned 5 points") # Fails and has no output.


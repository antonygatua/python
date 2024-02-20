# if-else is similar to a simple if statement
# else statement allows you to define an action or set of actions that are executed when the conditional test fails

age = 17
if age >= 18:
    print("you are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# if the test evaluates to False, the else block is executed.

# try it yourself
# choose a color for an alien 
# write an if-else chain if the alien's color is green, print a statement that the player just earned 5 points for shooting the alien
# if the alien's color isn't green, print a statement that the player just earned 10 points
# write one version of this program that runs the if block and another that runs the else block

alien_color = "green"

alien_shot = "green"

if alien_shot == alien_color:
    print("\nyou just earned 5 points")
else:
    print("\nyou just earned 10 points")

alien_shot = "red"

if alien_shot == alien_color:
    print("\nyou just earned 5 points")
else:
    print("\nYou just earned 10 points.")
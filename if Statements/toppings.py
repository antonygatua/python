# Testing Multiple Conditions
# if-elif-else chain is powerful, but it's only appropriate to use when just one tested is need to pass.
# Sometimes its important to check all of the conditions of interest.
# in this case, should use a series of simple if statements with no elif or else blocks
# Request a two-topping pizza

requested_toppings = ["mushrooms", "extra cheese"]

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza!")

# because every condition in this example is evaluated, both mushrooms and extra cheese are added to the pizza
# code would not work properly if we used an if-elif-else block


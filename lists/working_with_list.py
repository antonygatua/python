# looping through an entire list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# doing more within a loop
# print a mesage to each magician
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

# can also write as many lines of code as you like in the for loop
for magician in magicians:
    print(f"{magician.title()}, that was a great magic trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# doing something after a loop
# any line of code after the loop that are not indented are executed once without repetition
for magician in magicians:
    print(f"{magician.title()}, that was a great magic trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

# avoiding indentation errors - common errors include
# forgetting to indent
# forgetting to indent additional lines
# indenting unnecessarily
# indenting unnecessarily after the loop
# forgetting the colon

# try it yourself
# pizzas: Think of atleast three kinds of your favorite pizza
# srore these pizza names in a list, and then use a for loop to print the name of each pizza
pizza_list = ["Chicken Hawaiian", "Cheese Burger", "Meat Deluxe", "Chicken Macon BBQ", "Chicken & Beef Pepperoni"]

for pizza in pizza_list:
    print(pizza)

# modify the loop to print a sentence using the name of the pizza
for pizza in pizza_list:
    print(f"I like {pizza} pizza.")

# add a line at the end of your program, outside the loop
for pizza in pizza_list:
    print(f"I like {pizza} pizza.")
print("I really like Pizza")
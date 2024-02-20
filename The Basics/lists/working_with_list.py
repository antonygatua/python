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

# Try it yourself
# counting to twenty: Use a for loop to print numbers from 1 to 20
for number in range(1, 21):
    print(number)

# Threes: Make a list of the multiples of 3 from 3 to 30.
three_multiples = []
for numbers in range(3, 31, 3):
    three_multiples.append(numbers)

print(three_multiples)

# cubes: A number raised to the power of 3
# make a list of the first 10 cubes and use a loop to print out each value
cubes = []
for cube in range(1,11):
    print(cube**3)
    cubes.append(cube**3)

print(cubes)
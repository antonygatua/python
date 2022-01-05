# Programming often involves examining a set of conditions and 
# deciding which action to take based on those conditions
# If statement allows you to examine the current state of a program and respond appropriately to that state

# example

cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# Loop first checks if the current value of car is 'bmw'.
# If it is, the value is printed in uppercase. 
# If the value of car is anything other than "bmw", it's printed in title case

# Conditional Test
# at the heart of every if statement is an expression that can be evaluated as 
# True or False and is called a conditional test
# Python uses values True and False to decide whether the code in an if statement should be executed
# if True python executes the code following the if statement
# if false python ignores the code following the If statement

# Checking for equality
car = 'bmw' # set the value of car to 'bmw'
print(car == 'bmw') # check whether the value of the car is 'bmw'

# (==) Equality operator returns True if the values on the left and right side of the 
# operator match

car = "audi"
print(car == 'bmw')

# Ignoring case when checking for equality 
# Testing for equality is case sensitive in python

car = 'Audi'
print(car == 'audi')

print(car.lower() == 'audi')

# checking for inequality using (!=)
requsted_topping = "mushrooms"

if requsted_topping != "anchovies":
    print("Hold the anchovies!")

# numerical comparisons
age = 18 
print(age == 18)

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again")

# can include various mathematical comparisons in your conditional statemenets
age = 19

print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

# checking Multiple conditions
# using and to check multiple conditions
# used to check whether two conditions are both True simultaneously.
# if either test fails or if both tests fails, the expression evaluates to false

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# using or to check Multiple conditions
# passes when either or both of the individual test pass
# fails when both individual test fail

age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

# checking whether a value is in a list
requsted_toppings = ["mushrooms", "onions", "pineapple"]

out_1 = "mushroom" in requsted_topping
print(out_1)

out_2 = "pepperoni" in requsted_topping
print(out_2)

# checking whether a value is not in a list
banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

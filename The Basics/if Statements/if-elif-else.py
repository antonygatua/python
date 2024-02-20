# If-elif-else chain
# more than two possible situations
# excute only one block
# when a test passes, the code following that test is excuted. 

# example
# admission for anyone under age 4 is free
# admission for anyone between the ages of 4 and 18 is $25.
# admission for anyone age 18 or older is $40.

age = 12

if age < 4:
    print("your admission cost is $0.")
elif age < 18:
    print("your admission cost is $25.")
elif (age == 18) and (age > 18):
    print("your admission cost is $40.")
else:
    print("please try again")

# using Multiple elif blocks 
# can use as many elif blocks in your code as you like 
# anyone older 65 or older pays half the regular admission.

age = 67

if age < 4:
    print("your admission cost is $0.")
elif age < 18:
    print("your admission cost is $25.")
elif (age == 18) or (age > 18):
    print("your admission cost is $40.")
elif (age == 65) or (age > 65):
    print("your admission cost is $20.")
else:
    print("please try again")

# Omitting the else Block
# python does not require the else block at the end of an if-elif chain
# sometimes an else block is useful;

age = 48

if age < 4:
    print("your admission cost is $0.")
elif age < 18:
    print("your admission cost is $25.")
elif (age == 18) or (age > 18):
    print("your admission cost is $40.")
elif (age == 65) or (age > 65):
    print("your admission cost is $20.")

# write an if-elif-else chain that determines a person's stage of life.
# set a value for the variale age, and then:
# if the person is less than 2 years old, print a message that the person is a baby
# if the person is atleast 2 years old but less than 4, print a message that the person is a toddler
# if the person is atleast 4 years old but less than 13,print message that the person is a kid
# if the person is atleast 13 years old but less than 20, print a message that the person is a teenager
# if the person is atleast 20 years old but less than 65, print message that the person is an adult
# if the person is age 65 or older, print a message that the person is an elder

age = 23

if age < 2:
    print("person is a baby")
elif (age == 2) or (age < 4):
    print("person is a toddler")
elif (age == 4) or (age < 13):
    print("person is a kid")
elif (age == 13) or (age < 20):
    print("person is a teenager")
elif (age == 20) or (age < 65):
    print("person is an adult")
elif (age > 65):
    print("person is an elder")
else:
    print("Enter the correct age.")
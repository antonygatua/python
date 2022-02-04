# input() - allows user to enter some text
message = input("Tell me something, and I will repeat it back to you: ")
print(message) 

# Try it yourself
# rental car:Write a program that asks the user what kind of rental car they would like 
# Print a message about that car
car = input("Enter the name of the car you want: ")
print(f"Let me see if I can find you a {car}.")

# Resturant seating: Write a program that ask the user how many people are in their dinner group
# if the answer is more than 8, print a message saying they'll have to wait for a table.
# Otherwise, report that their table is ready
resturant_seating = input("How many people are in your dinner group?")
resturant_seating = int(resturant_seating)

if resturant_seating > 8:
    print("Please wait while we fix you a table.")
else:
    print("Table is ready.")
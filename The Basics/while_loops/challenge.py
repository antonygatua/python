# Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter
# 'quit' value. As they enter each topping, print a message saying you'll
# add that topping to their pizza 

user_input = "Enter Topping(s) to add to pizza:"
user_input += "\n(Enter 'quit' when finished): "

available_toppings = ["banana", "cheese", "mango", "Mushrooms", "Pepperoni"]
requested_toppings = []
active = True
while active:
    message = input(user_input)
    message.strip().lower()

    if message == 'quit':
        active = False
    else:
        if message in available_toppings:
            requested_toppings.append(message)
        else:
            print(f"{message.title()} is not available today. Available toppings are: ")
            print(available_toppings)
print(requested_toppings)



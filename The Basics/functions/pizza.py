# passing an arbitrary number of arguments 
# sometimes you won't know ahead of time how many arguments a function needs to accept

def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni")
make_pizza('mushrooms', 'green peppers', 'extra cheese')
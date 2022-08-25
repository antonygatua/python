# Keyword Arguments - name-value pair that you pass to a function 
# free from having to worry about correctly ordering the arguments in the function call

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type="dog", pet_name="scooby")
# when calling the function we explicitly tell python which parameter each argument should be matched with.
# the oder does not matter 
describe_pet(pet_name="snow",animal_type="cat")
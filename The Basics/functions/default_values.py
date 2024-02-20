# when writing a function, you can define a default value for each parameter
def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='willie')
# when you define a default value you can exclude the corresponding argument 

# describing an animal other than a dog
describe_pet(pet_name="snow", animal_type='cat')
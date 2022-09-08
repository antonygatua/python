"""
Try It Yourself
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.

"""
class Restaurant:
    """Simulate A restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Describe the resturant"""
        print(f"\nThe restaurant {self.restaurant_name} was founded in 1982.")
        print(f"It is reknown for its {self.cuisine_type} across the Europe.")

    def open_restaurant(self):
        """Indicates the restaurant is open"""
        print(f"\nThe {self.restaurant_name} is open from 7am to 12 midnight.")

# creating an instance 
my_restaurant = Restaurant("Iroko", "French Cuisine")

print(f"My favourite restaurant is {my_restaurant.restaurant_name} and is best known for its delicious {my_restaurant.cuisine_type}")

# calling the methods
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

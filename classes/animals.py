class Animals:
    """Models aspects of animals"""
    
    def __init__(self,name, age):
        """Initialize the attributes"""
        self.name = name
        self.age = age

    def describe_animal(self):
        """Describes the animal"""
        msg = f"This is a {self.name} and its {self.age} years old."
        return msg
    
class HumanBeing(Animals):
    """Models aspects of a human being, specific to animals"""

    def __init__(self, name, age):
        """Intialize attributes of parent class
        Then intialize attributes specific to an electric car
        """
        super().__init__(name, age)

        self.scient_name = "Homo Sapien"
    
    def scientific_name(self):
        """Describe their scientific name"""
        print(f"Human beings are {self.scient_name}.")
        

my_person = HumanBeing("Antonny", 14)
print(my_person.describe_animal())
my_person.scientific_name()

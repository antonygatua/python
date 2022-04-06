# Removing all instances of specific values from a list 
# cars in the showroom 
cars = ["subaru", "toyota", "nissan", "porche", "suzuki", "renault"]

while 'toyota' in cars:
    cars.remove('toyota')

print(cars)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)
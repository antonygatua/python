# A list in a Dictionary
# store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t"+ topping)

# favourite languages
# value associated with each key is a list
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")

# refine using if statement
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is: ")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite languages are: ")
        for language in languages:
            print(f"\t{language.title()}")

# try it yourself
# Favorite places - Make a dictionary called favorite_places 
favorite_places = {
    'jomo': ['beach', 'park', 'ocean'],
    'muiko': ['desert', 'reserve', 'river-bank'],
    'ruthie': ['park', 'national park', 'nature trails'],
}

for name, favorite_place in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are: ")
    for place in favorite_place:
        print(f"\t{place.title()}")
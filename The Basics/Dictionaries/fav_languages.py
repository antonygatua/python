# A dictionary of similar Objects 
# use a dictionary to store one kind of information about many objects

favorite_langauges = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

language = favorite_langauges['sarah'].title()
print(f"Sarah's favorite langauage is {language}.")

# Try It yourself
# Person: Use a dictionary to store information about a person you know
# store their first name, last name, age and the city in which they live in.
# print each of information stored in the dict

person = {
    'first_name': 'ruth',
    'second_name': 'jomo',
    'age': 24,
    'city': 'nairobi'
}

first_name = person['first_name'].title()
second_name = person['second_name'].title()
age = person['age']
city = person['city'].title()

print(f"My name is {first_name} {second_name}, {age} years old from {city}.")

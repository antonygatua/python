# list - Collection of items in a particular order
# indicated using ([]) square brackets. 
# can contain multiple data types

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# accessing elements in a list
# list are ordered collections, index position starts at 0, not 1

print(bicycles[0]) # pull out the first bicycle in the list

# using string methods
print(bicycles[0].title()) # pull out first bicycle in the list including title() method

print(bicycles[1]) # pull out second item in the list

# negative indexing - accessing last element in the list
# starts at index -1
print(bicycles[-1]) # pull out last bicycle in the list

# using individual values from a list

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# try it yourself
# names: store the names of a few friends in a list called names
# print each person's name by accessing each element in the list, one at a time
friends = ["Karen", "Kevin", "Vickie", "Yvonne", "Tabeel"]
print(friends[0]) # pull out Karen
print(friends[1]) # pull out Kevin
print(friends[2]) # pull out Vickie
print(friends[3]) # pull out Yvonne
print(friends[-1]) # pull out Tabeel

# greetings: Print a message to your friends 
# message should be the same 
msg = f"Holla {friends[0]}! You are an awesome friend!"
print(msg)
# slice - specific items in a list
# to make a slice, you specify the index of the first and the last elements you want to work with 
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3]) # the first three players

print(players[1:4]) # start slice at index 1 and end at index 4

print(players[:4]) # python automatically starts your slice at the beginning of the list

print(players[2:]) # all the items from the third item through the last item

print(players[-3:]) # last three players on the roster

# looping through a slice
# loop through the first three players and print their names 

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


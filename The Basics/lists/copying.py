# Copying a list
# start with an existing list and make an entirely new list based on the first one
# make a slice that includes the entire original list by omitting the first index and the second index([:])
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("my favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

# add new food to each list 
# recall append and insert
my_foods.append("cannoli")

friend_foods.insert(0, "fries")

print(my_foods)

print(f"\n{friend_foods}")

# this doesn't work
# friend_food = my_foods 
# associates the new variable friend_food with the list that is already associated with my_foods, so now both variables point to the same list
# adding cannoli to my_food will also appear in friend_food.
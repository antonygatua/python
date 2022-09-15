# writing to an empty file
filename = "programming.txt"

with open(filename, 'w') as file_object:
    file_object.write("\nI love programming.\n")
    """Writing Multiple Lines"""
    file_object.write("I love creating new games.\n")

# read the file
with open(filename, 'r') as file_object:
    content = file_object.read()
print(content)

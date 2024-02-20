# Appending to a file
# if you want to add content to a file instead of writing over existing content, you can open the file in append mode
# In append mode python doesn't erase the contents of the file before running the file object

filename = "programming.txt"

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")


# reading the file
with open(filename) as file_object:
    contents = file_object.read()

print(contents)
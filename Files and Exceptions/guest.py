# Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt

def get_user_name():
    """A simple function to get the name of a user"""
    first_name = input("Enter your first name: ")
    second_name = input("Enter your second name: ")
    combined_names = f"{first_name.title()} {second_name.title()}"

    return combined_names

# add name to guest.text
filename = "guest.txt"
with open(filename, 'w') as file_object:
    file_object.write(get_user_name())

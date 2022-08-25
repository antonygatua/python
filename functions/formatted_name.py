# Function doesn't have to display its output directly 
# Instead it can process some data and the return a value or set of values
# value a function returns is called a return value

def get_formatted_name(first_name, second_name):
    """Return a full name, neatly formatted"""
    full_name = (f"{first_name.title()} {second_name.title()}")
    return full_name

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
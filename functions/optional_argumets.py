# sometimes it makes sense to make an argument optional so that people using the function can chose to provide extra information only if they want to
def get_formatted_name(first_name, last_name, middle_name = ''): # non-default arguments follows default arguments
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = (f"{first_name} {middle_name} {last_name}")
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name("salim", "wanjiku", "junior")
print(musician)
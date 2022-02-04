# break statement - used to exit a while loop immediately without running any remaining code in the loop regardless of the result of any conditional test
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit when you are finished.)"

while True: # loop that starts with while True will run forever unless it reaches a break statement
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
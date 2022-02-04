# use continue statement to return to the beginning of the loop based on the result of a conditional test
# consider a loop that counts from 1 to 10 but only prints the ODD number 

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)
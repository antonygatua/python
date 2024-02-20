try:
    with open('file.text', 'r') as file:
        lines = file.readlines()
except:
    print('couldnt open file.txt')

try:
    with open('file.txt', 'r') as file:
        lines = file.readlines()
except FileNotFoundError as fnf_error:
    print(fnf_error)
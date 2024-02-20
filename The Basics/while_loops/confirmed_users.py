# moving items from one list to another 
# list of unconfirmed users
from locale import currency


unconfirmed_users = ['alice', 'brian', 'candace', 'antonny']
confirmed_users = []

i = 0

while 1 <= len(unconfirmed_users):
    current_user = unconfirmed_users.pop()

    confirm_prompt = f"\nVerify {current_user}?"
    confirm_prompt += "\n(yes or no): "

    if input(confirm_prompt) == "yes":
        confirmed_users.append(current_user)

# display users 
for user in confirmed_users:
    print(user)
    
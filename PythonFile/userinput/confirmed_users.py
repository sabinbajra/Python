confirmed_users = []
unconfirmed_users = ['ram', 'shyam', 'hari', 'gita', 'manoj', 'regan']

while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print(f"Verifying users: {current_users.title()}")
    confirmed_users.append(current_users)

#display all confirmed users
for users in confirmed_users:
    print(f"The user {users.upper()} is confirmed")

print(confirmed_users)
print(unconfirmed_users)
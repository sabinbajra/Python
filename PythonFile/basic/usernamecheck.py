current_users = ['ram', 'shyam', 'hari', 'gita']
new_users = ['rita', 'sita', 'gita', 'ram','biki']

for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} is already taken, please use different name")
    else:
        print(f"New user {new_user} successfully created")

print("User List all checked")

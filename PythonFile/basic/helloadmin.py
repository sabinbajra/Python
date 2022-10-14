#users = ['ram','sabin','admin','staff','librarian']
users = []

if users:
    for user in users:
        if user.lower() == 'admin':
            print(f"Welcome {user}, Do you want to do administrative task.")
        else:
            print(f"Hello {user} welcome back to our website")
else:
    print("We need to find some users")


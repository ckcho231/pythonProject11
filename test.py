# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

print(users.items())

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

    print(users)

# Strategy:  Create a new collection
active_users = {}

print(users.items())
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

    print(user, status)


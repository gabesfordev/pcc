usernames = ['david', 'alice', 'admin', 'bob', 'zed']

for user in usernames:
    if user == 'admin':
        print(f'Hello {user}, would you like to see a status report?')
    else:
        print(f'Hello {user}')
username = input('What is your username: ')
password = input('What is your password: ')

hashed = '*'
user_info = f'Your username is {username} and your password is {len(password) * hashed}'
print(user_info)
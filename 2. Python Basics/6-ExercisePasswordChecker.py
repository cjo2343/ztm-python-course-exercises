# Exercise Password Checker

username = input('Enter your username:\t')
password = input('Enter you password:\t')

secret_password = len(password) * '*'
print(f'Hey {username}, your password {secret_password} is {len(password)}  letters long.')



username = input('What is your username?')
password = input('Write your password')

password_length = len(password)
secret_pw = '*' * password_length

sentence = (f'Hello, {username}, your password {secret_pw} has been accepted. It is {password_length} characters long.')
print(sentence)
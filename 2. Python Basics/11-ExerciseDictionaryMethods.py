# Exercise Dictionary Methods
# Scroll to see answers.

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

user = {

'username' : input('Type your username'),
'age' : input('Enter your age'),
'weapons' : ['ak47', 'machette', 'small knife'],
'is_active' : True,
'clan' : input('Enter the name of your clan!')

}
print(user)

#Creating an empty dict: 

user_profile = {
    'age': 0,
    'username': ' ',
    'weapons': None,
    'is_active': False,
    'clan': None
}

# 2 iterate and print all the keys in the above user.

#Version 1
for key in user.keys():
    print(f'- {key}')

#Version 2
print(user.keys())

# 3 Add a new weapon to your user
user['weapons'].append('bat')

# 4 Add a new key to include 'is_banned'. Set it to false
user.update[{'is_banned' : False}]

# 5 Ban the user by setting the previous key to True
user.update[{'is_banned' : True}]

# 6 create a new user2 by copying the previous user and update the age value and username value.

user2 = user.copy()
user2.update[{'username' : 'DarthVaider'}, {'age' : 33}]
print(user2)


#ANSWERS BELOW:























# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user_profile = {
    'age': 0,
    'username': ' ',
    'weapons': None,
    'is_active': False,
    'clan': None
}

# 2 iterate and print all the keys in the above user.
print(user_profile.keys())

# 3 Add a new weapon to your user
user_profile['weapons'] = 'Katana'

# 4 Add a new key to include 'is_banned'. Set it to false
user_profile.update({'is_banned': False})

# 5 Ban the user by setting the previous key to True
user_profile['is_banned'] = True

# 6 create a new user2 my copying the previous user and update the age value and username value.
user2 = user_profile.copy()
user2.update({'age': 50, 'username': 'User2'})
print(user_profile)
print(user2)

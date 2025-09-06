# #fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
# friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

# print(friends)

# new_friend = ['Stanley']
# print(new_friend)



# combined_friendlist = (sorted(friends) + new_friend)

# print(combined_friendlist)















































# # Solution: (keep in mind there are multiple ways to do this, so your answer may vary. As long as it works that's all that matters!)
# # friends.extend(new_friend)
# # print(sorted(friends))


# basket_man = [1,2,3,4,5,6]
# tennis_man = [15, 30, 40]

# basket_man.extend(tennis_man)
# print(basket_man)


# user = {

# 'name': 'Christian',
# 'age': '31',
# 'gender': 'male',
# 'Like sports?': True

# }

# print(user.items())
# # Output: dict_items([('name', 'Christian'), ('age', 30)])

# for key, value in user.items():
#     print(f"- {key}: {value}")
# # Output:
# # - name: Christian
# # - age: 30


my_userlist = [
{ 
'name': 'Christian',
'age': 31,
'fav_soccerteam': ['FC Barcelona', 'OB'],
'gender': 'male'
},
{ 
'name': 'Jonathan',
'age': 28,
'fav_soccerteam': ['Brøndby'],
'gender': 'male'
} 
]

temp_list = my_userlist[0]
print('age' in temp_list)

# print(my_userlist)
# print(my_userlist[0]['name'])
# get_dict = (my_userlist[0])
# temp_name = get_dict.get('name')
# print(temp_name)

# user_man = [ 1, 2, 'i']
# print(1 in [user_man])

# user = {

# 'name' : 'Christian',
# 'age' : 31,
# 'gender' : 'male'

# }

# user.clear()
# print(user)

# user = {

# 'name' : 'Christian',
# 'age' : 31,
# 'gender' : 'male'

# }

# user.update({'hometown' : 'Copenhagen'})
# print(user)

user = {

'username' : input('Type your username'),
'age' : input('Enter your age'),
'weapons' : ['ak47', 'machette', 'small knife'],
'is_active' : True,
'clan' : input('Enter the name of your clan!')

}

#user.update({'weapons' : [3].append(bat)})
#user['weapons'].append('bat')
#user['weapons'].remove('ak47')
#print(user.get('weapons'))
#print(user.values())
# for key in user.keys():
#     print(f'- {key}')

# print(user.keys())

user2 = user.copy()
user2.update[{'username' : 'DarthVaider'}]
user2.update[{'age' : 33}]
print(user2)
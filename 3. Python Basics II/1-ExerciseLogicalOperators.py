# # Exercise Logical Operators

is_magician = False
is_expert = True
 
# Check if magician and expert: "you are a master magician"
if is_magician and is_expert:
    print('You are a master magician')


# Check if magician but not expert: "at least you're getting there"

elif not is_magician and is_expert:
    print('At least you\'re getting there')


# Check if not a magician: "You need magic powers"
elif not is_magician:
    print('You need magic powers!')

# is_old = True
# is_licensed = False

# if is_old and is_licensed:
#     print('You are old enough, and you have a valid driver license!')
# elif is_old and not is_licensed:
#     print('You are old enough, but you do not have a valid driver license!')



# is_raining = True
# is_cold = True

# if is_raining:
#     print("Remember to take an umbrella.")  # This line is part of the 'if' block.
    
#     if is_cold:
#         print("And wear a warm coat.")   # This line is part of the 'if is_cold' block.
    
#     print("Stay dry!")                     # This line is also part of the first 'if' block.

# print("Have a nice day!")  

# is_old = True
# is_licensed = False
# is_test = True

# if is_old and is_licensed:
#     print('You are old enough, and you have a valid driver license!')
# elif is_old and not is_licensed:
#     print('You are old enough, but you do not have a valid driver license!')
# print('hej med dig!')

print([] == [])
print ('' == 1)

age = ""
while not age.isdigit():
    age = input("Please enter your age as a number: ")

print(f"Thank you! Your age is {age}.")

for item in [1,2,3,4,5]:
    for item2 in ['a','b','c']:
        print(item, item2)
        
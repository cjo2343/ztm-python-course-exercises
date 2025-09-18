# Exercise Find Duplicates
# Check for duplicates in the list.
# Print the characters which have duplicates in the list.

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []


for element in some_list: 
    print(f'Checking {element}')
    if some_list.count(element) > 1:
            duplicates.append(element)
            print(f' Added {element} to the duplicate list!')
print(duplicates)



x = 0 
while x < 5:
    print(x)
    x += 1

my_list = ['Chris', 'Martin', 'Grethe', 'Hans']
i = 0
while i < len(my_list):
    print(f' The index of {my_list[i]} is: {i}')
    i +=1


# while True: 
#     response = input('Say something: ')
#     if (response== 'bye'):
#         break

# Stop looping as soon as we find a number larger than 5
for number in [1, 3, 8, 2, 9]:
    if number > 5:
        print(f"Found a number larger than 5: {number}")
        break # Exit the loop now
    print(f"Checking {number}...")
print('this line is the first outside the for loop - see the indentation')
























# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)

# print(duplicates)

# for i in range(len(some_list)):
#     for j in range(i+1, len(some_list)):
#         if some_list[i] == some_list[j]:
#             duplicates.append(some_list[i])
#
# print(duplicates)
#
#
#
# duplicates = set()
#
# list_set = set(some_list)
#
# for char in list_set:
#     count = 0
#     for item in some_list:
#         if item == char:
#             count += 1
#     if count > 1:
#         duplicates.add(char)
#
# print(duplicates)

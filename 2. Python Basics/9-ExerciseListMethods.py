# Exercise List Methods
# SCROLL FOR ANSWERS!
# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove the Banana from the list
#basket.remove('Banana')
basket.remove('Banana')
print(basket)

# 2. Remove "Blueberries" from the list.
basket.remove('Blueberries')
print(basket)

# 3. Put "Kiwi" at the end of the list.
basket.append('Kiwi')
print(basket)

# 4. Add "Apples" at the beginning of the list
basket.insert(0,'Apples')
print(basket)

# 5. Count how many apples in the basket
print(basket.count('Apples'))

# 6. empty the basket
basket.clear()
print(basket)


print(list(range(50,100)))


basket = ["Banana", "Apples", "Oranges", "Blueberries"]
number_list = list((range(100)))
print(number_list)
combined_list = basket + number_list
print(combined_list)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list_3 = ['banan', 'dåsecola', 'lillefinger']
combined_list = list1 + list2 + list_3
print(combined_list)

mixed_list = [10, "apple", 25.5, "banana", True, 30, "cherry", 4.0]

# 1. Create empty lists
integers = []
strings = []
others = []

# 2. Loop through the mixed_list
for item in mixed_list:
    # 3. Check the type of the item
    if isinstance(item, int):
        # 4. Append to the correct list
        integers.append(item)
    elif isinstance(item, str):
        strings.append(item)
    else:
        others.append(item)

print(f"Integers: {integers}")
print(f"Strings: {strings}")
print(f"Others: {others}")

dict = {

    'a' : 1,
    'b' : 2
}
print(dict)






















# 1. Remove the Banana from the list
#basket.remove('Banana')
# 2. Remove "Blueberries" from the list.
#basket.remove('Blueberries')
# 3. Put "Kiwi" at the end of the list.
#basket.append('Kiwi')
# 4. Add "Apples" at the beginning of the list
#basket.insert(0, 'Apples')
# 5. Count how many apples in the basket
#basket.count('Apples')
# 6. empty the basket
#basket.clear()
#print(basket)

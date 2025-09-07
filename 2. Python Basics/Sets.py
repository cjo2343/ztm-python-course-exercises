# Sets

# my_set = {1, 2, 3, 4, 5, 5}
# my_set.add(100)
# my_set.add(2)
# print(my_set)

# my_list = [1, 2, 3, 4, 4, 5, 5]
# print(set(my_list))
# print(list(my_set))

# new_set = my_set.copy()
# my_set.clear()
# print(my_set)
# print(new_set)
# print('\n')


# # Set Methods

# my_set = {1, 2, 3, 4, 5}
# your_set = {4, 5, 6, 7, 8, 9, 10}

# print(my_set.difference(your_set))
# print(my_set.intersection(your_set))
# print(my_set.isdisjoint(your_set))
# print(my_set.issubset(your_set))
# print(my_set.issuperset(your_set))
# print(my_set.union(your_set))
# my_set.difference_update(your_set)
# print(my_set)
# my_set.discard(5)
# print(my_set)

my_set = {1,2,3,4,5}
print(my_set)
my_set.add(100000)
my_set.add('Hans og Grethe')
print(my_set)

my_list = [1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,4,5,6,1]
no_dup = set(my_list)
print(no_dup)

set_test = {1,2,3,4,5,65,6,6,6,6,6,4}
list_test = list(set_test)
print(list_test)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a - set_b)
set_a.difference_update(set_b)
print(set_a)
print(set_a.isdisjoint(set_b))

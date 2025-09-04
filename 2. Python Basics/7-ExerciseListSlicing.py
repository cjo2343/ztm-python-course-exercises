#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1]) #b
print(new_list[-2]) #b
print(new_list[1:3]) #b,c
new_list[0] = 'z' #changing a with z
print(new_list) # [z,b,c]

my_list = [1,2,3]
bonus = my_list + [5] #adding 5 to the bonus list
my_list[0] = 'z' #changing 1 with z
print(my_list) #[z, 2, 3]
print(bonus) # [1,2,3,0,0,0] (wrong), the correct answer is: [1,2,3,5]

list_test = [1,2,3,4, 'test']
my_best_list = list_test + ['tester']
print(list_test)
print(my_best_list)

amazon_cart = [

'Macbook laptop',
'Pencil',
'Apple iPad 11',
5000, 
'Sunglasses'
]
amazon_cart2 = (amazon_cart[2:5])

print(amazon_cart)
print(amazon_cart2)

amazon_cart2[0] = 'bike'
print(amazon_cart2)

amazon_cart = [
'laptop',
'notebook',
'pencil',
'mouse'
]

amazon_cart2 = amazon_cart[:]
amazon_cart2[0] = 'Macbook Pro 2022'
print(amazon_cart)
print(amazon_cart2)

basket = [1,2,3,4,5]
print(len(basket))

matrix = [

[1,2,3,4],
['test','Preben','Giraf'],
[5,6,4,2,1]

]

print(len(matrix[0]))
matrix.insert(2,100)
print(matrix)

basket_man = [1,2,3,4,5,6,5, 5]
basket_man.extend([100,200,300])
print(basket_man)
print(basket_man.index(3))
print(2 in basket_man)
print(basket_man.count(5))

# Exercise Tricky Counter
# Write a program to find the sum of items in the list

my_list = [1,2,3,4,5,6,7,8,9,10]
my_list2 = [1,2,3]

sum = 0
for item in my_list:
   sum =+ item

print(sum)


    
# sum starts at 0, at first iteration the sum =+ item = 0 + 1 = 1
# at second iteration, the calculation is 1 = 1 + 2 = 3
# at third iteration, the calculation is 3 = 3 + 3 = 6
# at forth iteration, the calculation is 6 = 6 + 4 = 10
# at fifth iteration, the calculation is 10 = 10 + 5 = 15
#... and so on
#The reason we place the print(sum) outside of the loop is because we only want to print the last value of the loop output






























# counter = 0
# for hej in my_list:
#     counter += hej

# print(counter)



#Guess the output of each answer before you click RUN
#Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)

print((5 + 4) * 10 / 2) # = print(9 * 5) = 45

print(((5 + 4) * 10) / 2) # = print((9 * 10) / 2) = print(90 / 2) = print(45)

print((5 + 4) * (10 / 2)) # = print((9) * (5)) = print(45)

print(5 + (4 * 10) / 2)  # = print((5) + ((40) / 2)) = print((5) + 20) = print(25)

print(5 + 4 * 10 // 2) # = print(5 + 4 * 5) = print(5 + 20) = print(20)


age = 30
print('What is your age?' + ' My age is: {age}')

iq = 190
user_age = iq/4
print(user_age)
a = user_age
print(a)

name = "Christian"
age = 30

# Using an f-string to create a sentence
sentence = f"My name is {name} and I am {age} years old."

print(sentence)

class Car:
    # Python calls this automatically when you create a Car object
    def __init__(self, color):
        print("Initializing a new car...")
        self.color = color

    # Python calls this automatically when you try to print() the object
    def __str__(self):
        return f"A beautiful {self.color} car"

# You write this:
my_car = Car("red") # Python calls __init__ in the background
print(my_car)       # Python calls __str__ in the background
car_2 = Car("black")
print(car_2)

test_1,test_2,test_3 = "hej", "farvel", "goddag"
print(test_2)

word = "Python"
first_letter = word[0]  # 'P'
last_letter = word[-1] # 'n'
print(first_letter + ' ' + last_letter)

name = "Sam"
#name[0] = "P" # This will cause a TypeError
#print(name[0])
#TypeError: 'str' object does not support item assignment
# The correct way to "change" it is to create a new string
new_name = "P" + name[1:] # new_name is "Pam"
print(new_name)

print(len('hvad så der man!!!!'))

nice_name = 'Christian.'.replace('ian','johnjohn')
print(nice_name)

print(type(str(100)))

str_number = "100"
my_int = int(str_number)
print(type(my_int + 50))

age = 30
# This would cause an error: "My age is " + age
# We must convert the integer to a string first.
message = "My age is " + str(age)
print(message)
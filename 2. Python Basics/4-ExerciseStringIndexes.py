#Guess the output of each print statement before you click RUN!
python = 'I am PYHTON'

print(python[1:4]) # am
print(python[1:]) # am PYTHON
print(python[:]) #I am PYTHON
print(python[1:100]) #IndexError -> wrong
print(python[-1]) #N
print(python[-4]) #H
print(python[:-3]) #THYP am I -> starts from the beginning (index 0) and ends at -3, which is T
print(python[-3:]) #TON
print(python[::-1]) #NOTHYP am I

numbers = "0123456789"

# Get every second number from the beginning to the end
print(numbers[1:5:2])
# Output: 02468
print(numbers[1:-1])

name = 'Sam'
name += 'i'
print(name)

#name = input('What is your name?')
#print(f'Hello, {name}!')

greet = 'hello'
print(greet[0:len(greet)])

string_method = 'let\'s flip som cards!'
print(string_method.replace('flip', 'cast'))
print(string_method)


# print(string_method.upper())

name = ['John', 'Hans', 'Mikkel']
if name:
    print(f"Hello, {name}")
else:
    print("You did not enter a name.")
# Output: You did not enter a name. (Because an empty string is Falsy)




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
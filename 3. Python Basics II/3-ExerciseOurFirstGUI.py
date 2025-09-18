#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for item in picture:
  for element in item:
    if element:
      print('*', end=(""))
    else:
      print(' ', end=(""))
  print('')
    
for item in picture:
  print(item[2])

print('Hello, world!')
print('Hello')
print('world!')




























# #Answer:
# for image in picture:
#   for pixel in image:
#     if (pixel):
#       print('*', end ="")
#     else:
#       print(' ', end ="")
#   print('')
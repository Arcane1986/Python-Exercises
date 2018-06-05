from PIL import Image
from random import randrange

img = Image.open("profile.jpg")
width = img.width
height = img.height

new_image = Image.new('RGB',[width,height])

for col in range(1,height-1):
  for row in range(1,height-1):
    
    RGB = img.getpixel((col,row))
    new_image.putpixel((col+randrange(-1,2),row+randrange(-1,2)),(RGB))

new_image.show()
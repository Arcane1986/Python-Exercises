from PIL import Image

img = Image.open("profile.jpg")
width = img.width
height = img.height

new_image = Image.new('RGB',[width,height])

for col in range(width):
  for row in range(height):
    new_red = 0
    new_green = img.getpixel((col,row))[1]
    new_blue = img.getpixel((col,row))[2]
    RGB=new_red,new_green,new_blue

    new_image.putpixel((col,row),(RGB))

new_image.show()
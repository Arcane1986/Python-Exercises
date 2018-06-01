import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
Richboy = turtle.Turtle()
Richboy.shape("turtle")
Richboy.up()
Richboy.forward(-200)
Richboy.right(90)
Richboy.forward(200)
Richboy.left(90)
Richboy.down()
for triangle in range(3):
  Richboy.color("blue")
  Richboy.forward(200)
  Richboy.left(120)
for square in range(4):
  Richboy.color("red")
  Richboy.forward(150)
  Richboy.left(90)
for hexagon in range(6):
  Richboy.color("purple")
  Richboy.forward(250)
  Richboy.left(60)
for octagon in range(8):
  Richboy.color("black")
  Richboy.forward(200)
  Richboy.left(45)
wn.exitonclick()
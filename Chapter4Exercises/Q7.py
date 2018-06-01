import turtle
wn = turtle.Screen()
wn.bgcolor("blue")
Richboy = turtle.Turtle()
Richboy.shape("turtle")
Richboy.pensize(10)
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
  Richboy.forward(100)
  Richboy.left(angle)
wn.exitonclick()
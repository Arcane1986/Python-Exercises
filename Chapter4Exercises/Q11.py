import turtle
import random
wn = turtle.Screen()
Richboy = turtle.Turtle()
Richboy.hideturtle()
Richboy.speed(20)

for i in range(360):
  Richboy.forward(i)
  Richboy.right(i)
  if i%3==0:
    Richboy.color("Red")
  if i%3==1:
    Richboy.color("Blue")
  else:
    Richboy.color("Purple")
wn.exitonclick()
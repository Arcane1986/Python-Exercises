import turtle
wn=turtle.Screen()
George=turtle.Turtle()
George.color("Blue")
wn.bgcolor("Red")
George.speed(10)

def draw_sprite(t,legs,length):
  for _ in range(legs):
    t.forward(length)
    t.forward(-length)
    t.left(360/legs)

draw_sprite(George,200,120)
wn.exitonclick()
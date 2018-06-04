import turtle
wn=turtle.Screen()
George=turtle.Turtle()
wn.bgcolor("Purple")
George.speed(10)

def draw_sprite(t,legs,length):
  for _ in range(legs):
    t.forward(length)
    t.forward(-length)
    t.left(360/legs)

def fancy_square(t):
  for _ in range(4):
    t.color("Blue")
    t.forward(150)
    t.color("Yellow")
    t.left(90)
    draw_sprite(George,30,10)

fancy_square(George)
wn.exitonclick()



draw_sprite(George,200,120)
wn.exitonclick()
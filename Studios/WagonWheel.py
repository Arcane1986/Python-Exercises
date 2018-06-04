import turtle
wn=turtle.Screen()
George=turtle.Turtle()
George.color("Blue")
wn.bgcolor("Red")
George.speed(10)

def draw_square(t,length):
  for _ in range(4):
    t.forward(length)
    t.left(90)

def wagon_wheel(t,squares):
  for _ in range(squares):
    draw_square(George,100)
    t.left(360/squares)

wagon_wheel(George,20)
wn.exitonclick()


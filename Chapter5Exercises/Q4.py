import turtle

wn=turtle.Screen()
wn.bgcolor("Blue")
Wilito=turtle.Turtle()
Wilito.color("Red")
Wilito.shape("turtle")
def spiral_square(t,shape):
  if shape == 1:
    for x in range(720):
      t.right(90)
      t.forward(x)
      x=x+1
      y=x-1
      t.speed(y)
  if shape == 2:
    for x in range(720):
      t.right(91)
      t.forward(x)
      x=x+1
      y=x-1
      t.speed(y)

spiral_square(Wilito,2)
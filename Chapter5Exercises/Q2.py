import turtle
wn = turtle.Screen()       # Set up the window and its attributeswn.bgcolor("lightgreen")
alex = turtle.Turtle()     # create alex
alex.color('hotpink')
alex.pensize(3)
alex.speed(10)
alex.penup()
alex.goto(-100,-100)
alex.pendown()

def expanding_square(side_length,squares,size_of_increase):
  for i in range(squares):
    new_side_length = side_length+size_of_increase*i
    alex.forward(new_side_length)
    alex.left(90)
    alex.forward(new_side_length)
    alex.left(90)
    alex.forward(new_side_length)
    alex.left(90)
    alex.forward(new_side_length)
    alex.left(90)
    alex.penup()
    alex.right(135)
    alex.forward(side_length/2*2**0.5)
    alex.left(135)
    alex.pendown()

expanding_square(10,30,10)
wn.exitonclick()
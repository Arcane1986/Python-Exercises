UserBGColor=input("Please indicate the background color: ")
UserPenColor=input("Please indicate the pen color: ")
UserPenWidth=int(input("Please indicate the width of your pen: ")
                 
import turtle
wn = turtle.Screen()
wn.bgcolor(UserBGColor)        # set the window background color

tess = turtle.Turtle()
tess.color(UserPenColor)              # make tess blue
tess.pensize(UserPenWidth)                 # set the width of her pen

tess.forward(150)
tess.left(120)
tess.forward(150)

wn.exitonclick()                # wait for a user click on the canvas
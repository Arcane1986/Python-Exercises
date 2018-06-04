import turtle
wn=turtle.Screen()
Rich=turtle.Turtle()

def draw_star(t,n):
    for _ in range(n):
        t.forward(100)
        t.right(720/n)
draw_star(Rich,7)
wn.exitonclick()
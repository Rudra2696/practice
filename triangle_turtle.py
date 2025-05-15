import turtle

r=turtle.Turtle()
r.color("red")
r.begin_fill()
for i in range(3):
    r.forward(100)
    r.left(120)
r.end_fill()
turtle.done()
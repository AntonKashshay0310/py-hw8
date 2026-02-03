import turtle

t = turtle.Turtle()
t.speed(3)


t.color("blue")
for i in range(4):
    t.forward(120)
    t.left(90)

t.penup()
t.goto(0, 120)
t.pendown()
t.color("red")
for i in range(3):
    t.forward(120)
    t.left(120)

t.penup()
t.goto(40, 40)
t.pendown()
t.color("yellow")
t.circle(20)

turtle.done()

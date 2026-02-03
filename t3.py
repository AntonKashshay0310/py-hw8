import turtle

t = turtle.Turtle()
t.speed(3)

t.color("red")
for i in range(4):
    t.forward(80)
    t.left(90)
t.write("Квадрат", font=("Arial", 12, "normal"))

t.penup()
t.goto(150, 0)
t.pendown()

t.color("blue")
t.circle(40)
t.write("Коло", font=("Arial", 12, "normal"))

t.penup()
t.goto(-150, 0)
t.pendown()


t.color("green")
for i in range(3):
    t.forward(80)
    t.left(120)
t.write("Трикутник", font=("Arial", 12, "normal"))

turtle.done()

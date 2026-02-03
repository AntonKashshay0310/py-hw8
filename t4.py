import turtle

t = turtle.Turtle()
t.speed(3)

x = int(input("Введіть координату X: "))
y = int(input("Введіть координату Y: "))

t.goto(x, y)

new_x = int(input("Введіть нову X: "))
t.setx(new_x)

new_y = int(input("Введіть нову Y: "))
t.sety(new_y)

turtle.done()

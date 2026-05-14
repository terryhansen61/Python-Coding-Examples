import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

t.speed(0)
h = 0.0  # hue from 0 to 1

for i in range(180):
    r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(r, g, b)
    h += 1/180  # slowly rotate hue

    for j in range(5):
        t.forward(150)
        t.right(144)

    t.right(2)
    h += 0.01

turtle.done()


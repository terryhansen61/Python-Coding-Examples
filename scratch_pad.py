
# This code creates a spiral diagram using turtle (graphics)
"""
from turtle import *
from colorsys import *

tracer(10)
bgcolor("black")
shape("square")
pensize(1)
h = 0
penup()

for i in range(600):
    h = (h + 0.01) % 1
    color(hsv_to_rgb(h, 1.0, 1.0))
    size = 0.1 + 1 * 0.01
    shapesize(size, size)
    forward(i * 0.5)
    right(59)
    stamp()
done()
"""

""" 
# This capitalizes the first character of the string
print("hello".capitalize())

# This capitalizes the entire string to upper case
print("hello".upper())

"""
"""
# This creates a class called Test, which returns the square of a number
# The FOR loop interates through numbers 1 thru 3 and returns the square for each number, N
class Test:
    def square(self, n):
        return n * n

t = Test()
for i in range(1,4):
    print(t.square(i), end=" ")
"""










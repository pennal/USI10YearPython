import turtle
import math

__author__ = 'Alessio Buratti'

height = 5
lato = 8
unit = 20
alfa = 45
depth = unit*(math.sin(math.radians(alfa)))

def griglia(lato = lato, unit = unit, depth = depth, alfa = alfa):
    for j in range(lato):
        for i in range(2):
            turtle.forward(lato*unit)
            turtle.left(alfa)
            turtle.forward(depth*lato)
            turtle.left(180-alfa)
        turtle.left(90)
        turtle.forward(unit)
        turtle.right(90)

def go_to(x, y, z, unit = unit, depth = depth, alfa = alfa, height = height):
    turtle.penup()
    turtle.home()
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(x*unit)
    turtle.left(90)
    turtle.forward(y*unit)
    turtle.right(90-alfa)
    turtle.forward(z*depth)
    turtle.right(alfa)
    turtle.pendown()


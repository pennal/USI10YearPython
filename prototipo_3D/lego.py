import turtle
from griglia import unit, alfa, depth, lato, height

__author__ = 'Alessio Buratti'
colors = {'red': '#7F100C', 'yellow': '#CCA210', 'white':'#C7C7CC', 'orange': '#CC7323', 'blue': '#1D1B7F', 'black': '#292827'}

def pezzo(color, colors = colors, unit = unit, alfa = alfa, depth = depth):
    turtle.pencolor(colors[color])
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(unit)
        turtle.left(90)
        turtle.forward(unit)
        turtle.left(90)
    turtle.forward(unit)
    for i in range(2):
        turtle.left(alfa)
        turtle.forward(depth)
        turtle.left(alfa)
        turtle.forward(unit)
        turtle.left(90)
    turtle.backward(unit)
    turtle.left(90)
    turtle.forward(unit)
    turtle.right(90)
    for i in range(2):
        turtle.forward(unit)
        turtle.left(alfa)
        turtle.forward(depth)
        turtle.left(180-alfa)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(unit)
    turtle.left(90)


def lego(larghezza, profonodita, color, alfa = alfa, depth = depth, unit = unit, colors = colors):
    turtle.pencolor(colors[color])
    #va all'inizio dell'ultima linea
    turtle.left(alfa)
    turtle.forward(depth*(profonodita-1))
    turtle.right(alfa)
    # turtle.backward(unit)
    #inizia a disegnare una riga alla volta partendo dal fondo
    for j in range(profonodita):
        for i in range(larghezza):
            pezzo(color)
            turtle.forward(unit)
        if j == profonodita-1:
            break
            turtle.backward(larghezza*unit)
        turtle.backward(unit*(larghezza))
        turtle.left(alfa)
        turtle.backward(depth)
        turtle.right(alfa)


############ BASE ##########

def base(color = 'blue',colors = colors, lato = lato, unit = unit, alfa = alfa, depth = depth, height = height):
    turtle.pencolor(colors[color])
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(unit*lato)
    turtle.left(alfa)
    turtle.forward(depth*lato)
    turtle.left(alfa)
    turtle.forward(height)
    turtle.left(90+alfa)
    turtle.forward(depth*lato)
    turtle.left(alfa)
    turtle.forward(height)
    turtle.backward(height)
    turtle.right(90)
    turtle.forward(lato*unit)
    turtle.left(90)
    turtle.forward(height)
    turtle.right(180)
    turtle.forward(height)
    turtle.right(alfa)
    turtle.forward(depth*lato)
    turtle.right(alfa)
    turtle.forward(lato*unit)
    turtle.left(alfa)
    turtle.backward(depth*lato)
    turtle.right(alfa)
    turtle.backward(unit*lato)
    turtle.end_fill()

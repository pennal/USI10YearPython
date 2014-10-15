import turtle
import math
import control
#========= CONSTANTS =========
height = 5
lato = 6
unit = 20
alfa = 45
depth = unit*(math.sin(math.radians(alfa)))

colors = {'red': '#7F100C', 'yellow': '#CCA210', 'white':'#C7C7CC', 'orange': '#CC7323', 'blue': '#1D1B7F', 'black': '#292827'}

#Disegna un pezzo seguendo le specifiche del parametro
def disegnaPezzo3D(color, colors = colors, unit = unit, alfa = alfa, depth = depth):
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

# Disegna pezzo di lego semplice
def disegnaPezzoLego(larghezza, profonodita, color, alfa = alfa, depth = depth, unit = unit, colors = colors):
    turtle.pencolor(colors[color])
    #va all'inizio dell'ultima linea
    turtle.left(alfa)
    turtle.forward(depth*(profonodita-1))
    turtle.right(alfa)
    #inizia a disegnare una riga alla volta partendo dal fondo
    for j in range(profonodita):
        for i in range(larghezza):
            disegnaPezzo3D(color)
            turtle.forward(unit)
        if j == profonodita-1:
            break
            turtle.backward(larghezza*unit)
        turtle.backward(unit*(larghezza))
        turtle.left(alfa)
        turtle.backward(depth)
        turtle.right(alfa)


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

def disegnaBase(color = 'blue',colors = colors, lato = lato, unit = unit, alfa = alfa, depth = depth, height = height):
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
    disegnaLineePerBase()

def controlloPezzoValido(larghezza, altezza, x, z, color):
    coor = control.aggiorna_matrice(larghezza,altezza,x,z)
    if coor is not None:
        go_to(coor[0],coor[1],coor[2])
        input('')
        print("Posizione corrente: x: " + str(6-z) + ", y: " + str(x))
        disegnaPezzoLego(larghezza, altezza, color)
        print("Disegnato pezzo " + str(larghezza) + "x" + str(altezza) + " di colore \"" + color + "\"")
        turtle.update()

    else:
        print('Fuori dal piano')

def disegnaLineePerBase(lato = lato, unit = unit, alfa = alfa, depth = depth): #disegna le linee scure sulla base per rendere meglio l'idea
    for i in range(lato):
        turtle.forward(unit)
        turtle.left(alfa)
        turtle.forward(lato*depth)
        turtle.backward(lato*depth)
        turtle.right(alfa)
    for i in range(lato):
        turtle.left(alfa)
        turtle.forward(depth)
        turtle.right(alfa)
        turtle.backward(lato*unit)
        turtle.forward(lato*unit)
    turtle.backward(lato*unit)
    turtle.left(alfa)
    turtle.backward(lato*depth)
    turtle.right(alfa)

def disegnaGriglia(lato = lato, unit = unit, depth = depth, alfa = alfa):
    for j in range(lato):
        for i in range(2):
            turtle.forward(lato*unit)
            turtle.left(alfa)
            turtle.forward(depth*lato)
            turtle.left(180-alfa)
        turtle.left(90)
        turtle.forward(unit)
        turtle.right(90)
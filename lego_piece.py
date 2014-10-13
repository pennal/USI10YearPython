import turtle
turtle.speed(0)
turtle.hideturtle()

unit = 20
def dots(width, height, color, colors, newX, newY, unit = unit): #draws the dots of the lego
    turtle.penup()
    turtle.color(colors[color])
    turtle.pensize(unit/4)
    for j in range(height):
        turtle.left(90)
        turtle.forward(unit/2+unit*j)
        turtle.right(90)
        turtle.forward(unit/2)          #turtle is on first dot of the row
        turtle.dot()
        for i in range(1,width):
            turtle.forward(unit)
            turtle.dot()
        turtle.goto(newX,newY)





def lego_piece(width, height, color, unit = unit): #draws the base of the lego piece
    (newX,newY) = turtle.pos()
    colors = {'red': '#7F100C', 'yellow': '#CCA210', 'white':'#C7C7CC', 'orange': '#CC7323', 'blue': '#1D1B7F', 'black': '#292827'}
    turtle.pensize(1)
    turtle.pencolor(colors[color])
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width*unit)
        turtle.left(90)
        turtle.forward(height*unit)
        turtle.left(90)
    turtle.end_fill()

    dots(width, height, color, colors, newX, newY)

    turtle.penup()
    turtle.home()
    turtle.pensize(1)
    turtle.pendown()

def goTo(x, y, unit = unit):
    turtle.penup()
    turtle.goto(x*unit,y*unit)
    turtle.pendown()
    #log by pennationelove



########################### VERTICAL VIEW

def bordo(height = unit+unit):
    turtle.left(90)
    turtle.forward(height)
    turtle.backward(height)
    turtle.right(90)

def dot_vertical(height = unit+unit, unit = unit): #funzione cazzona
    turtle.penup()
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(unit/4)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(unit/4)
    turtle.right(90)
    turtle.forward(unit/2)
    turtle.right(90)
    turtle.forward(unit/4)
    turtle.end_fill()
    turtle.penup()
    turtle.right(90)
    turtle.forward(3*unit//4)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.pendown()

def pezzo_singolo(colore_fill, colore_bordo, unit = unit, height = unit+unit):
    turtle.begin_fill()
    for i in range(2):
        turtle.pencolor(colore_bordo)
        turtle.forward(unit)
        turtle.left(90)
        turtle.pencolor(colore_fill)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    turtle.pencolor(colore_bordo)
    dot_vertical(height)

def check_z():
    return True

def pezzo_verticale(width, color, posizione, z, unit = unit):
    colors = {'red': '#7F100C', 'yellow': '#CCA210', 'white':'#C7C7CC', 'orange': '#CC7323', 'blue': '#1D1B7F', 'black': '#292827'}
    turtle.pencolor(colors[color])
    turtle.fillcolor(color)
    turtle.penup()
    turtle.forward(posizione*unit)
    turtle.left(90)
    turtle.forward((unit+unit)*z)
    turtle.right(90)
    turtle.pendown()
    for i in range(width):
        if check_z():
            pezzo_singolo(color, colors[color])
        turtle.forward(unit)
    bordo()
    turtle.backward(width*unit)
    bordo()


########## Base verticale

def disegna_base(unit = unit, width = 8):
    lego_piece(width,width,'blue')
    turtle.penup()
    turtle.backward(250)
    turtle.pendown()
    turtle.pencolor('#1D1B7F')
    turtle.fillcolor('blue')
    for i in range(width):
        pezzo_singolo('blue', '#1D1B7F', unit, unit/2)
        turtle.forward(unit)
    bordo(unit/2)
    turtle.backward(width*unit)
    bordo(unit/2)
    turtle.penup()
    turtle.home()
    turtle.pendown()
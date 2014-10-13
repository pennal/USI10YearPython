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
    turtle.pendown()

def goTo(x, y, unit = unit):
    turtle.penup()
    turtle.goto(x*unit,y*unit)
    turtle.pendown()
    #log by pennationelove



########################### VERTICAL VIEW




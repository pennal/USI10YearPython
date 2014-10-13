from lego_piece import *

#prova
# lego_piece(10,10,'blue')
# goTo(4,5)
# lego_piece(3,3,'red')
# goTo(9,1)
# lego_piece(1,4,'white')
# lego_piece(1,8,'yellow')

disegna_base()

def pezzo(width, height, color, x, y):
    goTo(x, y)
    lego_piece(width, height, color)
    turtle.penup()
    turtle.goto(-250,unit/2)
    turtle.pendown()
    pezzo_verticale(width, color, x)

pezzo(2,3, 'red', 2,3)
pezzo(1,1, 'orange', 7,1)
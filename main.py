from lego_piece import *


disegna_base()

def pezzo(width, height, color, x, y, z):
    goTo(x, y)
    lego_piece(width, height, color)
    turtle.penup()
    turtle.goto(-250,unit/2)
    turtle.pendown()
    pezzo_verticale(width, color, x, z)

pezzo(2,3, 'red', 2,3,0)
pezzo(1,1, 'orange', 7,1,1)
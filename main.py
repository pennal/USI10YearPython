from lego_piece import *

colors = {'red': '#7F100C', 'yellow': '#CCA210', 'white':'#C7C7CC', 'orange': '#CC7323', 'blue': '#1D1B7F', 'black': '#292827'}
disegna_base(colors)

def pezzo(width, height, color, x, y, colors = colors):
    lego_piece(width, height, color, colors, x, y)
    turtle.penup()
    turtle.goto(-250,unit/2)
    turtle.pendown()
    pezzo_verticale(width, height, color, x, y, colors)

pezzo(2,3, 'red', 2,3)
pezzo(1,1, 'orange', 2,1)
pezzo(1,2, 'blue', 3,3)
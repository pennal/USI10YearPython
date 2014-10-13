from lego_piece import *

#Imposta la base
lego_piece(6,6,'blue')

#Disegna i 4 blocchetti di base
lego_piece(2,2,'yellow')
#Blocco rosso
goTo(4,0)
lego_piece(2,2,'red')
#Blocco arancione
goTo(4,4)
lego_piece(2,2,'orange')
#Blocco bianco
goTo(0,4)
lego_piece(2,2,'white')
#Connettori
#Rosso
lego_piece(6,1,'red')
#Arancione
goTo(5,1)
lego_piece(1,4,'orange')
#Bianco
goTo(0,5)
lego_piece(6,1,'white')
#Giallo
goTo(0,1)
lego_piece(1,4,'yellow')

input("Enter to quit...")
#vertical_lego_piece(4, 'blue')
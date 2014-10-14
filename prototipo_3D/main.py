import griglia
import dati
import lego
import turtle

turtle.speed(0)

def user():
    larghezza = eval(input('Larghezza: '))
    altezza = eval(input('Altezza: '))
    x = eval(input('x: '))
    z = eval(input('z: '))
    color = input('Colore: ')
    return larghezza, altezza, x, z, color

lego.base()
for i in range(10):
    pezzo = user()
    coor = dati.aggiorna_matrice(pezzo[0],pezzo[1],pezzo[2],pezzo[3])
    if coor is not None:
        griglia.go_to(coor[0],coor[1],coor[2])
        lego.lego(pezzo[0],pezzo[1],pezzo[4])
    else:
        print('Fuori dal piano')

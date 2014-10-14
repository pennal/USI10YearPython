import dati
import lego
import griglia

def user():
    larghezza = eval(input('Larghezza: '))
    altezza = eval(input('Altezza: '))
    x = eval(input('x: '))
    z = eval(input('z: '))
    color = input('Colore: ')
    return larghezza, altezza, x, z, color

def disegna_pezzo(larghezza, altezza, x, z, color):
    coor = dati.aggiorna_matrice(larghezza,altezza,x,z)
    if coor is not None:
        griglia.go_to(coor[0],coor[1],coor[2])
        lego.lego(larghezza, altezza, color)
    else:
        print('Fuori dal piano')
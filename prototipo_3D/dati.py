__author__ = 'Alessio Buratti'

from griglia import lato

matrice_cubica = [ [ 0 for i in range(lato) ] for j in range(lato) ]

def aggiorna_matrice(larghezza, profondita, x, z, lato = lato):
    if larghezza+x <= lato and profondita+z <= lato:
        max = 0
        for i in range(larghezza):
            for j in range(profondita):
                matrice_cubica[x+i][z+j]+=1
                if max < matrice_cubica[x+i][z+j]:
                    max = matrice_cubica[x+i][z+j]
        return x, max-1, z
    else:
        return None
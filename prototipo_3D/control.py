from commands import *

#========= CONSTANTS =========
height = 5
lato = 6
unit = 50
alfa = 45
depth = unit*(math.sin(math.radians(alfa)))
matrice_piana = [ [ 0 for i in range(lato) ] for j in range(lato) ]

def aggiorna_matrice(larghezza, profondita, x, z, lato = lato):
    if larghezza+x <= lato and profondita+z <= lato:
        max = 0
        for i in range(larghezza):
            for j in range(profondita):
                matrice_piana[x+i][z+j]+=1
                if max < matrice_piana[x+i][z+j]:
                    max = matrice_piana[x+i][z+j]
        for i in range(larghezza):
            for j in range(profondita):
                matrice_piana[x+i][z+j]=max
        return x, max-1, z
    else:
        return None
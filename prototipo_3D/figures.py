import commands
import control
# Figure precreate per dimostrazione
def figura1():
    commands.controlloPezzoValido(6,2, 0,0 , 'white' )
    commands.controlloPezzoValido(2, 6, 4, 0, 'yellow')
    commands.controlloPezzoValido(6, 2, 0, 4, 'red')
    commands.controlloPezzoValido(2, 6, 0, 0, 'blue')

def figura2():
    commands.controlloPezzoValido(4, 2, 0, 4, 'black')
    commands.controlloPezzoValido(1, 2, 5, 4, 'orange')
    commands.controlloPezzoValido(1, 1, 5, 3, 'orange')
    commands.controlloPezzoValido(1, 1, 0, 0, 'yellow')
    commands.controlloPezzoValido(3, 1, 3, 0, 'black')
    commands.controlloPezzoValido(2, 3, 2, 3, 'yellow')
    commands.controlloPezzoValido(2, 3, 2, 0, 'yellow')
    commands.controlloPezzoValido(6, 1, 0, 1, 'red')

def figura3():
    commands.controlloPezzoValido(4, 2, 0, 4, 'orange')
    commands.controlloPezzoValido(1, 2, 5, 4, 'white')
    commands.controlloPezzoValido(4, 2, 0, 0, 'orange')
    commands.controlloPezzoValido(1, 2, 5, 0, 'white')
    commands.controlloPezzoValido(2, 4, 2, 1, 'red')
    commands.controlloPezzoValido(3, 2, 3, 2, 'blue')

def personal1():
    commands.controlloPezzoValido(4, 2, 0, 2, 'white')
    commands.controlloPezzoValido(1, 6, 3, 0, 'red')
    commands.controlloPezzoValido(4, 2, 2, 0, 'yellow')
    commands.controlloPezzoValido(1, 2, 5, 1, 'black')



def personal2():
    commands.controlloPezzoValido(6, 2, 0, 4, 'white')
    commands.controlloPezzoValido(6, 1, 0, 0, 'white')
    commands.controlloPezzoValido(2, 6, 0, 0, 'black')
    commands.controlloPezzoValido(2, 6, 4, 0, 'yellow')
    commands.controlloPezzoValido(2, 2, 4, 2, 'black')
    commands.controlloPezzoValido(2, 2, 4, 2, 'blue')





















def castello():
    for i in range(4):
        commands.controlloPezzoValido(2, 2, 0, 4, 'black')
        commands.controlloPezzoValido(2, 1, 2, 5, 'black')
        commands.controlloPezzoValido(2, 2, 4, 4, 'black')
        commands.controlloPezzoValido(1, 2, 0, 2, 'black')
        commands.controlloPezzoValido(2, 2, 2, 2, 'white')
        commands.controlloPezzoValido(1, 2, 5, 2, 'black')
        commands.controlloPezzoValido(2, 2, 0, 0, 'black')
        if i <2:
            commands.controlloPezzoValido(2, 1, 2, 0, 'orange')
        else:
            commands.controlloPezzoValido(2, 1, 2, 0, 'black')
        commands.controlloPezzoValido(2, 2, 4, 0, 'black')
    commands.controlloPezzoValido(2, 2, 0, 4, 'black')
    commands.controlloPezzoValido(2, 2, 4, 4, 'black')
    commands.controlloPezzoValido(2, 2, 0, 0, 'black')
    commands.controlloPezzoValido(2, 2, 4, 0, 'black')


#    control.aggiorna_matrice(1, 2, 0, 0)

import commands
# Figure precreate per dimostrazione
def figura1():
    commands.controlloPezzoValido(4, 2, 1, 4, 'yellow')
    commands.controlloPezzoValido(2, 2, 0, 2, 'blue')
    commands.controlloPezzoValido(2, 2, 4, 2, 'orange')
    commands.controlloPezzoValido(4, 2, 1, 0, 'white')
    commands.controlloPezzoValido(2, 6, 2, 0, 'red')
    commands.controlloPezzoValido(1, 4, 2, 1, 'orange')
    commands.controlloPezzoValido(1, 4, 3, 1, 'blue')

def figura2():
    commands.controlloPezzoValido(4, 1, 0, 5, 'black')
    commands.controlloPezzoValido(1, 1, 0, 0, 'yellow')
    commands.controlloPezzoValido(3, 1, 3, 0, 'black')
    commands.controlloPezzoValido(2, 6, 2, 0, 'yellow')
    commands.controlloPezzoValido(6, 1, 0, 1, 'red')

def figura3():
    commands.controlloPezzoValido(4, 2, 0, 4, 'orange')
    commands.controlloPezzoValido(1, 2, 5, 4, 'black')
    commands.controlloPezzoValido(4, 2, 0, 0, 'orange')
    commands.controlloPezzoValido(1, 2, 5, 0, 'black')
    commands.controlloPezzoValido(2, 4, 2, 1, 'red')
    commands.controlloPezzoValido(3, 2, 3, 2, 'white')
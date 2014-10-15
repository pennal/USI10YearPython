import commands
import figures
import turtle

#Imposta il refresh a intervalli alti, velocizza il tutto
turtle.tracer(10)
#Nascondi al tartaruga
turtle.hideturtle()
#Disegna la base in ogni caso
commands.disegnaBase()
# turtle.update()
#Semplice scelta
scelta = int(input("Disegno: "))

print('Enter per iniziare!\n')


if scelta == 1:
    figures.figura1()
elif scelta == 2:
    figures.figura2()
elif scelta == 3:
    figures.figura3()
elif scelta == 4:
    figures.personal1()
elif scelta == 5:
    figures.personal2()
else:
    figures.castello()
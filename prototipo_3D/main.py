import commands
import figures
import turtle

#Imposta il refresh a intervalli alti, velocizza il tutto
turtle.tracer(50)
#Nascondi al tartaruga
turtle.hideturtle()


#Semplice scelta
scelta = int(input("Disegno: "))
#Disegna la base in ogni caso
commands.disegnaBase()
if scelta == 1:
    figures.figura1()
elif scelta == 2:
    figures.figura2()
elif scelta == 3:
    figures.figura3()

input("Enter to quit...")

from turtle import Screen
from paddle import Paddle

win = Screen()

# Definimos las caracteristicas basicas de la pantalla
win.bgcolor("black")
win.title("Pong game 🏓")

# Definimos dimensiones y delay de las animaciones en pantalla
win.setup(width=800, height=600)
win.tracer(0)

paddle_r = Paddle("r")
paddle_l = Paddle("l")

win.listen()
win.onkeypress(paddle_r.move_up, "Up")
win.onkeypress(paddle_r.move_down, "Down")
win.onkeypress(paddle_l.move_up, "w")
win.onkeypress(paddle_l.move_down, "s")

game_on = True
while game_on:
    win.update()

win.exitonclick()

# Nota para el shapesize: Ya que el objeto turtle viene con dimensiones por defecto de 20x20, por lo que los valores
# es la cantidad de veces que se estira con respecto a sus dimensiones (alto: 20x5=100; ancho: 20x1=20)

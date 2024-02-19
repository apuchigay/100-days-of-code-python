from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Definimos las caracteristicas basicas de la pantalla
win = Screen()
win.bgcolor("black")
win.title("Pong game 🏓")
# Definimos dimensiones y delay de las animaciones en pantalla
win.setup(width=800, height=600)
win.tracer(0)

# Creamos las dos paletas
r_paddle = Paddle("r")
l_paddle = Paddle("l")

# Creamos la pelota
ball = Ball(r_paddle, l_paddle)

win.listen()
win.onkeypress(r_paddle.move_up, "Up")
win.onkeypress(r_paddle.move_down, "Down")
win.onkeypress(l_paddle.move_up, "w")
win.onkeypress(l_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(.05)
    win.update()
    ball.move()

win.exitonclick()

# Nota para el shapesize: Ya que el objeto turtle viene con dimensiones por defecto de 20x20, por lo que los valores
# es la cantidad de veces que se estira con respecto a sus dimensiones (alto: 20x5=100; ancho: 20x1=20)

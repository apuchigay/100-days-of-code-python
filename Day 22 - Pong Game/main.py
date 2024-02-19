from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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

# Creamos el tablero de puntajes
scoreboard = Scoreboard()

win.listen()
win.onkeypress(r_paddle.move_up, "Up")
win.onkeypress(r_paddle.move_down, "Down")
win.onkeypress(l_paddle.move_up, "w")
win.onkeypress(l_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    win.update()
    ball.move()

    # Da un puntaje al jugador izquierdo
    if ball.xcor() > 410:
        scoreboard.l_point()

    # Da un puntaje al jugador izquierdo
    if ball.xcor() < -410:
        scoreboard.r_point()

win.exitonclick()

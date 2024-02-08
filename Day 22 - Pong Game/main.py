import turtle
from turtle import Screen, Turtle

win = Screen()

# Definimos las caracteristicas basicas de la pantalla
win.bgcolor("black")
win.title("Pong game 🏓")
turtle.speed("fastest")  # Elimina la animación de movimiento de la posición

# Definimos dimensiones y delay de las animaciones en pantalla
win.setup(width=800, height=600)
win.tracer(0)

paddle = Turtle("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)

# Definir la posición en pantalla de la paleta
paddle.penup()
paddle.goto(360, 0)


# Escucha las teclas del usuario
def move_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def move_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


win.listen()
win.onkeypress(move_up, "Up")
win.onkeypress(move_down, "Down")

game_on = True
while game_on:
    win.update()

win.exitonclick()

# Nota para el shapesize: Ya que el objeto turtle viene con dimensiones por defecto de 20x20, por lo que los valores
# es la cantidad de veces que se estira con respecto a sus dimensiones (alto: 20x5=100; ancho: 20x1=20)

from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game 🐍")

# Definimos las dimensiones y el tiempo de delay en las animaciones de la pantalla
screen.setup(width=600, height=600)
screen.tracer(0)

snakes = Snake()

screen.listen()  # escuchamos el input de teclado
screen.onkey(fun=snakes.move_up, key="Up")
screen.onkey(fun=snakes.move_down, key="Down")
screen.onkey(fun=snakes.move_east, key="Right")
screen.onkey(fun=snakes.move_west, key="Left")

game_is_on = True
while game_is_on:
    # Actualiza la pantalla luego de que todos los movimientos de la serpiente se hayan hecho
    screen.update()
    time.sleep(0.1)
    snakes.move()

screen.mainloop()

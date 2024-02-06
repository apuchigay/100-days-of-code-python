from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game 🐍")

# Definimos las dimensiones y el tiempo de delay en las animaciones de la pantalla
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()  # escuchamos el input de teclado
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_east, key="Right")
screen.onkey(fun=snake.move_west, key="Left")

game_is_on = True
while game_is_on:
    # Actualiza la pantalla luego de que todos los movimientos de la serpiente se hayan hecho
    screen.update()
    time.sleep(0.08)
    snake.move()
    scoreboard.write_score()

    # Detecta la colision entre objetos
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detecta la colisión con la pared
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detecta la colision con el cuerpo
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

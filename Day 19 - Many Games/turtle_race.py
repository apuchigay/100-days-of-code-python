from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=420)
is_race_on = False
tortugas = []

# Retorna una cadena, por lo que la almacenamos en una variable. Funciona similar a un input()
user_bet = screen.textinput(title="¡Hagan sus apuestas!",
                            prompt="¿Que tortuga crees ganará la carrera? Digita el color: ")


def create_turtles():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y = -180
    # Asigna colores a diferentes tortugas y luego las almacena en una lista
    for i in range(6):
        tortugas.append(Turtle(shape="turtle"))
        tortugas[i].penup()
        tortugas[i].color(colors[i])
        tortugas[i].goto(-230, y)
        y += 70
    return tortugas


if user_bet:
    is_race_on = True
    create_turtles()

while is_race_on:
    for tortuga in tortugas:
        if tortuga.xcor() > 210:
            is_race_on = False
            winner = tortuga.pencolor()
            if winner == user_bet:
                print(f"¡Felicidades! La tortuga {winner} ha ganado la carrera")
            else:
                print(f"Perdiste. La tortuga {winner} ha ganado la carrera")

        distance = random.randint(0, 10)
        tortuga.forward(distance)

screen.mainloop()

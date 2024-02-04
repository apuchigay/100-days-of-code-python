import random
import turtle as t

# Listado de colores para la pintura
colores = [(54, 108, 149),
           (225, 201, 108),
           (134, 85, 58),
           (229, 235, 234),
           (224, 141, 62),
           (197, 144, 171),
           (143, 180, 206),
           (137, 82, 106),
           (210, 90, 68),
           (232, 226, 194),
           (188, 78, 122),
           (69, 101, 86),
           (132, 183, 132)
           ]

matt = t.Turtle()
matt.speed(0)
t.colormode(255)
matt.hideturtle()  # Ocultamos el objeto
matt.penup()  # Levantamos el lapiz para que no se vea el trazo del recorrido

for y in range(-250, 250, 50):
    for x in range(-250, 250, 50):
        matt.goto(x, y)  # Definimos las coordenadas en x:y
        matt.dot(20, random.choice(colores))

screen = t.Screen()
screen.exitonclick()

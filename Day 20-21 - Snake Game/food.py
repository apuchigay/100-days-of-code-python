from turtle import Turtle
import random as ran


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()  # Levata el lapiz para que no dibuje al moverse de posición
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Define dimensiones de 10x10
        self.color("purple")
        self.speed(0)
        self.refresh()

    def refresh(self):
        x_pos = ran.randrange(-280, 280, 20)
        y_pos = ran.randrange(-280, 280, 20)
        self.goto(x_pos, y_pos)

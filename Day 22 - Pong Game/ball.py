from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        # Define las direcciones de X e Y
        self.direction_y = 10
        self.direction_x = 10

    def move(self):
        new_x = self.xcor() + self.direction_x
        new_y = self.ycor() + self.direction_y
        self.goto(new_x, new_y)
        self.bounce()

    def bounce(self):
        """Válida si la posición del objeto es superior al límite superior e inferior para despues invertir sus
        posiciones"""
        if self.ycor() > 280:
            self.sety(280)
            self.direction_y *= -1

        if self.ycor() < -280:
            self.sety(-280)
            self.direction_y *= -1

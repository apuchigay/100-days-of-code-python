from turtle import Turtle


class Ball(Turtle):
    def __init__(self, r_paddle, l_paddle):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        # Define las direcciones de X e Y
        self.direction_y = 10
        self.direction_x = 10
        self.r_paddle = r_paddle
        self.l_paddle = l_paddle

    def move(self):
        new_x = self.xcor() + self.direction_x
        new_y = self.ycor() + self.direction_y
        self.goto(new_x, new_y)
        self.bounce()

    def bounce(self):
        """Válida si la posición del objeto es superior al límite superior e inferior para despues invertir sus
        posiciones"""
        # Detecta las colisiones con los bordes superior e inferior
        if self.ycor() > 270 or self.ycor() < -270:
            self.sety(self.ycor())
            self.direction_y *= -1

        # Detecta colisiones con las paletas
        if ((self.distance(self.r_paddle) < 50 and self.xcor() > 320)
                or (self.distance(self.l_paddle) < 50 and self.xcor() < -320)):
            self.bounce_x()

    def bounce_x(self):
        self.direction_x *= -1

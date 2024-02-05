from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="Center", font=("8BIT WONDER", 8, "normal"))

    def increase_score(self):
        self.score += 1
        self.write_score()

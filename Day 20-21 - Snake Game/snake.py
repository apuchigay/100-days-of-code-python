from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 0
RIGHT = 180


class Snake:
    def __init__(self):
        self.snakes = []
        self.creating_snake_body()
        self.head = self.snakes[0]

    def creating_snake_body(self):
        """Metodo que crea el cuerpo inicial de la serpiente a partir de una lista"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snakes.append(new_segment)

    def extend(self):
        """Añade un nuevo segmento a la serpiente"""
        self.add_segment(self.snakes[-1].position())

    def move(self):
        """Mueve de forma automatica a la serpiente. No recibe parametros"""
        # Mueve la posición de las partes de la serpiente tomando la posición de su predecesora
        # ej. El índice 2 toma la posición del 1, el 1 el del 0, y el 0 se mueve 20 espacios en el plano
        for part_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[part_num - 1].xcor()
            new_y = self.snakes[part_num - 1].ycor()
            self.snakes[part_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_east(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_west(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

from turtle import Turtle, Screen

zarco = Turtle('turtle')
screen = Screen()
# Nota: Mejorar el codigo para mover la tortuga sosteniendo dos teclas


def move_forward():
    """Mueve el objeto 10 posiciones hacia donde se encuentre mirando"""
    zarco.forward(10)


def move_backward():
    """Mueve el objeto 10 posiciones hacia atras de donde se encuentre mirando"""
    zarco.backward(10)


def turn_left():
    """Mueve el objeto 10 posiciones hacia la izquierda"""
    zarco.left(10)


def turn_right():
    """Mueve el objeto 10 posiciones hacia la derecha"""
    zarco.right(10)


def restart():
    """Limpia el lienzo y retorna la tortuga a la posición de inicio"""
    zarco.reset()


screen.listen()
screen.onkeypress(key="w", fun=move_forward)  # Ejecuta move_forward solo cuando space es oprimido
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkey(key="c", fun=restart)
screen.mainloop()  # Mantiene la ventana abierta

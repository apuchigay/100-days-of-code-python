def get_another_card():
    """Pregunta al jugador si desea otra carta en su baraja"""
    return input("Type 'y' to get another card or 'n' to pass: ").lower() == "y"

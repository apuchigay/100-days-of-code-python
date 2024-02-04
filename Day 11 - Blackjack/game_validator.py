def play_game():
    """Pregunta al jugador si quiere iniciar un juego de Blackjack"""
    player_choice = input("Do you want to play Blackjack🃏? Type 'y' to start or 'n' to exit: ").lower()
    return player_choice == "y"

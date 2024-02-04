import random


def deck_cards():
    """Entrega una carta aleatoria de la baraja completa"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    picked_card = random.choice(cards)
    return picked_card

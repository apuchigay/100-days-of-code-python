import complete_deck


def deal_cards(player_deck):
    """Reparte las cartas entre los participantes"""
    # Reparte dos cartas en caso de que el jugador no tenga ninguna en su baraja
    if len(player_deck) < 2:
        for i in range(2):
            player_deck.append(complete_deck.deck_cards())
    else:
        player_deck.append(complete_deck.deck_cards())
    return player_deck

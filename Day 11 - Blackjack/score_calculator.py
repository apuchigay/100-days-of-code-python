def calc_score(player_deck):
    """Calcula el puntaje total de cada jugador. También válida el comportamiento del As cuando se requiera"""
    total_score = sum(player_deck)
    if total_score > 21 and 11 in player_deck:
        player_deck.remove(11)
        player_deck.append(1)
        return total_score
    else:
        return total_score

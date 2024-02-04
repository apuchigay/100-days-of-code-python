import random
import art
import game_validator
import give_cards
import score_calculator
import pick_a_card

user_deck = []
dealer_deck = []

win_emoji_list = ["👊", "✌️", "😎", "😁", "🤩"]
lose_emoji_list = ["🥲", "😭", "😢", "😩", "🫠"]

win_emoji = random.choice(win_emoji_list)
lose_emoji = random.choice(lose_emoji_list)


def blackjack_game():
    """Función que inicia el juego de Blackjack o '21'"""
    print(art.logo)
    while game_validator.play_game():
        user_deck.clear()
        dealer_deck.clear()
        user_cards = give_cards.deal_cards(user_deck)
        dealer_cards = give_cards.deal_cards(dealer_deck)

        user_score = score_calculator.calc_score(user_cards)
        dealer_score = score_calculator.calc_score(dealer_cards)

        print(f"  Your cards: {user_cards}  Current score: {user_score}\n"
              f"  Dealer's first card: {dealer_cards[0]}")

        while user_score < 21 and pick_a_card.get_another_card():
            user_cards = give_cards.deal_cards(user_deck)
            user_score = score_calculator.calc_score(user_cards)
            print(f"  Your cards: {user_cards}  Current score: {user_score}\n"
                  f"  Dealer's first card: {dealer_cards[0]}")

        if user_score == 21:
            print("User wins")
        elif user_score > 21:
            print(f"You went over. Dealer wins. {lose_emoji}")
        else:
            print(f"Dealer's turn.")
            while dealer_score < 17:
                dealer_cards = give_cards.deal_cards(dealer_deck)
                dealer_score = score_calculator.calc_score(dealer_cards)

            print(f"  Your final hand: {user_cards}  Your final score: {user_score}\n"
                  f"  Dealer's final hand: {dealer_cards}  Dealer's final score: {dealer_score}")

            if dealer_score > 21:
                print(f"Dealer went over. You win! {win_emoji}")
            elif dealer_score > user_score:
                print(f"Dealer wins {lose_emoji}")
            elif dealer_score < user_score:
                print(f"You win! {win_emoji}")
            else:
                print(f"It's a draw. 🙅")

        print("---------------------------------------------")
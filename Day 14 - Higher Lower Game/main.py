from art import logo, vs
from game_data import data
import random

correct_answer = ""
correct_answer_dic = {}
score = 0
compare_a = random.choice(data)

while True:
    # Asegura que los valores de "A" y "B" no sean iguales
    print(logo)
    while True:
        compare_b = random.choice(data)

        if compare_a != compare_b:
            break
        else:
            continue

    print(f"Compare A: {compare_a['name']}, a {compare_a['description']} from {compare_a['country']}.")
    print(vs)
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']} from {compare_b['country']}.")
    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Válida cuál es el valor más alto entre las dos busquedas
    if compare_a["follower_count"] > compare_b["follower_count"]:
        correct_answer = "A"
        correct_answer_dic = compare_a
    elif compare_a["follower_count"] < compare_b["follower_count"]:
        correct_answer = "B"
        correct_answer_dic = compare_b

    if user_answer == correct_answer:
        score += 1
        print(f"You got it! That's the answer! Current score {score}")
        compare_a = correct_answer_dic
        compare_b = data[random.randint(0, len(data) - 1)]
    else:
        break

print(f"Sorry. That's not the answer\nYour final score: {score}")

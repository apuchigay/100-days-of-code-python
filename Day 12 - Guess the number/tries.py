import difficulty_chose
import random

answer = random.randint(1, 101)


def tries_left():
    """Adivina la cantidad de intentos que tiene una persona de adivinar un numero"""
    num_attemps = difficulty_chose.diff_chose()
    while num_attemps > 0:
        print(f"You have {num_attemps} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess != answer:
            num_attemps -= 1
            if guess < answer:
                print("Too low")
            elif guess > answer:
                print("Too high")
            if num_attemps > 0:
                print("Guess again.")
        else:
            print(f"You got it! The answer was {answer}")
            return

    print("You've run out of guesses, you lose.")

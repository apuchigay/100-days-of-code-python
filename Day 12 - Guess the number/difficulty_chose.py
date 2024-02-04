def diff_chose():
    """Retorna una cantidad de intentos dependiendo de la respuesta del usuario"""
    while True:
        difficulty = input("Please, choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print("This isn't a valid option.")

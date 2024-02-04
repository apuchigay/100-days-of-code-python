import art
import clear

print(art.logo)


# Add
def add(n1, n2):
    return n1 + n2


# Substract
def substract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# Dictionary
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def start_calculation():
    number = int(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    return number


num1 = start_calculation()

while True:
    operator = input("Pick an operator from the line above: ")
    num2 = int(input("What's the next number? "))

    answer = operations[operator](num1, num2)

    print(f"{num1} {operator} {num2} = {answer}")

    keep_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()

    if keep_calculation != "n":
        num_1 = answer
    else:
        clear.clear_console()
        num1 = start_calculation()


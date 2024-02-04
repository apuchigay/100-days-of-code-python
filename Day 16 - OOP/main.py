from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# from prettytable import PrettyTable
# from turtle import Turtle, Screen
#
# elxokas = Turtle()
# print(elxokas)
# elxokas.shape("turtle")
# elxokas.color("#fe8932")
# elxokas.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

# table = PrettyTable()  # Objeto table creado a partir de la clase PrettyTable
# table.field_names = ("Pokemon Name", "Type")  # Definimos el nombre de las columnas
#
# # Añadimos las filas que rellenaran esas columnas
# table.add_rows(
#     [
#         ["Pikachu", "Electric"],
#         ["Squirtle", "Water"],
#         ["Charmander", "Fire"],
#     ]
# )
# table.horizontal_char = "—"
# # metodo para alinear textos (r=right, l=left)
# # table.align = "l"
#
# print(table)

coffee_menu = Menu()
coffee_machine = CoffeeMaker()
machine_profit = MoneyMachine()

while True:
    coffee_drink = input(f"What would you like? ({coffee_menu.get_items()}): ").lower()
    if coffee_drink == "report":
        coffee_machine.report()
        machine_profit.report()
    else:
        drink = coffee_menu.find_drink(coffee_drink)
        if coffee_machine.is_resource_sufficient(drink):
            if machine_profit.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)



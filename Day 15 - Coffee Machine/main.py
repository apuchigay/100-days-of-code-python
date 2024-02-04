from resources_dict import MENU, resources

options = ["espresso", "latte", "cappuccino"]
machine_profit = 0
total_profit = 0


def resources_left(coffee):
    """Funcion que va eliminando la cantidad de recursos segun se vaya pidiendo café"""
    for key, value in resources.items():
        if key in MENU[coffee]["ingredients"]:
            resources[key] = resources[key] - MENU[coffee]["ingredients"][key]


def check_money(coffee):
    """Funcion que pide la cantidad de monedas para el pago y retorna el total"""
    total_quarters = int(input("How many quarters?: ")) * 0.25
    total_dimes = int(input("How many dimes?: ")) * 0.1
    total_nickles = int(input("How many nickles?: ")) * 0.05
    total_pennies = int(input("How many pennies?: ")) * 0.01

    total_pay = total_quarters + total_nickles + total_dimes + total_pennies

    # Válida que el total pagado sea mayor al costo del cafe
    if total_pay >= MENU[coffee]["cost"]:
        return total_pay, coffee
    elif total_pay < MENU[coffee]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def calculate_change_profit(user_payment, coffee):
    """Función que retorna el cambio del usuario y la ganancia de la máquina de café"""
    total_pay = user_payment
    user_change = total_pay - MENU[coffee]["cost"]
    profit = MENU[coffee]["cost"]
    return user_change, profit


def complete_report():
    for key, value in resources.items():
        print(f"{key}: {value}")
    print(f"Money: ${total_profit}")


def check_resources(coffee):
    for key, value in resources.items():
        if key in MENU[coffee]["ingredients"]:
            if MENU[coffee]["ingredients"][key] > resources[key]:
                print(f"Sorry, there is not enough {key}.")
                return False
        else:
            continue
    return True


while True:

    coffee_drink = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if coffee_drink == "report":
        complete_report()
    elif coffee_drink not in options:
        print("Please, enter a valid option")
        continue
    else:
        total_resources = check_resources(coffee=coffee_drink)
        if total_resources is not False:
            total_paid = check_money(coffee=coffee_drink)
        else:
            continue

        if total_paid is not False:
            customer_money = calculate_change_profit(user_payment=total_paid[0], coffee=coffee_drink)[0]
            machine_profit += calculate_change_profit(user_payment=total_paid[0], coffee=coffee_drink)[1]
            total_profit = total_profit + machine_profit
            resources_left(coffee=coffee_drink)
            print(f"Here is ${customer_money:.2f} in change.")
            print(f"Here is your {coffee_drink.capitalize()}☕. Enjoy!")
        else:
            continue

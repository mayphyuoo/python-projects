import os
from prettytable.colortable import PrettyTable, ColorTable, Theme
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def clear_console():
    """Clear terminal"""
    return os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def print_menu(_coffeeMenu):
    """Print menu in formatted table"""
    table = PrettyTable()
    coffeeTheme = Theme(default_color="35",vertical_color="34",horizontal_color="34",junction_color="33")
    table = ColorTable(theme=coffeeTheme)
    coffeeList = []
    costList = []
    for coffee in _coffeeMenu:
        coffeeList.append(coffee.name)
        costList.append(coffee.cost)
    table.add_column("Coffee", coffeeList)
    table.add_column("Cost", costList)
    table.align = "l"
    print(table)


barista = CoffeeMaker()
cashier = MoneyMachine()
coffeeMenu = Menu()

machineOn = True

while machineOn:
    # print(f"\nHere is the menu:\n{coffeeMenu.get_items()}")
    print_menu(coffeeMenu.get_menu())
    choice = input("What would you like today?: ")

    if choice == "off":
        machineOn = False
    elif choice == "report":
        barista.report()
        cashier.report()
    elif choice == "clear":
        clear_console()
    elif choice == "refill":
        barista.refill_resources()
    elif coffeeMenu.find_inMenu(choice) is True:
        coffee = coffeeMenu.find_drink(choice)
        if barista.is_resource_sufficient(coffee):
            if cashier.make_payment(coffee.cost):
                barista.make_coffee(coffee)
    elif coffeeMenu.find_inMenu(choice) is False:
        print("Sorry that item is not available.")

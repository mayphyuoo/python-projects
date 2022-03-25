import os
from data import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def clear_console():
    """Clear terminal"""
    return os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def print_dictionary(dict):
    """print resources dictionary"""
    return f"""Water: {dict['water']}ml
Milk: {dict['milk']}ml
Coffee: {dict['coffee']}g"""


def check_resources(res, req):
    """Check resources for coffee, return true if enough"""
    enoughRes = True
    insufficientRes = ""
    if res['water'] < req['water']:
        enoughRes = False
        insufficientRes = "water"
    if res['coffee'] < req['coffee']:
        enoughRes = False
        insufficientRes = "coffee"
    if 'milk' in req.keys():
        if res['milk'] < req['milk']:
            enoughRes = False
            insufficientRes = "milk"
    return enoughRes, insufficientRes


def process_transaction(cost):
    """Ask to pay and process money paid"""
    coins = ["quarters", "dimes", "nickles", "pennies"]
    coinAmount = [0, 0, 0, 0]
    complete = True

    quarter = 0.25
    dime = 0.1
    nickle = 0.05
    penny = 0.01

    print("Please insert coins.")
    for i in range(len(coins)):
        coinAmount[i] = int(input(f"How many {coins[i]}?: "))

    paid = quarter * coinAmount[0] + dime * coinAmount[1] + nickle * coinAmount[2] + penny * coinAmount[3]
    if paid > cost:
        change = round(paid - cost, 2)
        paid = cost
    elif paid < cost:
        change = paid
        complete = False
        paid = 0
    elif paid == cost:
        change = 0
        paid = cost
    return change, complete, paid


def make_coffee(res, req):
    """Deduct resources and make coffee ☕"""
    res['water'] = res['water'] - req['water']
    res['coffee'] = res['coffee'] - req['coffee']
    if 'milk' in req.keys():
        res['milk'] = res['milk'] - req['milk']

    return res


def refill_coffeeMachine(resources):
    water = int(input("How much water?: "))
    milk = int(input("How much milk?: "))
    coffee = int(input("How much coffee?: "))
    resources['water'] += water
    resources['milk'] += milk
    resources['coffee'] += coffee
    return resources


machineOn = True
money = 0

clear_console()

while machineOn:
    choice = input("What would you like? (espresso/latte/cappuccino)[report/refill]: ")

    if choice == "off":
        machineOn = False
        clear_console()
    elif choice == "report":
        print(print_dictionary(resources))
        print(f"Money: ${money}")
    elif choice in MENU.keys():
        enough, res = check_resources(resources, MENU[choice]['ingredients'])
        if enough is True:
            print("Enough resources. proceed to make coffee")
            change, done, profit = process_transaction(MENU[choice]['cost'])
            money += profit
            if done is False:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print("Payment completed. making coffee.")
                resources = make_coffee(resources, MENU[choice]['ingredients'])
                print(f"Here is your {choice}. Enjoy!")
                if change > 0:
                    print(f"Here is ${change} dollars in change.")
        else:
            print(f"Sorry there is not enough {res}.")
    elif choice == "refill":
        print("Refilling coffee machine")
        resources = refill_coffeeMachine(resources)
    elif choice == "clear":
        clear_console()
    else:
        print("Invalid menu.")

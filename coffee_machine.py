from main import resources
from main import MENU


def espresso():
    if resources["water"] >= 50 and resources["coffee"] >= 18:
        print("please insert coins")
        quarters = int(input("how many quarters"))
        dimes = int(input("how many dimes"))
        nickles = int(input("how many nickels"))
        pennies = int(input("how many pennies"))
        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        change = total - 1.5
        if total < 1.5:
            print("Sorry that's not enough money. Money refunded.")
            game()
        elif total >= 1.5:
            print(f"here is ${change.__round__(2)} in change.")
            print("Enjoy your espresso.☕")
            resources["cost"] = resources["cost"] + 1.5
            resources["water"] = resources["water"] - 50
            resources["coffee"] = resources["coffee"] - 18
    elif resources["water"] < 200:
        print("there is not enough water")
    elif resources["coffee"] < 24:
        print("There is not enough coffee")
    elif resources["milk"] < 150:
        print("there is not enough milk")


def latte():
    if resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 150:
        print("please insert coins")
        quarters = int(input("how many quarters"))
        dimes = int(input("how many dimes"))
        nickles = int(input("how many nickels"))
        pennies = int(input("how many pennies"))
        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        change = total - 2.5
        if total < 2.5:
            print("Sorry that's not enough money. Money refunded.")
            game()
        elif total >= 2.5:
            print(f"here is ${change.__round__(2)} in change.")
            print("Enjoy your latte.☕")
            resources["cost"] = resources["cost"] + 2.5
            resources["water"] = resources["water"] - 200
            resources["coffee"] = resources["coffee"] - 24
            resources["milk"] = resources["milk"] - 150
    elif resources["water"] < 200:
        print("there is not enough water")
    elif resources["coffee"] < 24:
        print("There is not enough coffee")
    elif resources["milk"] < 150:
        print("there is not enough milk")


def cappuccino():
    if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:
        print("please insert coins")
        quarters = int(input("how many quarters"))
        dimes = int(input("how many dimes"))
        nickles = int(input("how many nickels"))
        pennies = int(input("how many pennies"))
        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        change = total - 3
        if total < 3:
            print("Sorry that's not enough money. Money refunded.")
            game()
        elif total >= 3:
            print(f"here is ${change.__round__(2)} in change.")
            print("Enjoy your cappuccino.☕")
            resources["cost"] = resources["cost"] + 3
            resources["water"] = resources["water"] - 250
            resources["coffee"] = resources["coffee"] - 24
            resources["milk"] = resources["milk"] - 100
    elif resources["water"] < 250:
        print("there is not enough water")
    elif resources["coffee"] < 24:
        print("There is not enough coffee")
    elif resources["milk"] < 100:
        print("there is not enough milk")



def game():
    user_asking = True
    while user_asking:
        user = input("What would you like? (espresso/latte/cappuccino): ")
        if user == "report":
            # for key, value in resources.items():  another way to print key and value in dict
            #     print(key, value)
            print(f"water {resources['water']}ml")
            print(f"milk {resources['milk']}ml")
            print(f"coffee {resources['coffee']}g")
            print(f"profit ${resources['cost']}")
        elif user == "off":
            user_asking = False
            print("Coffee Machine is off! now")
        elif user == "espresso":
            espresso()
        elif user == "latte":
            latte()
        elif user == "cappuccino":
            cappuccino()


game()

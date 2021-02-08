from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system
from time import sleep

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
MORE = True


def clear():
    system('cls||clear')


while MORE:
    while True:
        clear()
        print(f"Current available ingredients:")
        coffee_maker.report()
        drink = input(f"\nWhat drink would you like today ?\nAvailable drinks: {menu.get_items()}\n").lower()
        if drink == 'report':
            money_machine.report()
        elif drink == 'off':
            quit()
        elif drink in list(menu.get_items().split("/")):
            if coffee_maker.is_resource_sufficient(menu.find_drink(drink)):
                drink = menu.find_drink(drink)
                break
            else:
                pass
        else:
            print("wrong input please try again")
            clear()
            continue

    print(f"\n{drink.name} costs ${drink.cost}.\n")

    while True:
        if money_machine.make_payment(drink.cost):
            break
        else:
            continue

    print("\nbrewing ...\n")
    sleep(2)
    coffee_maker.make_coffee(drink)
    sleep(5)
    clear()

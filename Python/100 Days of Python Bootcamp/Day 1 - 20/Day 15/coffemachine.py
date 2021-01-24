'''
------------------------------------------------------------------------------ 
BlackJack Game
Coded By : Gary. K
Language : Python
------------------------------------------------------------------------------
Description :
**WIP**
offline higher or lower game replica.
------------------------------------------------------------------------------
/////////d0ntblink\\\\\\\\\\
\\\\www.dontblink.ca////
------------------------------------------------------------------------------
'''
###LIBERARIES########################################################################################################################################################
from art import logo, coffee
from lists import coins, resources, MENU
from os import system
from time import sleep
import string, random
###CONSTANTS########################################################################################################################################################
greeting ="""
        /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
What would you like today ?
    1. Espresso
    2. Cappuccino
    3. Latte

Additionally you can type:
    1. Off: to turn off the machine
    2. Report: to display the remaining resources
"""
error = "invalid input, please try again\n"
###FUNCTIONS########################################################################################################################################################
def report():
    global MONEY
    print(f"""
Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${MONEY}
""")


def clear():
    system('cls||clear')


def menu_selection():
    global MONEY
    selected_item = input(greeting).lower().strip(" ")
    while True:
        if selected_item in MENU:
            clear()
            prompt, ingredient = check_resources(selected_item)
            if prompt == "error":
                selected_item = input(f"Sorry I don't have enough {ingredient} for {selected_item}\n{greeting}")
                continue
            elif prompt == "ok":
                print(f'One {selected_item} costs ${MENU[selected_item]["cost"]}')
                while MONEY < MENU[selected_item]["cost"]:
                    insert_coin()
                    clear()
                    print(f'You\'ve inserted ${MONEY}')
                    if MONEY < MENU[selected_item]["cost"]:
                        print(f'You\'re still missing another ${MENU[selected_item]["cost"] - MONEY}')
                        continue
                    else:
                        break
                deduct_resources(selected_item)
                MONEY -= MENU[selected_item]["cost"]
                print("Brewing......")
                sleep(1)
                print("Pouring......")
                sleep(1)
                print(coffee)
                print(f'Your {selected_item} is ready.\nEnjoy!\n')
                if input('Would you like to order another coffee ? ') == "yes":
                    clear()
                    menu_selection()
                else:
                    clear()
                    print(f'Here is your change: ${MONEY}\nDont forget to take it!')
                    MONEY = 0
                    menu_selection()
        elif selected_item == "off":
            print("Goodbye!")
            clear()
            quit()
        elif selected_item == "report":
            report()
            selected_item = input()
            continue
        else:
            selected_item = input(error)


def check_resources(coffeetype):
    for ingredient, ml in MENU[coffeetype]["ingredients"].items():
        if resources[ingredient] - ml > 0:
            pass
        else:
            return "error", ingredient
    return "ok", "nothing"


def deduct_resources(coffeetype):
        for ingredient, ml in MENU[coffeetype]["ingredients"].items():
            resources[ingredient] -= ml


def insert_coin():
    global MONEY
    print("\nPlease insert your coins one at a time.\nType done when you are finished.\n")
    while True:
        coin = input().lower().strip(" ")
        if coin == "done":
            break
        elif coin in coins:
            MONEY += coins[coin]
        else:
            print(f'invalid coin!\nplease note that this machine only accpets american {", ".join([coin for coin in coins])}.')
            continue


###VARIABLES########################################################################################################################################################
MONEY = 0
###PROGRAM START########################################################################################################################################################
clear()
print(logo)
menu_selection()

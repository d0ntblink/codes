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
import string, random
from os import system
from art import logo, vs
from accounts import data
###FUNCTIONS########################################################################################################################################################
def clear():
    system('cls||clear')

def pullaccount():
    name, followers, description, country =random.choice(data).items()
    return name[1], followers[1],description[1],country[1]

def choose():
    while True:
        userschoice = input("\nHeigher or lower ? ").lower()
        if userschoice == 'heigher' or userschoice == 'lower' :
            return userschoice
        else:
            print("Invalid input, try again.")

def setup():
    global POINTS, NAME, DESCRIPTION, COUNTRY, FOLLOWERS
    if POINTS == 0:
        name, followers, description, country = pullaccount()
        NAME, FOLLOWERS, DESCRIPTION, COUNTRY = pullaccount()
        while NAME == name:
            NAME, FOLLOWERS, DESCRIPTION, COUNTRY = pullaccount()  
    else :
        name, followers, description, country = NAME, FOLLOWERS, DESCRIPTION, COUNTRY
        NAME, FOLLOWERS, DESCRIPTION, COUNTRY = pullaccount()
        while NAME == name:
            NAME, FOLLOWERS, DESCRIPTION, COUNTRY = pullaccount()
    display(name=name, description=description, followers=followers, country=country, show=True)
    print(vs)
    display(name=NAME, description=DESCRIPTION, followers=FOLLOWERS, country=COUNTRY, show=False)
    return name, followers

def display(name, description, followers, country,show):
    print(f"""   {name}\n   {description}\n   from {country}""")
    if show == True:
        print(f"""\n   {followers}000 followers""")
    else:
        print(f"""\n   XXXXXX followers """)

def game():
    global POINTS, NAME, DESCRIPTION, COUNTRY, FOLLOWERS
    name, followers = setup()
    userschoice = choose()
    clear()
    print(logo)
    if followers > FOLLOWERS :
        actualanswer = 'lower'
    elif followers < FOLLOWERS :
        actualanswer = 'heigher'
    if userschoice == actualanswer:
        print("\nyou are correct!!:D")
        print(f"\n{name} has {followers}000 followers\n{NAME} has {FOLLOWERS}000 followers\n")
        POINTS += 1
        print(f"\nYou currently have {POINTS} point(s).\n")
    else:
        print("\nyou lost D:")
        print(f"\n{name} has {followers}000 followers\n{NAME} has {FOLLOWERS}000 followers\n")
        print(f"\nYou ended the game with {POINTS} point(s).\n")
        POINTS = 0
###VARIABLES########################################################################################################################################################
NAME, DESCRIPTION, COUNTRY, FOLLOWERS = '', '', '', ''
POINTS = 0
###GAME START########################################################################################################################################################
while True:
    clear()
    print(logo)
    game()
    while POINTS > 0:
        game()
    if input("Would you like to try again ? (yes/[no]) ").lower() == 'yes':
        continue
    else:
        print("good bye")
    break
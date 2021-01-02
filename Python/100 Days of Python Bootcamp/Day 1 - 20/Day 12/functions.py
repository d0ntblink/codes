'''
------------------------------------------------------------------------------ 
Guess the Number
Coded By : Gary. K
Language : Python
------------------------------------------------------------------------------
Description : 
Guess the number game
------------------------------------------------------------------------------
/////////d0ntblink\\\\\\\\\\
\\\\www.dontblink.ca////
------------------------------------------------------------------------------
'''
###LIBERARIES########################################################################################################################################################
from os import name, system
from random import randint
from art import banner
from time import sleep
###VARIABLES########################################################################################################################################################
LIVES = 0
WIN = False
NUMBER = 0
MODE = ''
GUESS = 0
MODES = ['easy', 'medium', 'hard', 'extreme']
###FUNCTIONS########################################################################################################################################################
def clear():
    '''
    clears the terminal
    '''
    if name == 'nt' :
        system('cls')
    else :
        system('clear')

def randnum(mode):
    '''
    chooses a random number base on the mode.
    extreme = 0 to 1000
    easy and hard = 0 to 100
    '''
    if mode == 'extreme' :
        num = randint(0, 1001)
    else :
        num = randint(0, 101)
    return num

def lives(mode):
    '''
    chooses number of lives based on the mode
    '''
    if mode == 'easy' :
        lives = 10
    elif mode == 'medium' :
        lives = 7
    elif mode == 'hard' or mode == 'extreme' :
        lives = 5
    return lives

def checkguess(guess, number):
    '''
    checks to see if the guess is correct
    '''
    global LIVES, WIN
    if guess == number :
        WIN = True
        LIVES = 0
    elif guess > number :
        print("Go lower !")
        LIVES -= 1
        print("%d lives left" % LIVES)
    elif guess < number :
        print("Go higher !")
        LIVES -= 1
        print("%d lives left" % LIVES)

def playagain():
    '''
    Reloads the game
    '''
    if input("\nwould you like to play again ?(Y/N)(defaut = N) ").lower() == "y" :
        guess_the_number()
    else :
        quit()

def guess_the_number():
    '''
    game start
    '''
    global LIVES, WIN, NUMBER, MODE, GUESS
    while True :
        clear()
        print(banner)
        MODE = input('''Choose a difficulty setting :
        Easy : between 0 to 100 with 10 guesses
        Medium : between 0 to 100 with 7 guesses
        Hard : between 0 to 100 with 5 guesses
        Extreme : between 0 to 1000 with 5 guesses
        Type mode here -> : ''').lower()
        if MODE in MODES :
            pass
        else :
            print("invalid response")
            sleep(1)
            continue
        WIN = False
        NUMBER = randnum(mode=MODE)
        LIVES = lives(mode=MODE)
        print("\n\n\n------------------------------<LETS START!>-------------------------------\n%d lives left" % LIVES)
        while LIVES > 0 :
            GUESS = int(input("Guess a number : "))
            checkguess(guess=GUESS,number=NUMBER)
        if WIN : 
            print("Great guess !!\nYou won")
            playagain()
        else :
            print(f"Good Try but you didnt guess the correct number\nNumber was {NUMBER}")
            playagain()
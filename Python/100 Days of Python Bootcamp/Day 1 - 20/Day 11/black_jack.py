'''
------------------------------------------------------------------------------ 
BlackJack Game
Coded By : Gary. K
Language : Python
------------------------------------------------------------------------------
Description : 
BlackJack game with randomized results
------------------------------------------------------------------------------
/////////d0ntblink\\\\\\\\\\\
\\\\www.dontblink.ca////
------------------------------------------------------------------------------
'''
###LIBERARIES########################################################################################################################################################
import random
from os import name, system
from time import sleep
from art import logo, hand
###FUNCTIONS########################################################################################################################################################
def clear():
    '''clears the console'''
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def hit():
    '''draws a single untaken card'''
    while True:
        suit = random.choice(suits)
        card, val = random.choice(list(cards.items()))
        drawn_card = card + " of " + suit
        if drawn_card in drawn_cards :
            if len(drawn_cards) < 52:
                continue
            else :
                print("Dealer is out of cards")
                quit()
        drawn_cards.append(drawn_card)
        sleep(.5)
        return drawn_card, suit, card, val

def pchit():
    '''pc gets a card'''
    global pcval
    drawn_card, suit, card, val = hit()
    print("\nOne card to the dealer")
    pcval += val
    if card == "Ace" and pcval > 21 :
        pcval -= 10
    pccards.append(drawn_card)

def playerhit():
    '''player gets a card'''
    global playerval
    drawn_card, suit, card, val = hit()
    print(f"\n{drawn_card} to you")
    playerval += val
    if card == "Ace":
        if input(f"what value would you like to user for it ?(1/11) ") == "1":
            playerval -= 10
    playercards.append(drawn_card)

def showplayercard():
    print(hand)
    print("\nYour current cards are : ")
    for card in playercards:    print(card, end=' | ')

def showpccards(reveal):
    if reveal == "all" :
        print("\nDealers cards are : ")
        for card in pccards:    print(card, end=' | ')
    if reveal == "some" :
        print(f"\nDealers revealed card is : \n{pccards[1]}")

def hitorstand():
    while True:
        showplayercard()
        showpccards(reveal="some")
        hitorstand = input("\nDo you want to hit or stand ?(hit/stand) ").lower()
        if hitorstand == "hit" :
            playerhit()
            if playerval < 21:
                continue
            else :
                break
        elif hitorstand == "stand" :
            break
        else :
            print("invalid response")
            continue

def playagain():
    if input("\nwould you like to play again ?(Y/N)(defaut = N) ").lower() == "y" :
        blackjack()
    else :
        quit()

def blackjack():
    global drawn_cards, pcval, pccards, playercards, playerval
    drawn_cards = []
    pcval = 0
    pccards = []
    playerval = 0
    playercards = []
    clear()
    print(logo)
    print("Welcome to the game of BlackJack")
    print("\nSHUFFLING ..........")
    sleep(3)
    playerhit()
    pchit()
    playerhit()
    pchit()
    hitorstand()
    if playerval > 21 :
        print(f"""\nyour total card vlaue({playerval}) went over\nDealer won.""")
        playagain()
        return
    while pcval < 16:
        pchit()
    showplayercard()
    showpccards(reveal="all")
    print(f"""\nYour total card value is {playerval}\ndealer's total card value is {pcval}""")
    if pcval > 21 :
        print("Dealer went over 21,\nYou won.")
        playagain()
    elif playerval == pcval :
        print("You and delaer are tied.")
        playagain()
    elif playerval == 21 :
        print("You win with a BlackJack.")
        playagain()
    elif pcval == 21 :
        print("Dealer wins with a BlackJack")
        playagain()
    elif (21 - playerval) < (21 - pcval) :
        print("You win.")
        playagain()
    else :
        print("Dealer wins.")
        playagain()
###LISTS########################################################################################################################################################
suits = ['♣Clubs♣','♦Diamonds♦','♥Hearts♥','♠Spades♠']
cards = {
    'Ace': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
}
###VARIABLES########################################################################################################################################################
drawn_cards = []
pcval = 0
pccards = []
playerval = 0
playercards = []
###GAMESTART########################################################################################################################################################
blackjack()
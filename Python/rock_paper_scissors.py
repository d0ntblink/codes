import os
import random
import curses
import time
import formatter
#######
def winner(p3 , p4):
    if p3 == '1' :
        if p4 == '1' :
            print('draw!\n both players chose rock')
            pass
        if p4 == '2' :
            print('Player 2 Won This Round! ')
            scoreboard['Player2'] += 1
        if p4 == '3' :
            print('Player 1 Won This Round! ')
            scoreboard['Player1'] +=1
    if p3 == '2' :
        if p4 == '2' :
            print('draw!\n both players chose paper')
            pass
        if p4 == '1' :
            print('Player 2 Won This Round! ')
            scoreboard['Player2'] += 1
        if p4 == '3' :
            print('Player 1 Won This Round! ')
            scoreboard['Player1'] +=1
    if p3 == '3' :
        if p4 == '3' :
            print('draw!\n both players chose scissors')
            pass
        if p4 == '1' :
            print('Player 2 Won This Round! ')
            scoreboard['Player2'] += 1
        if p4 == '2' :
            print('Player 1 Won This Round! ')
            scoreboard['Player1'] +=1
objlist = ['rock','paper','scissors']
menu = ("1. Player vs Player\n"
        '2. Player vs CPU\n'
        '3. Quit\n'
        'Please choose an option by typing the number : ')
error = 'Please chose a number between 1-3'
objprompt = (' choose your object :\n1. Rock\n2. Paper\n3. Scissors\n')
scoreboard = {'Player1' : 0 , 'Player2' : 0}  
option = input(menu).strip()
while True :
    if option == '1' :
        roundnum = input('How many rounds would you like to play ?\n')
        for i in range(int(roundnum)) :
            p1 = input('Player1' + objprompt)
            print('You chose %s' % objlist[int(p1)-1])
            time.sleep(.5)
            os.system('cls||clear')
            p2 = input('Player2' + objprompt)
            print('You chose %s' % objlist[int(p2)-1])
            time.sleep(.5)
            os.system('cls||clear')
            winner(p1 , p2)
        os.system('cls||clear')
        print(scoreboard)
    elif option == '2' :
        print('CPU is player 2')
        roundnum = input('How many rounds would you like to play ?\n')
        for i in range(int(roundnum)) :
            p1 = input('Player1' + objprompt)
            print('You chose %s' % objlist[int(p1)-1])
            p2 = random.randrange(1,4)
            print('PLayer2 chose %s' % objlist[int(p2)-1])
            winner(p1 , p2)
        os.system('cls||clear')
        print(scoreboard)
    elif option == '3' :
        os.system('cls||clear')
        quit
    else :
        print(error)

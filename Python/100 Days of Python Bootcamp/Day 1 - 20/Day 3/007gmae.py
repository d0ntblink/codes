''''
Coded by Gary. K
16/12/2020
'''
import random


weapon = ""
dead = "007!! 007!! NOOOOOOOOOOOOOOOOOOOOOOOO"
win = "Congratulations agent 007 another mission well done."
nightis = False

print('''     0000             0000        7777777777777777/========___________
   00000000         00000000      7777^^^^^^^7777/ || ||   ___________
  000    000       000    000     777       7777/=========//
 000      000     000      000             7777// ((     //
0000      0000   0000      0000           7777//   \\\\   //
0000      0000   0000      0000          7777//========//
0000      0000   0000      0000         7777
0000      0000   0000      0000        7777
 000      000     000      000        7777
  000    000       000    000       77777
   00000000         00000000       7777777
     0000             0000        777777777''')

print('''Hello agen 007, Today I have another mission for you.
Poggers has been running around the city killing inocent poeple and we have to put a stop to this.
Your mission is to find and eleminate him''')
weapon = input('''please a chose a weapon : 
your options are : Pistol , Poison Pen , Bomb Jacket ''').lower()

dayornight = input('''Your intels tell you Pogger always hangs out at his private club, When do you wanna go there ? Night , Day ''').lower()
if dayornight == "day" :
    while True :
        whatdoday = input("Club is closed , do you wanna break in or wait untill night ? Break in . Wait ").lower()
        if whatdoday == "break in" :
            print("Pogger's goon see hear you whatdodayg in and shoot and kill you in sight")
            print(dead)
            break
        elif whatdoday == "wait" :
            nightis = True
            break
        else :
            print("invalid choice try again")
if dayornight == "night" or nightis == True :
    print('''You waite untill night comes and then blended in with the crowd and got in to the club,
    you see Pogger in the back of the club''')
    while True :
        cluboption = input("Get closer ? Attack him , Get closer ").lower()
        if cluboption == "get closer" :
            if weapon == "pistol" :
                print('''You get close to Pogger at the back of his club, the shoot him and all his goons the procede to leave the club''')
                print(win)
                break
            elif weapon == "bomb jacket" :
                print("One of Pogger's goons sees your bomb jacket and shoots and kills you")
                print(dead)
                break
            elif weapon == "poison pen" :
                print("You stab Poggers in the neck with your poison pen and kill him, but the his goons shoot and kill you")
                print(dead)
                break
        if cluboption == "attack him" :
            if weapon == "pistol" :
                print("You have 50%% chance of hitting him from the back of the club.")
                if random.getrandbits(1) == 1 :
                    print("BULLSEYE, you shoot him and run away")
                    print(win)
                    break
                else :
                    print("you miss ur shot and and get shot by Pogger's goons")
                    print(dead)
                    break
            if weapon == "bomb jacket" :
                print('''You explode your bomb jacket and kill your self , 
                but because your were so far away from Poggers he didnt die, 
                you died and still failed your misson''')
                print(dead)
                break
            if weapon == "poison pen" :
                print("you throw ur poision pen at Pogger but it doesnt reach, his Goons shoot and kill you")
                print(dead)
                break


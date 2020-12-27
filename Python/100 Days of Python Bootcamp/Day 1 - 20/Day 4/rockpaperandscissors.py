import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computerscore = 0
userscore = 0
options = [rock, paper, scissors]

while True :
    try :
        useroption = options[int(input("Choose your stnace : 1 for Rock , 2 for Paper, 3 for Scissors or type anything else to end the game ")) - 1 ]
        computeroption = random.choice(options)

        print(f"computer you chose\n{useroption} \ncomputer chose\n{computeroption}")

        if useroption == computeroption :
            print("its a tie")
        elif useroption == rock :
            if computeroption == paper :
                print("computer won")
                computerscore += 1
            else :
                print("you win")
                userscore += 1
        elif useroption == paper :
            if computeroption == scissors :
                print("computer won")
                computerscore += 1
            else : 
                print("you win")
                userscore += 1
        elif useroption == scissors :
            if computeroption == rock :
                print("computer won")
                computerscore += 1
            else : 
                print("you won")
                userscore += 1

        print(f"scoreboard \n   you : {userscore} computer : {computerscore}")
    except :
        break
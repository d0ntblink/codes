''' 
Programed by Gary.K
12/12/2019
'''
import csv
import time
import os
###########
def displayall() :
    with open('grades.csv','r') as file :
                csvfile = csv.reader(file)
                for row in csvfile :
                    print(row[0] , '|' ,  row[1] , '|'  , row[2] , '|'  , row[3] , '|' , row[4] , '|' , row[5])
                print()
def average() :
    #some value that i will need for future use in this function
    i = 0
    atten = 0
    zy = 0
    ass = 0
    mid = 0
    fin = 0
    with open('grades.csv' , 'r') as file :
                csvfile = csv.reader(file)
                for row in csvfile :
                    try :
                        atten += int(row[1])
                        zy += int(row[2])
                        ass += int(row[3])
                        mid += int(row[4])
                        fin += int(row[5])
                        i += 1
                    except Exception :
                        pass
                print("class average for attendece was %d" % (atten/i))
                print("class average for Zybooks was %d" % (zy/i))
                print("class average for Assignments was %d" % (ass/i))
                print("class average for Midterm was %d" % (mid/i))
                print("class average for Final was %d" % (fin/i))
                print()
def finalscore() :
    with open('grades.csv' , 'r') as file :
                csvfile = csv.reader(file)
                for row in csvfile :
                    try :
                        #finding the total final score
                        finalgrade = ((int(row[1]) * (0.05)) + (int(row[2]) * (0.15)) + (int(row[3]) * (0.30)) + (int(row[4]) * (0.25)) + (int(row[5]) * (0.25)))
                        print('%s\'s final grade is %0.2f' % (row[0] , finalgrade))
                    except Exception :
                        pass
                print()
error = ('file grades.csv is missing')
#menue prompt
menu = ("1. Display grade book\n"
        "2. Display average grade per category\n"
        "3. Display final grade per student\n"
        "4. Exit\n"
        "Please choose an option : ")
while True :
    #prompts menu
    command = input(menu).strip()
    #runs the program to display the grades table
    if command == '1' :
        print()
        try :
            displayall()
        #gets rid of errors
        except Exception :
            print(error)
            pass
    #displays average per category
    elif command == '2' :
        print()
        try :
            average()
        except Exception :
            print(error)
            pass
    #displays final grade per person
    elif command == '3' :
        print()
        try :
            finalscore()
        except Exception :
            print(error)
            pass
    #quits the program and deletes everything
    elif command == '4' :
        print('Bye :)')
        time.sleep(1)
        print('this was actually coded by Gary\'s codeing sugerdaddy dont believe his lies')
        time.sleep(0.25)
        os.system('cls||clear')
        break
    #prompts the user to put in the correct input
    else : 
        print('unrecognized command, please try again\n')
        time.sleep(1)

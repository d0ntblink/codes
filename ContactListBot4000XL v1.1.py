'''
Gary Khodayari
28/11/2019

'''
import os
import csv
import time
####
#I was having fun exploring some new library functions :)
print('Loading ..... ')
time.sleep(3)
print('You are logged as super agent %s' % os.getlogin())
time.sleep(0.5)
print('Hello, I am ContactListBot4000XL ver 1.1 \nhow can I help you ?')
time.sleep(1)
#menu options
menu_prompt = ("1. I want to add someone to the contact list\n"
                "2. Show me everyone in the contact list\n"
                "3. Find me someone in the contact list\n"
                "4. Quit\n")
while True :
    command = input(menu_prompt).strip() #calls for the menu options and records user's input
    if command == '1' : 
        with open('Contact_List.csv' , 'a') as file : #edits the existing file without getting rid of old data but if it doesnt exist it can make a new one
            csvfile = csv.writer(file) #reads the file
            nameNnum = [input('Enter the name : ') , input('Enter their number : ')] #creates an list with two inputs from the user
            csvfile.writerow(nameNnum) #writes the list into the file
    elif command == '2' :
        try :
            with open('Contact_List.csv' , 'r') as file : #opens the file just for reading purposes
                csvfile = csv.reader(file)
                print('Name : Phone number') #table header
                for row in csvfile :
                    try : #prints the rows in the csv file, one by one
                        print(row[0] , ':' , row[1])
                    except Exception: #ignores the errors , had to do it becasue csv files always have a new line at the end aparently so it messed with my indexes
                        pass
        except Exception :
            print('Oh no!!\nI think I\'ve lost my contact list :( \nLets create a new one!\n')
            pass
    elif command == '3' :
        try :
            with open('Contact_List.csv' , 'r') as file :
                csvfile = csv.reader(file, delimiter=',') #seprates the words from the csv
                name = input('Who are you looking for ?\n') #ask for the name
                nameinlist = False #resets the nameinlist to default (False)
                for row in csvfile : #checks every row for the name
                    if name in row : #prints the second word in that row
                        print(row[1])
                        nameinlist = True #sets nameinlist to True
                if nameinlist == False : #if nameinlist is False it will prompt the user
                    print('Sorry, I dont have any info for %s\n' % name)
        except Exception :
            print('Oh no!!\nI think I\'ve lost my contact list :( \nLets create a new one!\n')
            pass
    elif command == '4' : #exist the loop and clear the terminal
        print('Bye ! :D\n')
        time.sleep(2)
        os.system('cls||clear')
        break
    else : 
        print('Can you not read ?\n')
        time.sleep(5)
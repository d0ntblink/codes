'''
Gary Khodayari
11/28/2019
'''
total = 0 #will find the total percentage of all the grades
grades = [] #grades of the student will be added to this list by the user, one by one
#^ some variable and a list that I will be using later on
###
###
print("This program will calculate your average grade")
print("Please enter all your grades, one at a time,")
print("and when you are finished, press the 'Enter' key")
print()
###
###
grade = input("Please enter a grade: ")
while grade != "":
    ''' needed the user input to stay string for the "while loop condition" and float for the calculations'''
    if grade.isdigit() and (float(grade) <= 100) and (float(grade) >= 0) : #finds if the students entered grade is valid, netacad doesnt even have this !!
        grades.append(float(grade)) #adds each grade into a list
    else :
        print("invalid grade, try again") #user will be prompted if the entered grade is invalid
    grade = input("Please enter a grade: ") #program asks for another grade untill the user presses enter


for x in grades :
    total += x #adds each of the grades together to get all the grades total
avg = total / len(grades)#finds out how many grade were in entered by the user
print('%0.2f' % avg)#rounds to two decimal digits

'''avg = sum(grades) / (len(grades))
print(avg)''' #this is more efficient :D

student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'): \n"
name_prompt = "Enter name (Ex. Bob): \n"
error_prompt = "This name does not exist in the Gradebook!\n"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n")
while True:  # Exit when user enters no input
    command = input(menu_prompt).lower().strip()
    if command == '1':
        #splits the user's data to name and grade 
        name, grade = input(grade_prompt).split() 

        #if the entered name is already in the dictionary program will add the grade to the list of the grades under students name
        if name in student_grades : 
            student_grades[name].append(grade)
        #if the entered name is new to the dictionary it will create a list under the student's name
        else :
            student_grades[name] = [grade]
    elif command == '2':
        #if the entered name is already in the dictionary program deletes all the recorded data under the students name
        #if the entered name doesnt exist in the dictionary it will promp an error
        name = input(name_prompt).strip()
        print(student_grades.pop(name, error_prompt))
        '''if name in student_grades :
            del student_grades[name]
        else :
            print(error_prompt)'''
    elif command == '3':
        #if the entered name is already in the dictionary program prints the list of grades under the students name
        #if the entered name doesnt exist in the dictionary it will promp an error
        name = input(name_prompt).strip()
        print(student_grades.get(name, error_prompt))
        '''if name in student_grades :
            print(student_grades[name])
        else :
            print(error_prompt)'''
    # quits the program
    elif command == '4':
        print('Bye!')
        break
    #any other entry promptes an error
    else:
        print('Unrecognized command.')
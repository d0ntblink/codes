# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}
highest = 0
total = 0
i = 0
totalscore = 0
# finds the highest average with going trough each list indevidualy, calculating it average and then fids who had the highest average and records them
for name , s in student_grades.items() :
    avg = sum(s) / len(s)
    if avg > highest :
        beststudent = name 
        highest = avg
    else :
        continue
print(('%s has the highest percentage with average score of %0.1f%%') % (beststudent , highest))

''' 82.8 , 81.8 , 86.0 , 70.6 , 80.4 '''
# goes through each person recording only the socre for a certain test then moving to the next test
for x in range(len(student_grades)) :
    for tests in student_grades.values():
        totalscore += tests[i]
    i += 1
    print('class average for test# %d is %0.1f' % (i , (totalscore/len(student_grades))))#prints the average for each test
    totalscore = 0 # resets the total value to 0
 
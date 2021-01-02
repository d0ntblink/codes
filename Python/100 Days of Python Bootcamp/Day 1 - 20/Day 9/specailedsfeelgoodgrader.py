student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
'''Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"'''
#TODO-1: Create an empty dictionary called student_grades.
'''for student,score in student_scores.items() :
    if score > 90 :
        student_scores[student] = "Outstanding"
    elif score > 80 :
        student_scores[student] = "Exceeds Expectations"
    elif score > 70 :
        student_scores[student] = "Acceptable"
    else :
        student_scores[student] = "Fail"

student_grades = student_scores'''

student_grades = {}

for name in student_scores :
    score = student_scores[name]
    if score > 90 :
        student_grades[name] = "Outstanding"
    elif score > 80 :
        student_grades[name] = "Exceeds Expectations"
    elif score > 70 :
        student_grades[name] = "Acceptable"
    else :
        student_grades[name] = "Fail"

#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
print(student_grades)






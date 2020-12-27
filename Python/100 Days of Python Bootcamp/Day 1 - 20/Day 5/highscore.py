# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
maxscore = 0
print(f"heighest score is {max(student_scores)}")
for score in student_scores :
    if score > maxscore :
        maxscore = score
print(F"heighest score is {maxscore}")
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1.lower() + name2.lower()
t = "true"
l = "love"
tnum = 0
lnum = 0

for a in names :
    tnum += t.count(a)
    lnum += l.count(a)

tlnum = int(str(tnum) + str(lnum))

if tlnum > 90 or tlnum < 10 :
  print(f"Your score is {tlnum}, you go together like coke and mentos.")
elif tlnum > 40 and tlnum < 50 :
  print(f"Your score is {tlnum}, you are alright together.")
else :
  print(f"Your score is {tlnum}.")
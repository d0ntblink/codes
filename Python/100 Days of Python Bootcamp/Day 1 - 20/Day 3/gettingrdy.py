height = int(input("What is your height in cm? "))
if ( height >= 120 ) :
  print("Welcome to the rollercoaster!")
else : 
  print("No")

  # 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if (number % 2) == 0 :
  print("its even")
else :
  print("its Odd")

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
'''Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.'''

prompt = ""
bmi = (weight // (height ** 2))
if bmi < 18.5 :
  prompt = "under weight"
elif bmi < 25 :
  prompt = "normal weight"
elif bmi < 30 :
  prompt = "slightly overweight"
elif bmi < 35 :
  prompt = "obese"
elif bmi > 35 : 
  prompt = "critically obese"
print(f"your bmi is {bmi} and youre are {prompt}.")


while True :
  # 🚨 Don't change the code below 👇
  year = int(input("Which year do you want to check? "))
  # 🚨 Don't change the code above 👆

  #Write your code below this line 👇

  if year % 4 == 0 :
    if year % 100 == 0 :
      if year % 400 == 0 :
        isleap = True
      else : 
        isleap = False
    else :
      isleap = True
  else :
    isleap = False

  if isleap == True :
    print(f"year {year} is a leap year")
  else : 
    print(f"yaer {year} is not a leap year")



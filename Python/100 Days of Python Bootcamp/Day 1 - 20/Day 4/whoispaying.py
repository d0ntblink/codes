import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
"""Angela, Ben, Jenny, Michael, ChloeAngela, Ben, Jenny, Michael, Chloe
"""
#print("%s is paying for the meal" % names[4])

print("%s is paying for the meals today" % names[random.randint(0, len(names) - 1)])


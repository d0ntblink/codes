# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"1{row1}\n2{row2}\n3{row3}\n   1 ,   2 ,   3")
position = input("Where do you want to put the treasure?(ColumnRow) ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
map[int(position[0]) - 1][int(position[1]) - 1] = "❌"




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"1{row1}\n2{row2}\n3{row3}\n   1 ,   2 ,   3")

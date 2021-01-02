import os, art

def clear():
    os.system('cls||clear')

keepgoing = ""
entries = {}

while keepgoing != "no" :
    clear()
    print(art.logo)
    entries[input("What is your name ? ")] = int(input("How much are you bidding : $"))
    keepgoing = input("Are there any more bidders ? (yes/no)")

clear()
print(art.logo)
winner = max(entries, key=entries.get)
print(f"{winner} won the blind bidding with a bid of ${entries[winner]}")

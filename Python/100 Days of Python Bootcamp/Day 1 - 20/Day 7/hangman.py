import random, art, words, os, time

def stringfy(list):
    return (' '.join(list))

def screen() :
    os.system('cls||clear')
    print(art.logo)
    print(stringfy(display))
    print(art.stages[lives])
    print(f"lives left {lives}")

lives = 6
chosen_word = random.choice(words.word_list)
display = list(len(chosen_word) * "_")
screen()
while display != chosen_word and lives != 0 :
    guess = input("Guess a letter: ").lower()
    if guess not in display :
        if guess in chosen_word :
            for index in range(len(chosen_word)) :
                if chosen_word[index] == guess :
                    display[index] = guess
                else :
                    pass
        else :
            print("Wrong letter")
            lives -= 1
            time.sleep(.75)
    else :
        print(f"You've already guessed {guess}")    
        time.sleep(.75)
    screen()
    

if display == chosen_word :
    print("You've won")
else : 
    print("You've lost")
    print(f'the word was {chosen_word}.')
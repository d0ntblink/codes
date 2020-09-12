import os
#######
word = input('What is your word ?\n')
max_guesses = int(input('How many guesses can they make ?\n'))
os.system('cls||clear')
hidden_word = '-' * len(word)
guess = 1
print('You have %d guesses' % max_guesses)
while guess <= max_guesses and '-' in hidden_word:
    print(hidden_word)
    user_input = input('Enter a character (guess #%d): ' % guess)
    if len(user_input) == 1:
        num_occurrences = word.count(user_input)
        position = -1
        for occurrence in range(num_occurrences):
            position = word.find(user_input, position+1)
            hidden_word = hidden_word[:position] + user_input + hidden_word[position+1:]
        guess += 1
if not '-' in hidden_word:
    print('Winner!', end=' ')        
else:
    print('Loser!', end=' ')
print('The word was %s.' % word)

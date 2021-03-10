import random
from hangman_words import word_list
from hangman_stages import stages

chosen_word = random.choice(word_list)

player_lives = 6

display = []
for letter in chosen_word: 
    display += '_'

while ('_' in display) and (player_lives > 0):
    guess = input("Guess a letter: ").lower()
    for number in range(0, len(chosen_word)):
        if guess == chosen_word[number]:
            display[number] = guess
    if guess not in chosen_word:
        player_lives -= 1

    print(stages[player_lives])
    print(display)

if player_lives == 0:
    print(f"The word was {chosen_word.upper()}")
    print("You lose :(")
else:
    print("You Win :)")

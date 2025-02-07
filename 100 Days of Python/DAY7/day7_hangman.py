# Final code

import random 
from hangman_art import hangman, logo
from hangman_words import word_list

hangman.reverse()

chosen_word = random.choice(word_list)

print(logo)
print(chosen_word)

place_holder = ""
for letters in chosen_word:
    place_holder += "_"
print(place_holder)

game_over = False
correct_letters = []
lives = 6

while not game_over:

    print(f"-----------------------Lives left: {lives}----------------------")

    guess = input("Take a guess on a letter of the word: ").lower()

    if guess in correct_letters:
        print(f"You already try {guess}, try another letter")

    display = ""

    print(hangman[lives])

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_" 

    print(f"Word: {display}")

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word, you lose a life, try another one")
        if lives == 0:
            game_over = True
            print("--------------------------")
            print(f"You lose!, the correct word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("--------------------------")

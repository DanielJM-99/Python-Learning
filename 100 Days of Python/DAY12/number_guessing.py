# Number Guessing Game project 

#Generate random num 
import random 
random_num = random.randint(1, 100)

is_playing = True
guesses = int(input("How many guesses do you want?: "))

while is_playing:

    # Ask user for guess
    guess = int(input(f"Welcome to the Guessing Game: You have {guesses} guesses, choose wisely (1-100). \n Type your guess: "))

    # Give feedback to user
    if guess == random_num:
        print("You win!")
        is_playing = False
    elif guesses == 1:
        print("Sorry you lose!")
        print(f"The correct number was: {random_num}")
        is_playing = False
    elif random_num > guess:
        print("Too low")
        guesses -= 1
    elif random_num < guess:
        print("Too high")
        guesses -= 1
    
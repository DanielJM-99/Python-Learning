# Guessing number
import random 
from art import guess_numb_logo

# TODO 3 CREATE LIVES AND ASK USER IF EASY = 10 OR HARD = 5
LIVES_EASY = 10
LIVES_HARD = 5

def difficulty():
    level = input("Do you want the game to be easy or hard?  ").lower()
    if level == "easy":
        return LIVES_EASY
    else:
        return LIVES_HARD

# TODO 5  REDUCE LIVES AND IF HE IS RIGHT FINISH GAME
def check_guess(u_guess, r_guess, lives):
    if u_guess == r_guess:
        print("You win!")
        return lives - 11
    elif u_guess > r_guess:
        print("You are too high")
        return lives - 1
    else:
        print("You are too low")
        return lives - 1

def game():
    # TODO 1 WELCOME USER 
    print(guess_numb_logo)
    print("WELCOME TO THE NUMBER GUESSING GAME!")
    print("Im thinking of a number between 1-100")

    # TODO 2 RANDOMLY CHOOSE A NUMBER BETWEEN 1-100
    random_number = random.randint(1, 100)

    # TODO 4 CREATE WHILE LOOP TO KEEP ASKING USER FOR NUMBER, GIVE CLUES IF TOO HIGH OR TOO LOW
    keep_guessing = True

    lives = difficulty()

    print(random_number)

    while keep_guessing:
        print("---------------------------")
        print(f"You have {lives} lives left")

        guess = int(input("Take a guess: "))
        turns = check_guess(guess, random_number, lives)
        if turns == 0:
            print(f"Sorry you run out of lives the correct answer was: {random_number}")
            keep_guessing = False
        elif turns < 0:
            keep_guessing = False

game()
# Higher lower gamer 1.0

# TODO 1 PRINT LOGO AND IMPORT RANDOM, ART AND DATA
import random
from art import higher_lower_logo, vs_logo
from game_data import data

print(higher_lower_logo)

# TODO 2 FUNCTION TO RANDOMLY SELECT PIECE OF DATA
def get_data(list_of_data):
    """Returns a randomly choosen data from a list"""
    random_num = random.randint(0, len(list_of_data) - 1)
    choosen_data = list_of_data[random_num]
    return choosen_data
    
player1_data = get_data(data)
correct_asnwers = True
score = 0

while correct_asnwers:

    # TODO 6 SHOW SCORE
    if score > 0:
        print(f"You are right! Current Score: {score}")

    # print(player1_data["follower_count"])

    # TODO 3 TRANSFORM FROM LIST -> DICTIONARY -> STRING/INT -> PRINT STRING
    print(f"Compare A: {player1_data["name"]}, a {player1_data["description"]}, from {player1_data["country"]}.")

    print(vs_logo)

    player2_data = get_data(data)
    #print(player2_data["follower_count"])
    
    print(f"Compare B: {player2_data["name"]}, a {player2_data["description"]}, from {player2_data["country"]}.")

    # TODO 4 ASK USER TO GUESS AND FUNCTION TO COMPARE WITH ANSWER

    user_guess = input("Who has more instagram followers? Type 'A' or 'B':  ").upper()

    if user_guess == "A":
        if player1_data["follower_count"] > player2_data["follower_count"] or player1_data["follower_count"] == player2_data["follower_count"]:
            print("You are right")
            score += 1
        else:   # When player 1 is bigger than 2
            correct_asnwers = False
    elif user_guess == "B":
        if player2_data["follower_count"] > player1_data["follower_count"] or player1_data["follower_count"] == player2_data["follower_count"]:
            print("You are right")
            score += 1
        else:   # When player 2 is bigger than 1
            correct_asnwers = False

    # TODO 5 LOGIC TO REPLACE SECOND GUESS TO FIRST ONE
    player1_data = player2_data

    print("\n" *25)
    print("------------------------------")

    if correct_asnwers == False:
        print(higher_lower_logo)
        print(f"Sorry, you are wrong. Final Score: {score}")
    
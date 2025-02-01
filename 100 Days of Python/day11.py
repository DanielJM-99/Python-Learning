# Blackjack game 
import random 
import os
from art import blackjack_logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def chek_as_or_bj(list_cards, u_score, computer_cards, computer_score):
    if u_score > 21 and 11 not in list_cards:
        print("---------------------------------------------------------------")
        print(f"Your cards: {list_cards}, score: {sum(list_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("You went over the limit, You lose!")
        blackjack()
        return False
    else:
        if u_score > 21 and 11 in list_cards:
            for aces in range(len(list_cards)):
                if list_cards[aces] == 11:   # Looks for aces in list of cards
                    list_cards[aces] = 1     #Tranforms 11 into 1
        return True

def blackjack():

    user_answer = input("Do you want to play a game of BLACKJACK ? Type 'y' or 'n': ").lower()
    os.system("cls")

    print(blackjack_logo)
    print("WELCOME TO THE BLACKJACK GAME")

    if user_answer == "y":
        user_cards = []
        computer_cards = []

    # DEAL CARDS 
        for numbers in range(2):
            user_cards.append(random.choice(cards))

        computer_cards.append(random.choice(cards))

        keep_playing = True

        # CHECK CARDS 
        keep_playing = chek_as_or_bj(user_cards, sum(user_cards), computer_cards, sum(computer_cards))

        while keep_playing:

            print(f"Your cards: {user_cards}, score: {sum(user_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")

            one_more_hand = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if one_more_hand == "y":
                    user_cards.append(random.choice(cards))
                    keep_playing = chek_as_or_bj(user_cards, sum(user_cards), computer_cards, sum(computer_cards))
            else:
                    # Computer starts to play
                    computer_playing = True
                    while computer_playing:

                        if sum(computer_cards) < 17:
                            computer_cards.append(random.choice(cards))
                        else:
                            computer_playing = False
                        
                            computer_score = sum(computer_cards)
                            user_score = sum(user_cards)

                            print("---------------------------------------------------------------")
                            print(f"Your final hand: {user_cards}, final score: {user_score}")
                            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                            if user_score == computer_score:
                                print("Its a tie!")
                            elif user_score == 21:
                                print("You've just got a BlackJack! You win!")
                            elif computer_score == 21:
                                print("Computer got BlackJack! You lose!") 
                            elif computer_score > 21:
                                print("Computer went over, you win!")
                            elif user_score > computer_score:
                                print("You have won!")
                            else:
                                print("You lose!!")
                            keep_playing = False
                            blackjack()
        
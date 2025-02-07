# Angela's solution 

# Display art 
from art import higher_lower_logo, vs_logo
from game_data import data
import random

def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_descrip = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descrip}, from {account_country}. "

def check_answer(user_guess, a_followers, b_followers):
    """Take a users guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    
print(higher_lower_logo)
score = 0
game_schould_continue = True
account_b = random.choice(data)

# Make the game repeatable 
while game_schould_continue:

    # Generate a random account from the game data

    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs_logo)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear screen
    print("\n" * 20)
    print(higher_lower_logo)

    # Check if user is correct
    ## Get follower count of each account 
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    ## Use if statement to check if user is correct 
    # Score keeping
    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right! Current Score {score}")
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        game_schould_continue = False
#Project of the day 
import random 

# Assign asci art to var rock, paper, scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of options
rock_paper_scissors = [rock, paper, scissors]

# User and computer choices, use random choice to select var for you and computer
user_choice = int(input("What do you choose? Type 0 for Rock, 1 Paper, 2 Scissors: "))
computer_choice = random.choice(rock_paper_scissors)

# Index of choices
index_computer = rock_paper_scissors.index(computer_choice)

# Use if to get out of troubles if you have a bug
if 0 <= user_choice <= 2:
    print(rock_paper_scissors[user_choice])
    print("Computer chose: ")
    print(computer_choice)

# Create 3 rules to get who wins    
if user_choice > 2 or user_choice < 0:
    print("Invalid number. You lose!")
elif user_choice == 0 and index_computer == 2:
    print("You win!")
elif user_choice == 1 and index_computer == 0:
    print("You win!")
elif user_choice == 2 and index_computer == 1:
    print("You win!")
elif user_choice == index_computer:
    print("Its a tie")
else:
    print("You lose!")

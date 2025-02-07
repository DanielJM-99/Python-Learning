#Project of the day my solution

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
user = random.choice(rock_paper_scissors)
computer = random.choice(rock_paper_scissors)

# Index of choices
index_user = rock_paper_scissors.index(user)
index_computer = rock_paper_scissors.index(computer)

# Create 3 rules to get who wins
print(user)
print("Computer chose: ")
print(computer)
if index_user == 0 and index_computer == 2:
    print("You win!")
elif index_user == 1 and index_computer == 0:
    print("You win!")
elif index_user == 2 and index_computer == 1:
    print("You win!")
elif index_user == index_computer:
    print("Its a tie")
else:
    print("You lose!")

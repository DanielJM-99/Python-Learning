# Challenge day 5 password generator my solution

import random 

letters = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '.', '~', '|', '<', '>', '=', '-', '_', '/', ':', ';', '?', '[', ']', '{', '}', '~']

print("PASSWORD GENERATOR :V")
num_letters = int(input("How many letter in your password?: "))
num_numbers = int(input("How many numbers? "))
num_symbols = int(input("How many symbols? "))

# Easy level 
# Store random choice
users_choices = []

# Loop to get random choices 
for letter in range(0, num_letters):
    letter = random.choice(letters)
    users_choices.append(letter)

for letter1 in range(0, num_numbers):
    letter1 = random.choice(numbers)
    users_choices.append(letter1)

for letter2 in range(0, num_symbols):
    letter2 = random.choice(symbols)
    users_choices.append(letter2)

# Hard randomize choices
random.shuffle(users_choices)
print("".join(users_choices))
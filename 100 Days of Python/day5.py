# Challenge day 5 password generator 

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
password = ""

# Loop to get random choices 
for ch in range(0, num_letters):
    password += random.choice(letters) 

for ch in range(0, num_numbers):
    password += random.choice(numbers) 

for ch in range(0, num_symbols):
    password += random.choice(symbols) 

print(password)

# Hard randomize choices

password = []

# Loop to get random choices 
for ch in range(0, num_letters):
    # Can use += or .append()
    password += random.choice(letters) 

for ch in range(0, num_numbers):
    password += random.choice(numbers) 

for ch in range(0, num_symbols):
    password += random.choice(symbols) 

random.shuffle(password)

# Get final password
password1 = ""
for ch in password:
    password1 += ch

print(f"Your new password is: {password1}")
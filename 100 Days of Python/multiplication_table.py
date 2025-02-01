# Exercise Ask user for integer and give back the multiplication table 

user_num = int(input("What multiplication table do you want? Type any Integer:  "))

# Multiply every number with users number
for num in range(1, 11):
    print(f"{num} * {user_num} = ", num * user_num)


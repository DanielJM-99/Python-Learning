# 1: Open and close file
# file = open("Theory/read/write files/my_file.txt") 
# contents = file.read()
# print(contents)
# file.close()

# 2: Open file without need to close using 'with'
# with open("Theory/read/write files/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     file.close()

# 3: Write into a file (overwrites everything)
# with open("Theory/read/write files/my_file.txt", mode="w") as file:
#     file.write("New text.")

# 4: Append into a file 
# with open("Theory/read/write files/my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# 5: Write into file if it doesn't exists creates new file
with open("Theory/read/write files/new_file.txt", mode="w") as file:
    file.write("\nNew text.")

# file = open(r"C:\Users\T03USOH\OneDrive - NEW YORK LIFE INSURANCE COMPANY\Documents\Python-Learning\100 Days of Python\DAY24\my_file.txt")
# contents = file.read()
# print(contents)
# file.close

# with open(r"C:\Users\T03USOH\OneDrive - NEW YORK LIFE INSURANCE COMPANY\Documents\Python-Learning\100 Days of Python\DAY24\my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open(r"C:\Users\T03USOH\OneDrive - NEW YORK LIFE INSURANCE COMPANY\Documents\Python-Learning\100 Days of Python\DAY24\my_file.txt", mode="w") as file:
#     contents = file.write("New text")

#with open(r"C:\Users\T03USOH\OneDrive - NEW YORK LIFE INSURANCE COMPANY\Documents\Python-Learning\100 Days of Python\DAY24\my_file.txt", mode="a") as file:
#    contents = file.write("\nNew text")

# with open("./100 Days of Python/DAY24/new_file.txt", mode="w") as file:
#     file.write("First comment on new file on current dir, current folder day 24")

with open("../../Desktop/new_file.txt") as file:
    text = file.read()
    print(text)

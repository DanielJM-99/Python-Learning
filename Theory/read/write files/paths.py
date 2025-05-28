# Folders --> Files 

# Abolute file path
# /Root (Makintosh HD or C: Drive) --> /Root/Folder --> /Root/Folder/presentation.ppt

# Relative file path 
# if /Folder            is working directory then
# ./presentation.ppt    would be the relative path
# . dot represents current directory (working directory)
# .. goes back one folder up (step up)

# Absolute path ch 1 
# with open("/Users/T03USOH/OneDrive - NEW YORK LIFE INSURANCE COMPANY/Desktop/my_file.txt") as files:
#     content = files.read()
#     print(content)

# Relative path ch 2
with open("../../Desktop/my_file.txt") as files:
    contents = files.read()
    print(contents)

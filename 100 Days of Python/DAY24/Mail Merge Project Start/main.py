with open("./100 Days of Python/DAY24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
    print(content)

with open("./100 Days of Python/DAY24/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    all_names = names.readlines()
    print(all_names)


for name in all_names:
    new_name = name.strip()
    new_content = content.replace("[name]", new_name)
    with open(f"./100 Days of Python/DAY24/Mail Merge Project Start/Output/ReadyToSend/{new_name}.docx", mode="w") as invitations:
        invitations.write(new_content)

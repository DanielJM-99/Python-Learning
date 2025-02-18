from art import bj_cards

print(bj_cards[0])

cards = ["A", "1"]

new_card =""
for horizontal in range(0, 8): # From 0 -7
    if horizontal == 0:
        new_card += " "
    else:
        new_card += "-"
    for vertical in range(0, 6):
        if vertical == 0:
            new_card += "\n"
        elif vertical == 1:
            new_card += cards[0]
        else:
            new_card += "|\n"

print(new_card)

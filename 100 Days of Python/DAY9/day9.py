import art
import os

print(art.bid_logo)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def find_highest_bidder(bidding_dict):
    highest_bidder = ""
    highest_bid = 0
    for keys in bidding_dict:
            if bidding_dict[keys] > highest_bid:
                highest_bidder = keys
                highest_bid = bidding_dict[keys]

    print(f"The highest bidder is: {highest_bidder} with ${highest_bid}")

bidders = {}

more_bidders = True

while more_bidders:

    name = input("Your name: ")
    bid = float(input("Your bid: $"))

    # Store in dictionary with key as name
    bidders[name] = bid

    keep_bidding = input("Any other bidders? Typer 'Yes' or 'No'\n").lower()
    
    if keep_bidding == "yes":
        clear_screen()
    else:
        find_highest_bidder(bidders)
        more_bidders = False
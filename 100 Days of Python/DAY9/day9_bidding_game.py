# Final project bidding game

import art

# Print logo 
print(art.bid_logo)

# Create a dictionary to store values
bidders = {}
# While more_bids == True:
    #Ask users name, bid and if there is any other bidder
    # If yes
        #Clean screen 
    # Else
        # Finish bid and show winner

more_bidders = True
highest_bidder = ""
higest_bid = 0

while more_bidders:

    name = input("Your name: ")
    bid = float(input("Your bid: $"))

    # Store in dictionary
    bidders[name] = bid

    keep_bidding = input("Any other bidders? Typer 'Yes' or 'No'\n").lower()
    if keep_bidding == "yes":
        print("\n"*100)
    else:
        for keys in bidders:
            if bidders[keys] > higest_bid:
                highest_bidder = keys
                higest_bid = bidders[keys]
                
        print(f"The highest bidder is: {highest_bidder} with ${higest_bid}")
        more_bidders = False
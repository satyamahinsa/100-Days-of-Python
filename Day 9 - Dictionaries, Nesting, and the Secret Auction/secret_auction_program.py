import os
from secret_auction_art import logo
print(logo)

print("Welcome to the Secret Auction Program!")

def find_highest_bid(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        if bid_record[bidder] > highest_bid:
            highest_bid = bid_record[bidder]
            winner = bidder
    
    print(f"The winner is {winner} with a bid of {highest_bid}")

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
    if should_continue == "yes":
        os.system("cls")
    elif should_continue == "no":
        os.system("cls")
        bidding_finished = True
        find_highest_bid(bids)
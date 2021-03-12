print("Welcome to the secret Auction!")

in_progress = True
dict_bids = {}
highest_bid = 0
winner = ''

while in_progress:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))

    dict_bids[name] = bid

    more_bidders = input("Are there anymore bidders? 'yes' or 'no': ")
    if more_bidders == "no":
        in_progress = False

for bidder in dict_bids:
    if dict_bids[bidder] > highest_bid:
        highest_bid = dict_bids[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}")

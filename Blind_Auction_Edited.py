def bidding(bidding_list):
    highest = 0
    for x in bidding_list:
        if bidding_list[x] > highest:
            highest = bidding_list[x]
            highest_bidder = x
    print(f"Highest bidder is {highest_bidder}")
    print(f"Highest bid is {highest}")


bids = {}

situation = True
while situation == True:
    name = input("Enter your Name ")
    bid = int(input("Enter your bid "))
    bids[name] = bid
    conti = input("Are there other people? Yes/No ").lower()
    if conti == "no":
        situation = False
        bidding(bids)
    else:
        situation = True
        print("\n"*40)




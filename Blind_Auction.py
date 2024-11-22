import os

x = True
biding_dictionary = {}
while x == True:
    name = input("Enter name ")
    bid = int(input("Enter bid "))
    biding_dictionary[name] = bid
    #print(biding_dictionary) just for reference
    cont = input("are there other people? Yes or No? ").lower()
    if cont == "yes":
        x = True
        os.system('cls')
    else:
        x = False

highest = 0
winner = ""
for bider in biding_dictionary:

    amount = biding_dictionary[bider]
    if amount > highest:
        highest = amount
        winner = bider
print(f"winner is {winner}")
print(f"bid amount is {highest}")

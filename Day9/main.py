# TODO-1: Ask the user for input
# dict = {}
# while True:
#     user = input("Do you want to Continue: yes or no")
#     if user=='yes':
#         name=input("Enter a Bider name:\n")
#         bid= int(input("Enter the Bid"))
# # TODO-2: Save data into dictionary {name: price}
#
#         dict[name]=bid
# # TODO-3: Whether if new bids need to be added
#
#     else:
#         break
# # TODO-4: Compare bids in dictionary
#
# print(dict)
import art
print(art.logo)
dict = {}
def auction(names,bider):
    dict[name] = bider
while True:
    name = input("")
    bid = int(input(""))
    user = input("yes or no")
    auction(names=name,bider=bid)
    if user == 'no':
        winner = ''
        highest_bid = 0
        for bides in dick:
            bid_amnt = dict[bides]
            if bid_amnt>=highest_bid:
                highest_bid=bid_amnt
                winner = bides
        print(f"the maximum bid is {winner}")
        break
print(dict)


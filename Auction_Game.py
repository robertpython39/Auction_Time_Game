
#                                                                    ___Blind Auction Program___


# import time
#
# def countdown(t):
#     print("The dors are closed. The auction will began in 30 seconds...")
#     while t:
#         mins, secs = divmod(t, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat, end="\n")
#         time.sleep(1)
#         t -= 1
#
#
# countdown(30)
#
# print('''                ___________
#                          \         /
#                           )_______(
#                           |"""""""|_.-._,.---------.,_.-._
#                           |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\
#                          `'-------'`
#                        .-------------.
#                       /_______________\
#                       \n''')
#
# #
#bidding_open = True
# auction_members = {}
#
# while bidding_open:
#     bidder_name = input("Enter the name of the bidder: \n")
#     bid_ammount = int(input("Enter the bidding price: \n$"))
#     auction_members[bidder_name] = bid_ammount
#     add_another_bidder = input("Is there another bidder in this auction (yes/no):").lower()
#     while add_another_bidder != "no" and add_another_bidder != "yes":
#         print("Incorrect value entered \n")
#         add_another_bidder = input("Is there another bidder in this auction (yes/no):").lower()
#     if add_another_bidder == "no":
#         bidding_open = False
#
#
# max_bid = max(auction_members.values())
#
# winning_bidders = {}
#
# for key, values in auction_members.items():
#     if values == max_bid:
#         winning_bidders[key] = values
#
# print("The Winning Bidder(s): \n")
# for key, values in winning_bidders.items():
#     print(f"Bidder Name: {key} with the bid of ${values}")









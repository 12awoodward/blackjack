from deck import *

default = {
    "all" : {
        "A" : ["suit"],
        "2" : ["pickup_add_2"],
        "8" : ["skip"],
        "Q" : ["direction"],
    },
    "black" : {
        "J" : ["pickup_add_5"],
    },
    "red" : {
        "J" : ["pickup_set_0"],
    },
}

def main():
    new_deck = Deck()

main()
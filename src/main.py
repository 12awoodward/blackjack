from blackjack import *
from player import *

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
    players = [Player("CPU-1", True), Player("CPU-2", True), Player("CPU-3", True), Player("Player", False)]
    new_game = Blackjack(players, default)

main()
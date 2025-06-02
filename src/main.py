from blackjack import *
from player import *

from time import sleep

default = {
    "all" : {
        "A" : ["suit"],
        "2" : ["pickup_add:2"],
        "8" : ["skip"],
        "Q" : ["direction"],
    },
    "black" : {
        "J" : ["pickup_add:5"],
    },
    "red" : {
        "J" : ["pickup_set:0"],
    },
}

def set_name_spacing(player, size):
    player.display_name = player.name + " " * (size - len(player.name))

def hand_to_str(hand, hide = False):
    txt = ""
    sep = " | "
    hidden = "[?]"
    for card in hand:
        if hide:
            txt += hidden + sep
        else:
            txt += str(card) + sep
    return txt[:-len(sep)]

def get_str_player(player, hide = False, hand = None):
    if hand is None:
        hand = player.hand
    return player.display_name + ": " + hand_to_str(hand, hide)

def print_all_players(players, current_turn = -1, length = None):
    player_str = []
    if length is None:
        player_str = [get_str_player(player, player.is_computer) for player in players]
    else:
        player_str = [get_str_player(player, player.is_computer, player.hand[:length]) for player in players]
        
    size = len(max(player_str, key = lambda x : len(x)))

    txt = ""
    for i in range(len(player_str)):
        spacing = "\n"
        if i == current_turn:
            spacing += "-"*size + "\n"
        txt += spacing + player_str[i] + spacing
    txt += "\n"
    print(txt)

def print_card_dealing(players):
    for i in range(len(players[0].hand)):
        print_all_players(players, length = i + 1)
        sleep(0.3)

def main():
    players = [Player("CPU-1", True), Player("CPU-2", True), Player("CPU-3", True), Player("Player", False)]

    names = [player.name for player in players]
    size = len(max(names, key = lambda x : len(x)))
    for player in players:
        set_name_spacing(player, size)
    
    new_game = Blackjack(players, default)
    # print_card_dealing(new_game.players)

main()
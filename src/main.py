from time import sleep

from blackjack import *
from player import *

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
    # add spacing to match longest name
    player.display_name = player.name + " " * (size - len(player.name))    

def get_str_player(player, hide = False, hand = None, selectable = False):
    if hand is None:
        hand = player.hand

    txt = player.display_name + ": "
    sep = " | "
    hidden = "[?]"
    count = 1

    for card in hand:
        card_str = str(card)
        if hide:
            card_str = hidden
        if selectable:
            txt += f"{count}) "
            count += 1
        txt += card_str + sep

    return txt[:-len(sep)]

def print_all_players(players, current_turn = -1, length = None):
    player_str = []
    size = 0

    for i in range(len(players)):
        txt = ""
        # show card select options if not AI and current
        selectable = i == current_turn and not players[i].is_computer
        if length is None:
            # show players full hand
            txt = get_str_player(players[i], players[i].is_computer, selectable=selectable)
        else:
            # only show hands up to length
            txt = get_str_player(players[i], players[i].is_computer, players[i].hand[:length], selectable)
        
        #keep track of longest line
        if len(txt) > size:
            size = len(txt)
        
        player_str.append(txt)
    
    # apply current player marking
    if current_turn != -1:
        marking = "-" * size
        player_str[current_turn] = marking + "\n" + player_str[current_turn] + "\n" + marking

    print("\n" + "\n\n".join(player_str) + "\n\n")

def print_card_dealing(players):
    for i in range(len(players[0].hand)):
        print_all_players(players, length = i + 1)
        sleep(0.3)

def print_turn(game):
    status = f" Top Card: {str(game.top_card)}"

    if game.status["pickup"] > 0:
        status += "  - +" + str(game.status["pickup"])

    if game.status["skip"]:
        status += "  - Skip"

    direction = "\u21E9"
    if game.status["direction"] < 0:
        direction = "\u21E7"
    status += "  - " + direction

    spacing = "=" * len(status)
    print(f"{spacing}\n{status}\n{spacing}")
    print_all_players(game.players, current_turn=game.current_turn)

def main():
    # players = [Player("CPU-1", True), Player("CPU-2", True), Player("CPU-3", True), Player("Player", False)]
    players = [Player("Player", False), Player("Player 2", False), Player("Player 3", False)]

    # match player names to longest
    names = [player.name for player in players]
    size = len(max(names, key = lambda x : len(x)))
    for player in players:
        set_name_spacing(player, size)
    
    game = Blackjack(players, default)
    print_card_dealing(game.players)

    while True:
        print_turn(game)

        card = int(input("Enter card index: "))

        game.play_turn(card)

main()
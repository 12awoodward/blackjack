from blackjack import *
from player import *
from ui import *

rules = {
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

def main():
    # Placeholder
    players = [Player("CPU-1", True), Player("CPU-2", True), Player("CPU-3", True), Player("Player", False)]
    # players = [Player("Player", False), Player("Player 2", False), Player("Player 3", False)]

    # match player names to longest
    names = [player.name for player in players]
    size = len(max(names, key = lambda x : len(x)))
    for player in players:
        set_name_spacing(player, size)

    # pick rules

    # create players
    
    game = Blackjack(players, rules)
    print_card_dealing(game.players)

    while not game.game_over:
        current_player = game.players[game.current_turn]
        if current_player.is_computer or game.status["skip"]:
            non_playable_turn(game, current_player.is_computer)
        else:
            turn(game)
    
    print_winner(game.players[game.current_turn].name)

main()
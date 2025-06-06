from blackjack import *
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
    # pick rules

    players = create_players()
    
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
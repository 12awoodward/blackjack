from rule_files import *
from blackjack import *
from ui import *

def main():
    # pick rules
    rules = default

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
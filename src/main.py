from rule_files import *
from blackjack import *
from ui import *

def main():
    rules = default
    rule_dir_path = "rules"

    if is_rule_dir_valid(rule_dir_path):
        rule_list = get_all_rule_files(rule_dir_path)
        if len(rule_list) == 0:
            raise Exception("rules directory contains no .txt files")
        print(rule_list)
    
    else:
        print_message("No rules found / rules directory is invalid.\nUsing default rules.",)

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
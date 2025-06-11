from rule_files import *
from blackjack import *
from ui import *

def game_setup():
    rules = default
    rule_dir_path = "rules"

    if is_rule_dir_valid(rule_dir_path):
        rule_list = get_all_rule_files(rule_dir_path)

        if len(rule_list) == 0:
            raise Exception("rules directory contains no .txt files")
        
        rule_file_path = pick_rules(rule_list)
        rules = load_rules(rule_file_path)

        print_message(f"Loaded '{get_rule_name(rule_file_path)}' From '{rule_file_path}'")
    
    else:
        print_message("No Rules Found / Rules Directory Is Invalid.", will_wait=False)
        print_message("Loaded Default Rules")

    players = create_players()

    hand_size = set_hand_size()

    decks = set_deck_count(len(players), hand_size)
    
    return Blackjack(players, rules, decks, hand_size)


def game_loop(game):
    print_card_dealing(game.players)

    while not game.game_over:
        current_player = game.current_player()

        if current_player.is_computer or game.status["skip"]:
            non_playable_turn(game, current_player.is_computer)

        else:
            turn(game)
    
    print_winner(game.current_player().name)


def main():
    game_loop(game_setup())

main()
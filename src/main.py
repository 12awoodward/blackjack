from blackjack import Blackjack
from ui import *


def game_setup():
    rules_path = "rules"

    rules = get_rules(rules_path)

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
    
    winner = single_line_message(f"!!! {game.current_player().name} Wins !!!", sep="=")
    print(winner)


def main():
    game_loop(game_setup())


main()
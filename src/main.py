from blackjack import Blackjack
from ui import *


def game_setup():
    rules_path = "rules"

    rules = get_rules(rules_path)

    players = create_players()

    hand_size = set_hand_size()

    decks = set_deck_count(len(players), hand_size)
    
    return players, rules, decks, hand_size


def game_loop(players, rules, decks, hand_size):
    while True:
        game = Blackjack(players, rules, decks, hand_size)
        print_card_dealing(game.players)

        while not game.game_over:
            turn(game)
        
        winner = single_line_message(f"!!! {game.current_player().name} Wins !!!", sep="=")
        print(winner + "\n")
        wait()

        if play_again():
            for player in players:
                player.reset_hand()
        else:
            break


def main():
    game_loop(*game_setup())


main()
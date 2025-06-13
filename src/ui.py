from time import sleep

from ui_helpers import *
from player import Player
from rule_files import *

# Menu Timings
deal_time = 0.1


# Player Input Menus


def pick_rules(rule_list):
    choice = None
    rule_txt = list_choices([get_rule_name(rule) for rule in rule_list], "Available Rules")
    error = single_line_message("Invalid Choice")

    while choice is None:
        print(rule_txt)
        choice = get_player_choice(1, len(rule_list), "Pick Rules To Play With: ")

        if choice is None:
            print(error)
    
    return rule_list[choice - 1]


def set_player_name():
    name = ""
    error = single_line_message("Name Must Be 3-10 Characters Long")

    while len(name) > 10 or len(name) < 3:
        if len(name) > 0:
            print(error)

        name = input("\nEnter New Players Name: ")
        print("\n\n")

    return name


def create_players():
    players = []
    size = 0
    choices = ["Add Human Player", "Add Computer Player", "Start Game"]
    menu_txt = list_choices(choices, "Create Players")
    player_list = ""

    while True:
        # handle max players
        if len(players) == 10:
            print(single_line_message("Maximum Players Reached"))
            wait()
            break

        print(menu_txt)
        option = get_player_choice(1, 3, "Add Player? : ")

        if option is None:
            print(single_line_message("Invalid Input"))
            continue

        if option == 3:
            if len(players) >= 2:
                break
            else:
                print(single_line_message("Minimum 2 Players"))

        else:
            is_computer = option == 2
            players.append(Player(set_player_name(), is_computer))

            if len(players[-1].name) > size:
                size = len(players[-1].name)

            player_type = "Human"
            if is_computer:
                player_type = "Computer"
            
            player_list += f" {players[-1].name} : {player_type} |"

        if players:
            title = f"\n\nPlayers: {len(players)}"
            print(title + single_line_message(player_list[:-1], sep="="))

    # set player names to longest
    for player in players:
        set_name_spacing(player, size)
    
    return players


def set_hand_size():
    size = None
    default = 7
    minimum = 1
    maximum = 50

    message = single_line_message("Set Starting Hand Size")
    error = single_line_message(f"Must Be Between {minimum} And {maximum}")

    while size is None:
        print(message)
        size = get_player_choice(minimum, maximum, f"Press Enter For Default ({default}): ", default)

        if size is None:
            print(error)

    return size


def set_deck_count(player_count, hand_size):
    decks = None
    minimum = (((hand_size * player_count) + 20) // 52) + 1
    maximum = 19 # keep below 4 digit card count

    message = single_line_message("Number Of Decks Included")
    error = single_line_message(f"Must Be Between {minimum} And {maximum}")

    while decks is None:
        print(message)
        decks = get_player_choice(minimum, maximum, f"Press Enter For Minimum ({minimum}): ", minimum)

        if decks is None:
            print(error)

    return decks


def turn(game):
    current_player = game.current_player()
        # if current_player.is_computer or game.status["skip"]:
            # non_playable_turn(game, current_player.is_computer)

    hand_size = len(current_player.hand)

    state = game_state(game.top_card, game.status)
    player_list = all_player_hands(game.players, game.current_turn)
    hand_options = hand_select(len(current_player.display_name), hand_size)
    
    player_list.insert(game.current_turn + 1, hand_options)
    game_str = f"{state}\n{'\n'.join(player_list)}\n\n"

    while True:
        print(game_str)
        card = get_player_choice(0, hand_size, "Enter Move ( 0 - Pickup ): ")

        if card is None:
            print(single_line_message("Invalid Move"))
            continue

        card -= 1
        turn_result = game.play_turn(card)

        if turn_result == 0:
            # turn fail
            print(single_line_message(f"!!! {current_player.name} Cannot Play: {current_player.hand[card]} !!!"))

        else:
            # turn success
            break

    if card < 0:
        if game.was_deck_added():
            print(single_line_message("Not enough Cards: New Deck Added"))

        print(single_line_message(f"{current_player.name} Picked Up: ", current_player.last_pickup))

    else:
        print(single_line_message(f"{current_player.name} Played: " + str(game.top_card)))
    
    wait()
    
    if turn_result == 2:
        game.pick_suit(pick_suit_menu())

def non_playable_turn(game, computer = False):
    game_str = game_state(game.top_card, game.status) + "\n"
    game_str += "\n".join(all_player_hands(game.players, game.current_turn)) + "\n\n"
    print(game_str)
    wait()

    if game.status["skip"]:
        game.play_turn()

    elif computer:
        current_player = game.current_player()
        picked_up = current_player.computer_turn(game)

        if picked_up:
            if game.was_deck_added():
                    print(single_line_message("Not enough Cards: New Deck Added"))
            print(single_line_message(f"{current_player.name} Picked Up: ", current_player.last_pickup, hide_cards=True))

        else:
            print(single_line_message(f"{current_player.name} Played: " + str(game.top_card)))
        
        wait()


def pick_suit_menu():
    suit_list = [suit.value for suit in Suits]
    suit_txt = list_choices(suit_list, "Pick A Suit:")
    error = single_line_message("Invalid Choice")
    choice = None

    while choice is None:
        print(suit_txt)
        choice = get_player_choice(1, len(Suits), "Enter Suit: ")

        if choice is None:
            print(error)

    choice -= 1
    return Suits(suit_list[choice])


# Non Input Menus


def get_rules(rule_dir_path):
    rules = default_rules
    result = ""

    if is_rule_dir_valid(rule_dir_path):
        rule_list = get_all_rule_files(rule_dir_path)

        if len(rule_list) == 0:
            raise Exception("rules directory contains no .txt files")
        
        rule_file_path = pick_rules(rule_list)
        rules = load_rules(rule_file_path)

        result = single_line_message(f"Loaded '{get_rule_name(rule_file_path)}' From '{rule_file_path}'")
    else:
        result += single_line_message("No Rules Found / Rules Directory Is Invalid.")
        result += single_line_message("Loaded Default Rules")

    print(result)
    wait()
    return rules
    

def print_card_dealing(players):
    print()
    for i in range(len(players[0].hand)):
        for player in players:
            print(player_hand(player.hand[:i+1], player.display_name, player.is_computer))
            sleep(deal_time)
        sleep(deal_time)
        print()
    print("\n\n")
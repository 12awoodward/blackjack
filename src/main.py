from time import sleep

from blackjack import *
from player import *
from card import *
from deck import Suits

# Menu Timings
deal_time = 0.3
message_time = 0.8
state_time = 0.7


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

def print_message(txt, cards = []):
    if cards:
        join = " | "
        for card in cards:
            txt += str(card) + join
        txt = txt[:-len(join)]
    
    sep = "-" * len(txt)
    print(f"\n\n{sep}\n{txt}\n{sep}\n\n")
    sleep(message_time)

def print_winner(name):
    txt = f"!!! {name} Wins !!!"
    marking = "=" * len(txt)
    print(f"\n{marking}\n{txt}\n{marking}\n")

# print("          _1__|__2__|__3__|__4__|__5__|__6__|__7_")
# print("Player 3:  8♠ |  3♡ |  Q♡ |  2♢ | 10♢ |  J♢ |  4♣")
def get_str_player(player, hide = False, hand = None, selectable = False):
    if hand is None:
        hand = player.hand

    txt = player.display_name + ":"
    sel_txt = " " * len(txt)
    sep = "|"
    hidden = "[?]"
    count = 1

    for card in hand:
        card_str = str(card)
        if hide:
            card_str = hidden
        txt += f" {card_str} {sep}"

        if selectable:
            space = "_" * (4 - len(str(count)))
            sel_txt += f"{space}{count}_{sep}"
            count += 1

    if selectable:
        txt = sel_txt[:-len(sep)] + "\n" + txt
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
        
        #keep track of longest line - ignore extra selectable line
        line_len = len(txt.split("\n")[0])
        if line_len > size:
            size = line_len
        
        player_str.append(txt)
    
    # apply current player marking
    if current_turn != -1:
        marking = "-" * size
        player_str[current_turn] = marking + "\n" + player_str[current_turn] + "\n" + marking

    print("\n" + "\n\n".join(player_str) + "\n\n")

def print_card_dealing(players):
    for i in range(len(players[0].hand)):
        print_all_players(players, length = i + 1)
        sleep(deal_time)

def print_state(game):
    top_card = game.top_card
    if game.status["suit"] is not None:
        suit = Suits[game.status["suit"]]
        top_card = Card(suit, top_card.num)

    status = f" Top Card: {str(top_card)}"

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

def pick_suit_menu(game):
    suit_txt = "Pick A Suit: "
    suit_list = []
    count = 1
    for suit in Suits:
        suit_txt += f" {count}) {suit.value} "
        suit_list.append(suit)
        count += 1

    while True:
        print_message(suit_txt)

        try:
            choice = int(input("Enter Suit: "))
        except ValueError:
            print_message("Invalid Choice")
            continue

        choice -= 1
        if choice < 0 or choice >= len(Suits):
            print_message("Invalid Choice")
            continue

        game.pick_suit(suit_list[choice])
        break

def turn(game):
    current_player = game.players[game.current_turn]
    hand_size = len(current_player.hand)

    while True:
        print_state(game)
        sleep(state_time)

        try:
            card = int(input("Enter Move ( 0 - Pickup ): "))
        except ValueError:
            print_message("Invalid Move")
            continue

        if card < 0 or card > hand_size:
            print_message("Invalid Move")
            continue

        card -= 1
        turn_result = game.play_turn(card)
        if turn_result == 0:
            # turn fail
            print_message(f"!!! {current_player.name} Cannot Play: {current_player.hand[card]} !!!")
        else:
            # turn success
            if card < 0:
                print_message(f"{current_player.name} Picked Up: ", current_player.last_pickup)
            else:
                print_message(f"{current_player.name} Played: " + str(game.top_card))
            
            if turn_result == 2:
                pick_suit_menu(game)
            break

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

    while not game.game_over:
        current_player = game.players[game.current_turn]
        if current_player.is_computer:
            pass
        elif game.status["skip"]:
            print_state(game)
            sleep(state_time)
            game.play_turn()
        else:
            turn(game)
    
    print_winner(game.players[game.current_turn].name)

main()
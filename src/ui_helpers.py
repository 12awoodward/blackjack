from card import Card
from deck import Suits


def get_player_choice(min_val, max_val, prompt = "", default = None):
    choice = input(prompt)
    print("\n\n")

    try:
        choice = int(choice)
    
    except ValueError:
        if len(choice) == 0 and default != None:
            return default

        return None
    
    if choice > max_val or choice < min_val:
        return None
    
    return choice


def list_choices(options, title):
    title = f" {title} "
    sep = "-" * len(title)
    op_txt = "\n".join([f"  {i+1}) {options[i]}" for i in range(len(options))])

    return f"\n{sep}\n{title}\n{sep}\n{op_txt}\n{sep}\n"


def game_state(top_card, status):
    # if suit was changed, show top card as suit
    if status["suit"] is not None:
        suit = Suits[status["suit"]]
        top_card = Card(suit, top_card.num)

    state = f"Top Card: {str(top_card)}"

    if status["pickup"] > 0:
        state += "  - +" + str(status["pickup"])

    if status["skip"]:
        state += "  - Skip"

    direction = "\u21E9"
    if status["direction"] < 0:
        direction = "\u21E7"
    state += f"  - {direction}"

    return single_line_message(state, sep="=")


def all_player_hands(players, current_turn = -1):
    player_str = []
    size = 0

    for i in range(len(players)):
        # show players full hand
        txt = player_hand(players[i].hand, players[i].display_name, players[i].is_computer)
        
        #keep track of longest line
        if len(txt) > size:
            size = len(txt)
        
        player_str.append(txt)
    
    # apply current player marking
    if current_turn != -1:
        marking = "-" * size
        player_str.insert(current_turn + 1, marking)
        player_str.insert(current_turn, marking)

    return player_str


def player_hand(hand, name, hide = False):
    txt = f" {name}:"
    sep = "|"
    hidden = "[?]"

    for card in hand:
        if hide:
            card = hidden
        txt += f" {str(card)} {sep}"

    return txt[:-len(sep)]


def hand_select(name_len, hand_len):
    space = " " * (name_len + 2)
    options = ["_"*(4-len(str(i))) + f"{i}_" for i in range(1, hand_len+1)]
    return space + "|".join(options)


def single_line_message(txt, cards = [], hide_cards = False, sep = "-"):
    if cards:
        join = " | "
        hidden = "[?]"

        for card in cards:
            if hide_cards:
                card = hidden
            txt += str(card) + join

        txt = txt[:-len(join)]
    
    txt = f" {txt} "
    line = sep * len(txt)
    return f"\n{line}\n{txt}\n{line}\n"


def set_name_spacing(player, size):
    # add spacing to match longest name
    player.display_name = player.name + " " * (size - len(player.name)) 


def wait():
    input("Press Enter to Continue ")
    print("\n\n")
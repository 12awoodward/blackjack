from card import *
from deck import Suits


def get_player_choice(min_val, max_val, prompt = ""):
    try:
        choice = int(input(prompt))
    except ValueError:
        return None
    
    if choice > max_val or choice < min_val:
        return None
    
    return choice


# Print UI

        
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
    print(f"\n{spacing}\n{status}\n{spacing}")
    print_all_players(game.players, current_turn=game.current_turn)


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


# UI helpers


def set_name_spacing(player, size):
    # add spacing to match longest name
    player.display_name = player.name + " " * (size - len(player.name)) 


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


def wait():
    input("Press Enter to Continue ")
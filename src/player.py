# card sort key
def card_sort(card):
    val = card.num.value.strip()
    match val:
        case "A":
            val = 1
        case "J":
            val = 11
        case "Q":
            val = 12
        case "K":
            val = 13
        case _:
            val = int(val)
    return (card.suit.value, val)

class Player:
    def __init__(self, name, is_computer):
        self.name = name
        self.display_name = ""
        self.is_computer = is_computer

        self.hand = []
        self.last_pickup = []

    def take_cards(self, cards):
        self.hand += cards
        self.last_pickup = cards.copy()
        self.sort_hand()

    def sort_hand(self):
        self.hand.sort(key = card_sort)

    def play_card(self, card_index):
        return self.hand.pop(card_index)
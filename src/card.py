class Card:
    def __init__(self, suit, num, effects = [], is_pickup = False, is_suit_change = False):
        self.suit = suit
        self.num = num
        self.effects = effects

        # keep track of card properties for easier checks
        self.is_pickup = is_pickup
        self.is_suit_change = is_suit_change

    def __repr__(self):
        return f"{self.num.value}{self.suit.value}"
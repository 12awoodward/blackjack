class Card:
    def __init__(self, suit, num, effects = [], is_pickup = False):
        self.suit = suit
        self.num = num
        self.effects = effects
        self.is_pickup = is_pickup

    def __repr__(self):
        return f"{self.num.value}{self.suit.value}"
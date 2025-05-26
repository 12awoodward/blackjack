class Card:
    def __init__(self, suit, num, effects = []):
        self.suit = suit
        self.num = num
        self.effects = effects

    def __repr__(self):
        return f"{self.num.value} {self.suit.value}"
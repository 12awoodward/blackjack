class Player:
    def __init__(self, is_computer):
        self.hand = []
        self.is_computer = is_computer


    def take_cards(self, cards):
        self.hand += cards


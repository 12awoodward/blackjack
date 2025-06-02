class Player:
    def __init__(self, name, is_computer):
        self.name = name
        self.display_name = ""
        self.hand = []
        self.is_computer = is_computer

    def take_cards(self, cards):
        self.hand += cards


class Player:
    def __init__(self, name, is_computer):
        self.name = name
        self.display_name = ""
        self.hand = []
        self.is_computer = is_computer

    def set_name_space(self, names):
        size = len(max(names, key= lambda x : len(x)))
        self.display_name = self.name + " " * (size - len(self.name))

    def get_str_hand(self, hide = False):
        txt = ""
        sep = " | "
        hidden = "[?]"
        for card in self.hand:
            if hide:
                txt += hidden + sep
            else:
                txt += str(card) + sep
        return txt[:-len(sep)]
    
    def get_str_player(self, hide = False):
        return self.display_name + ": " + self.get_str_hand(hide)

    def take_cards(self, cards):
        self.hand += cards


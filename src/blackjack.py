from deck import *

class Blackjack:
    def __init__(self, players, rules):
        self.deck = Deck()
        self.top_card = None
        self.players = []
        self.current_turn = 0
        self.effects = {
            "pickup": 0,
            "direction": 1,
            "skip" : False,
            "suit" : None,
        }

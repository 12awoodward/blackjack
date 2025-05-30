from deck import *
from player import *

class Blackjack:
    def __init__(self, players, rules):
        self.deck = Deck()
        self.top_card = None
        self.players = [Player(comp) for comp in players]
        self.current_turn = 0
        self.effects = {
            "pickup": 0,
            "direction": 1,
            "skip" : False,
            "suit" : None,
        }

        self.initial_deal()

    def initial_deal(self, amount = 7):
        for i in range(amount):
            for player in self.players:
                player.take_cards(self.deck.draw_card())
                print(player.hand)
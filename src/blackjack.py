from deck import *
from player import *

class Blackjack:
    def __init__(self, players, rules):
        self.deck = Deck(rules)
        self.players = players
        self.current_turn = 0
        self.status = {
            "pickup": 0,
            "direction": 1,
            "skip" : False,
            "suit" : None,
        }

        self.initial_deal()
        self.top_card = self.deck.draw_card()

    def initial_deal(self, amount = 7):
        for i in range(amount):
            for player in self.players:
                player.take_cards(self.deck.draw_card())
    
    def next_turn(self):
        self.current_turn += self.status["direction"]

        if self.current_turn < 0:
            self.current_turn = len(self.players) - 1
        elif self.current_turn >= len(self.players):
            self.current_turn = 0

    def play_turn(self, card_index):
        card = self.players[self.current_turn].hand[card_index]
        print(card)
        self.next_turn()

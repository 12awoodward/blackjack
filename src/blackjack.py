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
        self.top_card = self.deck.draw_card()[0]

    def initial_deal(self, amount = 7):
        for player in self.players:
            player.take_cards(self.deck.draw_card(amount))
    
    def next_turn(self):
        self.current_turn += self.status["direction"]

        if self.current_turn < 0:
            self.current_turn = len(self.players) - 1
        elif self.current_turn >= len(self.players):
            self.current_turn = 0

    def play_turn(self, card_index):
        card = self.players[self.current_turn].hand[card_index]
        if self.can_play_card(card):
            pass
        print(card)
        self.apply_card_effects(card)
        self.next_turn()

    def can_play_card(self, card):
        if self.status["pickup"] == 0 and self.status["suit"] is None:
            if card.suit == self.top_card.suit or card.num == self.top_card.num:
                return True
            
        if self.status["pickup"] != 0 and self.status["suit"] is None:
            if card.is_pickup:
                if card.suit == self.top_card.suit or card.num == self.top_card.num:
                    return True
        
        if self.status["pickup"] == 0 and self.status["suit"] is not None:
            if card.suit.name.lower() == self.status["suit"] or card.num == self.top_card.num:
                return True
            
        if self.status["pickup"] != 0 and self.status["suit"] is not None:
            if card.is_pickup:
                if card.suit.name.lower() == self.status["suit"] or card.num == self.top_card.num:
                    return True
            
        return False

    def apply_card_effects(self, card):
        for effect in card.effects:
            effect(self.status)
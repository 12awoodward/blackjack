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
        if self.state["skip"]:
            self.next_turn()
            return
        
        current_player = self.players[self.current_turn]
        
        if card_index == -1:
            pickups = self.state["pickup"]
            if pickups == 0:
                pickups = 1
            current_player.take_cards(self.deck.draw_card(pickups))
            self.next_turn()
            return

        card = current_player.hand[card_index]
        if self.can_play_card(card):
            self.deck.return_to_deck(self.top_card)
            self.top_card = current_player.play_card(card_index)
            self.apply_card_effects(card)

            # handle suit change
            if self.status["suit"] == "set":
                self.status["suit"] = "spades"

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
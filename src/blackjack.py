from deck import *
from player import *

class Blackjack:
    def __init__(self, players, rules):
        self.game_over = False
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

    # returns 0 = turn fail, 1 = turn success, 2 = turn success - change suit
    def play_turn(self, card_index = -1):
        if not self.game_over:
            # turn was skipped
            if self.status["skip"]:
                self.status["skip"] = False
                self.next_turn()
                return 1
        
            current_player = self.players[self.current_turn]
            
            # player chose pickup
            if card_index == -1:
                pickups = self.status["pickup"]
                if pickups == 0:
                    pickups = 1
                current_player.take_cards(self.deck.draw_card(pickups))
                self.status["pickup"] = 0
                self.next_turn()
                return 1

            # player played a card
            card = current_player.hand[card_index]
            if self.can_play_card(card):
                self.deck.return_to_deck(self.top_card)
                self.top_card = current_player.play_card(card_index)
                self.apply_card_effects(card)

                # handle end game
                if len(current_player.hand) == 0:
                    self.game_over = True
                    return 1 # dont do next turn - current player is winner
                
                # handle suit change
                if self.status["suit"] == "set":
                    return 2
                
                #handle suit was changed
                if self.status["suit"] is not None:
                    self.status["suit"] = None

                self.next_turn()
                return 1
        return 0

    def can_play_card(self, card):
        # if no pickup
        if self.status["pickup"] == 0:

            # suit change can be played on any card
            if card.is_suit_change:
                return True
            
            # if suit was not changed
            if self.status["suit"] is None:
                if card.suit == self.top_card.suit or card.num == self.top_card.num:
                    return True
        
            # if suit was changed
            if self.status["suit"] is not None:
                if card.suit.name == self.status["suit"] or card.num == self.top_card.num:
                    return True
                
        # if there is pickup and is a pickup card
        elif card.is_pickup:
            
            # suit change can be played on any card
            if card.is_suit_change:
                return True
            
            # suit was not changed
            if self.status["suit"] is None:
                if card.suit == self.top_card.suit or card.num == self.top_card.num:
                    return True
              
            # suit was changed
            if self.status["suit"] is not None:
                if card.suit.name == self.status["suit"] or card.num == self.top_card.num:
                    return True
            
        return False
    
    def pick_suit(self, suit):
        if self.status["suit"] == "set":
            self.status["suit"] = suit.name
            self.next_turn()

    def apply_card_effects(self, card):
        for effect in card.effects:
            effect(self.status)
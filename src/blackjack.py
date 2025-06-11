from deck import Deck


class Blackjack:
    def __init__(self, players, rules, decks = 1, hand_size = 7):
        self.__deck = Deck(rules, decks)
        self.__deck_count = self.__deck.deck_count
        self.game_over = False
        self.players = players
        self.current_turn = 0
        self.status = {
            "pickup": 0,
            "direction": 1,
            "skip" : False,
            "suit" : None,
        }

        self.__initial_deal(hand_size)
        self.top_card = self.__deck.draw_card()[0]


    def __initial_deal(self, amount = 7):
        for player in self.players:
            player.take_cards(self.__deck.draw_card(amount))


    def __next_turn(self):
        self.current_turn += self.status["direction"]

        if self.current_turn < 0:
            self.current_turn = len(self.players) - 1

        elif self.current_turn >= len(self.players):
            self.current_turn = 0

    
    def current_player(self):
        return self.players[self.current_turn]


    # returns 0 = turn fail, 1 = turn success, 2 = turn success - change suit
    def play_turn(self, card_index = -1):
        if not self.game_over:

            # turn was skipped
            if self.status["skip"]:
                self.status["skip"] = False
                self.__next_turn()
                return 1
        
            current_player = self.current_player()
            
            # player chose pickup
            if card_index == -1:
                pickups = self.status["pickup"]
                self.status["pickup"] = 0

                if pickups == 0:
                    pickups = 1

                current_player.take_cards(self.__deck.draw_card(pickups))
                self.__next_turn()
                return 1

            # player played a card
            card = current_player.hand[card_index]
            if self.can_play_card(card):
                self.__deck.return_to_deck(self.top_card)
                self.top_card = current_player.play_card(card_index)
                self.__apply_card_effects(card)

                # handle end game
                if len(current_player.hand) == 0:
                    self.game_over = True
                    return 1 # dont do next turn - current player is winner
                
                # handle suit change played
                if self.status["suit"] == "set":
                    return 2
                
                #handle suit was changed
                if self.status["suit"] is not None:
                    self.status["suit"] = None

                self.__next_turn()
                return 1
        return 0


    def can_play_card(self, card):
        # if no pickup
        if self.status["pickup"] == 0:
            return self.__check_played_card(card)
                
        # if there is pickup and is a pickup card
        elif card.is_pickup:
            return self.__check_played_card(card)
            
        return False


    def __check_played_card(self, card):
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
    

    def was_deck_added(self):
        added = self.__deck.deck_count - self.__deck_count
        
        if added > 0:
            self.__deck_count += added
            return True
        else:
            return False


    def pick_suit(self, suit):
        if self.status["suit"] == "set":
            self.status["suit"] = suit.name
            self.__next_turn()


    def __apply_card_effects(self, card):
        for effect in card.effects:
            effect(self.status)
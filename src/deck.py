from enum import Enum
from random import shuffle

from card import Card
from card_effects import effect_alias


class Suits(Enum):
    SPADES = "\u2660"
    CLUBS = "\u2663"
    HEARTS = "\u2661"
    DIAMONDS = "\u2662"


class Numbers(Enum):
    ACE = " A"
    TWO = " 2"
    THREE = " 3"
    FOUR = " 4"
    FIVE = " 5"
    SIX = " 6"
    SEVEN = " 7"
    EIGHT = " 8"
    NINE = " 9"
    TEN = "10"
    JACK = " J"
    QUEEN = " Q"
    KING = " K"


class Deck:
    def __init__(self, rules, deck_count = 1):
        self.__rules = rules
        self.__deck = []
        self.deck_count = 0

        self.__gen_deck(deck_count)


    def __gen_deck(self, deck_count = 1):
        for i in range(deck_count):
            self.deck_count += 1
            
            for suit in Suits:
                color = "black"
                if suit == Suits.HEARTS or suit == Suits.DIAMONDS:
                    color = "red" 
                    
                for num in Numbers:
                    effects = []
                    num_str = num.value.strip()
                    suit_str = suit.name.lower()

                    key_check = ["all", color, suit_str]
                    for key in key_check:
                        if key in self.__rules:
                            if num_str in self.__rules[key]:
                                effects += self.__set_card_effects(self.__rules[key][num_str])
                    
                    self.__deck.append(Card(suit, num, effects))

        self.__shuffle_deck()
    

    def __set_card_effects(self, effects_to_apply):
        effects_applied = []

        for effect_rule in effects_to_apply:
            effect_parts = effect_rule.split(":")
            effect_name = effect_parts[0]


            if len(effect_parts) > 1:
                effect_arg = int(effect_parts[1])
                effect_val = effect_alias[effect_name][0]
                effect_func = effect_alias[effect_name][1](effect_arg)
                effects_applied.append((effect_val, effect_func))

            else:
                effects_applied.append(effect_alias[effect_name])

        return effects_applied


    def draw_card(self, count = 1):
        # not enough cards for pickup - add another deck
        if count > len(self.__deck):
            self.__gen_deck()

        draw = []
        for i in range(count):
            draw.append(self.__deck.pop())
        return draw


    def return_to_deck(self, card):
        self.__deck.append(card)
        self.__shuffle_deck()


    def __shuffle_deck(self):
        shuffle(self.__deck)
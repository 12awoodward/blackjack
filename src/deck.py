from enum import Enum
from random import shuffle

from card import *
from card_effects import *

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
        self.deck = []
        self.rules = rules
        self.gen_deck(deck_count)
    
    def gen_deck(self, deck_count = 1):
        for i in range(deck_count):
            for suit in Suits:
                color = "black"
                if suit == Suits.HEARTS or suit == Suits.DIAMONDS:
                    color = "red" 
                    
                for num in Numbers:
                    effects = []
                    is_pickup = False
                    num_str = num.value.strip()
                    suit_str = suit.name.lower()

                    key_check = ["all", color, suit_str]
                    for key in key_check:
                        if key in self.rules:
                            if num_str in self.rules[key]:
                                is_pickup, effect_funcs = self.set_card_effects(self.rules[key][num_str])
                                effects += effect_funcs
                    
                    self.deck.append(Card(suit, num, effects, is_pickup))

        self.shuffle_deck()
    
    def set_card_effects(self, effects):
        effect_funcs = []
        pickup = False # track if pickup rule is set
        for effect in effects:
            effect = effect.split(":")
            effect_name = effect[0]

            if "pickup" in effect_name:
                pickup = True

            if len(effect) > 1:
                effect_arg = int(effect[1])
                effect_func = lambda status: effect_alias[effect_name](status, effect_arg)
                effect_funcs.append(effect_func)
            else:
                effect_funcs.append(effect_alias[effect_name])

        return pickup, effect_funcs
            


    def draw_card(self, count = 1):
        draw = []
        for i in range(count):
            draw.append(self.deck.pop())
        return draw
    
    def return_to_deck(self, card):
        self.deck.append(card)
        self.shuffle_deck()
    
    def shuffle_deck(self):
        shuffle(self.deck)
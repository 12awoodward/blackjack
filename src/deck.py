from enum import Enum
from random import shuffle

from card import *

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
    def __init__(self, deck_count = 1):
        self.gen_deck(deck_count)
    
    def gen_deck(self, deck_count):
        self.deck = []
        for i in range(deck_count):
            for suit in Suits:
                for num in Numbers:
                    self.deck.append(Card(suit, num))
        self.shuffle_deck()

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
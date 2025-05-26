from enum import Enum

from card import *

class Suits(Enum):
    SPADES = "spades"
    CLUBS = "clubs"
    HEARTS = "hearts"
    DIAMONDS = "diamonds"

class Numbers(Enum):
    ACE = "A"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"

class Deck:
    def __init__(self, deck_count = 1):
        self.gen_deck(deck_count)
    
    def gen_deck(self, deck_count):
        self.deck = []
        for i in range(deck_count):
            for suit in Suits:
                for num in Numbers:
                    self.deck.append(Card(suit, num))
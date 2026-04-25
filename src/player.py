from __future__ import annotations
from typing import TYPE_CHECKING

from random import choice

from deck import Suits


# card sort key
def card_sort(card: Card):
    val = card.num.value.strip()
    match val:
        case "A":
            val = 1
        case "J":
            val = 11
        case "Q":
            val = 12
        case "K":
            val = 13
        case _:
            val = int(val)
    return (card.suit.value, val)


class Player:
    def __init__(self, name: str, is_computer: bool):
        self.name = name
        self.display_name = ""
        self.is_computer = is_computer

        self.hand: list[Card] = []
        self.last_pickup: list[Card] = []

    def take_cards(self, cards: list[Card]):
        self.hand += cards
        self.last_pickup = cards.copy()
        self.__sort_hand()

    def __sort_hand(self):
        self.hand.sort(key=card_sort)

    def play_card(self, card_index: int):
        return self.hand.pop(card_index)

    def reset_hand(self):
        self.hand = []
        self.last_pickup = []

    def computer_turn(self, game: Blackjack):
        playable: list[int] = []
        suit_count: dict[str, int] = {}

        # check which cards in hand can be played
        for i in range(len(self.hand)):
            if game.can_play_card(self.hand[i]):
                playable.append(i)

            # keep count of suits in hand
            if self.hand[i].suit.name in suit_count:
                suit_count[self.hand[i].suit.name] += 1
            else:
                suit_count[self.hand[i].suit.name] = 1

        move = -1
        if playable:
            move = choice(playable)

        result = game.play_turn(move)

        # played suit change
        if result == 2:
            # find most common suit in hand
            suit = max(suit_count, key=lambda x: suit_count[x])
            game.pick_suit(Suits[suit])

        if move == -1:
            return True
        return False


if TYPE_CHECKING:
    from blackjack import Blackjack
    from card import Card

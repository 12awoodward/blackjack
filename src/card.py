from __future__ import annotations
from typing import TYPE_CHECKING
from collections.abc import Callable


class Card:
    def __init__(
        self,
        suit: Suits,
        num: Numbers,
        effects: list[tuple[str, Callable[[GameStatus], None]]] = [],
    ):
        self.suit = suit
        self.num = num
        self.effects: list[Callable[[GameStatus], None]] = []

        # keep track of card properties for easier checks
        self.is_pickup = False
        self.is_suit_change = False

        self.__set_effects(effects)

    def __set_effects(self, effects: list[tuple[str, Callable[[GameStatus], None]]]):
        for effect in effects:
            self.effects.append(effect[1])

            if effect[0] == "suit":
                self.is_suit_change = True

            if effect[0] == "pickup":
                self.is_pickup = True

    def __repr__(self):
        return f"{self.num.value}{self.suit.value}"


if TYPE_CHECKING:
    from deck import Suits, Numbers
    from blackjack import GameStatus

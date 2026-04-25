from __future__ import annotations
from typing import TYPE_CHECKING
from collections.abc import Callable


def change_suit(status: GameStatus):
    status["suit"] = "set"


def change_direction(status: GameStatus):
    status["direction"] *= -1


def skip_turn(status: GameStatus):
    status["skip"] = True


def create_pickup_add(amount: int):
    def pickup_add(status: GameStatus):
        status["pickup"] += amount

    return pickup_add


def create_pickup_set(amount: int):
    def pickup_set(status: GameStatus):
        status["pickup"] = amount

    return pickup_set


BASE_EFFECT_ALIAS: dict[
    str,
    tuple[
        str,
        Callable[[GameStatus], None],
    ],
] = {
    "suit": ("suit", change_suit),
    "direction": ("direction", change_direction),
    "skip": ("skip", skip_turn),
}

SET_INT_EFFECT_ALIAS: dict[
    str,
    tuple[
        str,
        Callable[[int], Callable[[GameStatus], None]],
    ],
] = {
    "pickup_add": ("pickup", create_pickup_add),
    "pickup_set": ("pickup", create_pickup_set),
}


if TYPE_CHECKING:
    from blackjack import GameStatus

def change_suit(status):
    status["suit"] = "set"

def change_direction(status):
    status["direction"] *= -1

def skip_turn(status):
    status["skip"] = True

def pickup_add(status, amount):
    status["pickup"] += amount

def pickup_set(status, amount):
    status["pickup"] = amount

effect_alias = {
    "suit": change_suit,
    "direction": change_direction,
    "skip": skip_turn,
    "pickup_add": pickup_add,
    "pickup_set": pickup_set,
}
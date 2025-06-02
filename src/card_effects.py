def change_suit(effects):
    effects["suit"] = "set"

def change_direction(effects):
    effects["direction"] = effects["direction"] * -1

def skip_turn(effects):
    effects["skip"] = True

def pickup_add(effects, amount):
    effects["pickup"] += amount

def pickup_set(effects, amount):
    effects["pickup"] = amount

effect_alias = {
    "suit": change_suit,
    "direction": change_direction,
    "skip": skip_turn,
    "pickup_add": pickup_add,
    "pickup_set": pickup_set,
}
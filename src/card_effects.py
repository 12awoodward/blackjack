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
    "suit": ("suit", change_suit),
    "direction": ("direction", change_direction),
    "skip": ("skip", skip_turn),
    "pickup_add": ("pickup", pickup_add),
    "pickup_set": ("pickup", pickup_set),
}


def effect_has_arg(effect_name):
    if "pickup" in effect_name:
        return True
    return False
def change_suit(status):
    status["suit"] = "set"


def change_direction(status):
    status["direction"] *= -1


def skip_turn(status):
    status["skip"] = True


def create_pickup_add(amount):
    def pickup_add(status):
        status["pickup"] += amount
    
    return pickup_add


def create_pickup_set(amount):
    def pickup_set(status):
        status["pickup"] = amount

    return pickup_set


effect_alias = {
    "suit": ("suit", change_suit),
    "direction": ("direction", change_direction),
    "skip": ("skip", skip_turn),
    "pickup_add": ("pickup", create_pickup_add),
    "pickup_set": ("pickup", create_pickup_set),
}


def effect_has_arg(effect_name):
    if "pickup" in effect_name:
        return True
    return False
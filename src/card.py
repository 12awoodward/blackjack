class Card:
    def __init__(self, suit, num, effects = []):
        self.suit = suit
        self.num = num
        self.effects = []

        # keep track of card properties for easier checks
        self.is_pickup = False
        self.is_suit_change = False

        self.set_effects(effects)


    def set_effects(self, effects):
        for effect in effects:
            self.effects.append(effect[1])

            if effect[0] == "suit":
                self.is_suit_change = True
            
            if effect[0] == "pickup":
                self.is_pickup = True


    def __repr__(self):
        return f"{self.num.value}{self.suit.value}"
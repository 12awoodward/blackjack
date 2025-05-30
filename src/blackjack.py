from deck import *
from player import *

class Blackjack:
    def __init__(self, players, rules):
        self.deck = Deck()
        self.top_card = None

        self.players = players.copy()
        names = [player.name for player in self.players]
        for player in players:
            player.set_name_space(names)

        self.current_turn = 2
        self.effects = {
            "pickup": 0,
            "direction": 1,
            "skip" : False,
            "suit" : None,
        }

        self.initial_deal()

    def initial_deal(self, amount = 7):
        for i in range(amount):
            for player in self.players:
                player.take_cards(self.deck.draw_card())
            self.print_all_players()

    def print_all_players(self):
        player_str = [player.get_str_player(player.is_computer) for player in self.players]
        size = len(max(player_str, key = lambda x : len(x)))
        txt = ""
        for i in range(len(player_str)):
            spacing = "\n"
            if i == self.current_turn:
                spacing += "-"*size + "\n"
            txt += spacing + player_str[i] + spacing
        txt += "\n"
        print(txt)
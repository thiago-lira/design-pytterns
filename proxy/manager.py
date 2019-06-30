from contract import Contract
from player import Player


class Manager(Contract):
    def __init__(self):
        self.player = Player()

    def is_available(self):
        return self.player.is_available()

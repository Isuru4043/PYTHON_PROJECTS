import math
import random

class Player:
    def __int__(self,letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.availableSpaces())
        return square

class HumanPlayer(Player):
    def __int__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        pass

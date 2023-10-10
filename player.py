import math
import random


class Player:
    def __int__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.availableSpaces())
        return square


class HumanPlayer(Player):
    def __int__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            sqaure = input(self.letter + '\' s turn.Input move (0-9):')
            try:
                val = int(sqaure)
                if val not in game.availableSpaces():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid move.Try again.")

        return val




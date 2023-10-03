import random

def play():
    user = input("r,s,p")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return 'tie'

    if isWin(user,computer):
        print("You Won")
    return "You lost"


def isWin(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') \
        or (player == 's' and opponent == 'p'):
        return True


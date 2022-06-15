from random import random


import random

def play():
    user = input("'r' for rock, 'p' for paper or 's' for scissors:\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print('Tie, try again')
        play()

    if is_win(user, computer):
        return 'You win'
    return 'You lost'

def is_win(player, opponent):
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r') :
            return True

print(play())
import random

def play():
    user = input("What is your choice? 'r' for Rock, 'p' for Paper, and 's' for Scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, oppenent):
    if (player == 'r' and oppenent =='s') or (player == 's' and oppenent == 'p') \
        or (player == 'p' and oppenent == 'r'):
        return True

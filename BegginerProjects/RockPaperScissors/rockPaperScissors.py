import random

def play():
    user = input("What's your choice?\n'r' for rock\n'p' for paper\n's' for scissors\n: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
      return 'It\'s a tie!'

    if isWin(user, computer):
      return'You Won!'

    return 'You lost!'

def isWin(player, opponent):      
    # Return true if player wins
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
      return True

print(play())
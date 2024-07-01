import random

# User input's
def userInput():
  user = input("What's your choice?\n'r' for rock\n'p' for paper\n's' for scissors\n: ").lower()
  while user not in ['r', 'p', 's']:
    print('Invalid character! Please, try again.')
    user = input("What's your choice?\n'r' for rock\n'p' for paper\n's' for scissors\n: ").lower()
  return user

# Check if user is a winner
def userWin(user, computer):
  if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
    return True
  else:
    return False

# Print the result
def result(user, computer):
  if user == computer:
    return 'It\'s a tie!'
  elif userWin(user, computer):
    return 'You won!'
  else:
    return 'You lost!'

# Main program
def main():
  while True:
    user = userInput()
    computer = random.choice(['r', 'p', 's'])
    gameResult = result(user, computer)
    choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

    print(f'\nYou chose {choices[user]} and computer chose {choices[computer]}')
    print(gameResult)
    print('')

    if gameResult == 'You won!':
      break

if __name__ == "__main__":
  main()
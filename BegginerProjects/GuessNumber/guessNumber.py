import random

def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0
    while guess != randomNumber:
      guess = int(input(f'Guess a number betweem 1 and {x}: '))
      if guess < randomNumber:
        print('Sorry, guess again. Too low.')
      elif guess > randomNumber:
        print('Sorry, guess again. Too high.')
      
    print(f'Congratulations! You have guessed the number {randomNumber} correctly!')

print('Guess a number game: ')
guess(100)

def computerGuess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
      if low != high:
        guess = random.randint(low, high)
      else:
        guess = low # Could also be high because low = high
      feedback = input(f'Is {guess} to high (H), too low (L), or correct (C)? ').lower() # .lower() method converts the input to lowercase
      if feedback == 'h':
        high = guess - 1 # If the guess is too high, the upper limit is set to the guess - 1
      elif feedback == 'l':
        low = guess + 1
    
    print(f'Congratulations! The computer guessed your number {guess} correctly!')

print('\nComputer guess a number game: ')
computerGuess(100)
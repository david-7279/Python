import random
import string
from words import words

def getValidWord(words):
  word = random.choice(words) # Randomly chooses a word from the list
  while '-' in word or ' ' in word: 
    word = random.choice(words)
  
  return word.upper() # Returns the word that does not have '-' or ' '

def hangman():
    word = getValidWord(words)
    wordLetters = set(word)                     # Letters in the word
    alphabet = set(string.ascii_uppercase)      # All the letters in the alphabet
    usedLetters = set()                         # Letters the user has guessed

    lives = 6                                   # Number of lives the user has

    while len(wordLetters) > 0 and lives > 0:   # While the length of the wordLetters is greater than 0 and lives is greater than 0
      # Letters used
      print('You have', lives, 'lives left and you have used these letters: ', ' '.join(usedLetters))

      # Current word
      wordList = [letter if letter in usedLetters else '-' for letter in word]
      print('Current word: ', ' '.join(wordList))
      
      userLetter = input('\nGuess a letter: ').upper()
      if userLetter in alphabet - usedLetters:  # If the letter the user guessed is in the alphabet and not in the used letters
        usedLetters.add(userLetter)             # Add the letter to the user letters

        if userLetter in wordLetters:           # If the letter the user guessed is in the word
          wordLetters.remove(userLetter)        # Remove the letter from the wordLetters
          print('')

        else:
          lives = lives -  1                            # If the letter the user guessed is not in the word, the user loses a life
          print(f'Your letter {userLetter} is not in the word.')

      elif userLetter in usedLetters:           # If the letter the user guessed is in the used letters
        print(f'You have already used that character {userLetter}. Please try again.')
      
      else:                                     # If the letter the user guessed is not in the alphabet
        print(f'Invalid character {userLetter}. Please try again.')

    # Gets here when len(wordLetters) == 0 or when lives == 0
    if lives == 0:
      print(f'You have died! The word was {word}')
    else:
      print(f'You have guessed the word {word}')

hangman()
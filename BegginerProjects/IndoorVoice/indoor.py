import os
from time import sleep

def clearScreen():
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def userInput():
    try:
      word = input('Write an word to convert: ').strip().lower()
      return word
    except ValueError:
      print('Invalid word! Please, try again.')


def main():
    print('Welcome to Indoor Voice!\n')

    word = userInput()
    clearScreen()
    print('Converting ... ')
    clearScreen()
    print(f'Indoor word: {word}')

if __name__ == "__main__":
    main()
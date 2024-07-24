from time import sleep
import os
import time

def clearScreen():
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

def userOption():
    choices = ['L', 'S', 'E']

    while True:
      try:
        option = input('Choose an option: ').strip().upper()
        if option in choices:
          return option
        else:
          print(f'Invalid option {option}! Please, try again.')
      except ValueError as error:
        print(f'Invalid value {error}! Please, try again.')


def countDown(minutes, message):
    totalSeconds = minutes * 60
    while totalSeconds > 0:
      clearScreen()
      mins, sec = divmod(totalSeconds, 60)
      timer = '{:2d} {:2d}'.format(mins, sec)
      print(timer)
      sleep(1)
      totalSeconds -= 1
    clearScreen()
    print(message)
    sleep(2)
      

def longStudySession():
    countDown(60, "Study session over! Time for a 10-minute break.")
    countDown(10, "Break over! Time to get back to studying.")


def shortStudySession():
    countDown(25, "Study session over! Time for a 5-minute break.")
    countDown(5, "Break over! Time to get back to studying.")


def main():
    print('Welcome to Pomodoro Timer!')
    
    while True:
      print('\n(L)ong study session (1 hour studying and 10 minutes break)')
      print('(S)hort study session (25 minutes studying and 5 minutes break)')
      print('(E)xit the program')

      option = userOption()
      clearScreen()

      if option == 'L':
        longStudySession()
      elif option == 'S':
        shortStudySession()
      elif option == 'E':
        print('Goodbye!')
        break


if __name__ == "__main__":
    main()
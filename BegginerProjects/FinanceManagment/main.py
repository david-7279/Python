from finance import Finance
from user import User

from time import sleep
import os

# Clear the terminal
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  sleep(0.5)


# User Menu Choice
def user_main_menu_choise():
  choices = [1, 2, 3, 4, 0]
  while True:
    try:
      choice = int(input('Choose an option: '))
      if choice in choices: 
        return choice
      else:
        print(f'Invalid choice: {choice}. Please, choose an valid option.')
    except ValueError:
      print(f'Invalid number: {choice}. Please, write an integer number.')
    except Exception as e:
      print(f'An error ocurred: {e}. Please, try again.')


# Main program
def main():
  clear_screen()
  print('Welcome to Finance Management, here you can manage your finances.\n')

  # Load an create an user
  user = User()
  user.create_user()

  # Load user balance
  finance = Finance(user.balance)
  sleep(0.5)
  
  clear_screen()

  while True:
    print('1. for payments')
    print('2. for analyse')
    print('3. for profile')
    print('0. for leave the program')

    option = user_main_menu_choise()
    clear_screen()

    if option == 1:
      finance.add_payment(user)
    elif option == 2:
      finance.analyze_finances(user)
    elif option == 3:
      finance.view_profile(user)
    elif option == 0:
      print('Goodbye!')
      break


# Call main program
if __name__ == '__main__':
  main()
from inventory import Inventory
from time import sleep
import os


# Clear the terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(1)


# User choice
def user_choice():
  choices = [1, 2, 3, 4, 5, 6, 0]
  while True:
    try:
      choice = int(input('Choose an option: '))
      if choice in choices:
        return choice
      else:
        print(f'Invalid choice: {choice}. Please, try again.')
    except ValueError:
      print(f'Invalid number. Please, try again.')


# Main program
def main():
  inventory = Inventory()
  print('Welcome to Inventory Manager.\nHere you can manage all items of your inventory.\n')

  while True:
    print('1. for add item')
    print('2. for update item')
    print('3. for remove item')
    print('4. for view inventory')
    print('5. for view category item')
    print('6. for remove all inventory')
    print('0. for leave the program')

    choice = user_choice()

    if choice == 1:
      inventory.add_item()
    elif choice == 2:
      clear_screen()
      inventory.update_item()
    elif choice == 3:
      clear_screen()
      inventory.remove_item()
    elif choice == 4:
      clear_screen()
      inventory.view_inventory()
    elif choice == 5:
      clear_screen()
      inventory.view_category_item()
    elif choice == 6:
      clear_screen()
      inventory.clear_inventory()
    elif choice == 0:
      clear_screen()
      print('Goodbye.')
      break


# Call main program
if __name__ == '__main__':
    main()

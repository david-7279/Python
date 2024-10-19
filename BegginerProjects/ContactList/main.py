from contact import Contact
from time import sleep
import os

# Clear the terminal
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  sleep(0.5)

# User option
def user_choice():
  choices = [1, 2, 3, 4, 0]
  while True:
    try:
      option = int(input('Choose an option: '))
      if option in choices:
        return option
      else:
        print(f'Invalid option: {option}. Please, try again.')
    except ValueError:
      print(f'Invalid number: {option}. Please, try again.')
    except Exception as e:
      print(f'An error ocurred: {e}. Please, try again.')


# Main program
def main():
  contact = Contact()
  print('Welcome to the contact list.\nHere can manage your contact list.\n')

  while True:
    print('1. for add contact')
    print('2. for view contact list')
    print('3. for edit contact')
    print('4. for remove contact')
    print('0. for leave the program')

    option = user_choice()

    if option == 1:
      contact.add_contact()
    elif option == 2:
      clear_screen()
      contact.view_contact_list()
    elif option == 3:
      clear_screen()
      contact.edit_contact()
    elif option == 4:
      clear_screen()
      contact.remove_contact()
    elif option == 0:
      clear_screen()
      print('Goodbye!')
      break


# Call the main program
if __name__ == '__main__':
  main()
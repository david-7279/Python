from pet import Pet
from time import sleep
import os 


# Clear the terminal
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  sleep(0.5)


# User option
def user_main_menu():
  choices = [1, 2, 3, 4, 5, 6, 0]
  while True:
    try:
      option = int(input('Choose an option: '))
      if option in choices:
        return option
      else:
        print(f'Invalid choice: {choices}. Please, choose an valid option.\n')
    except ValueError:
      print(f'Invalid number: {choices}. Please, choose an integer number.\n')
    except Exception as e:
      print(f'An error ocurred: {e}. Please, try again.')
    

# Main program
def main():
  clear_screen()
  pet_manager = Pet()
  
  print('Welcome to Pet Book. Here can manage your pets')
  while True:
    print('\n1. for add pet')
    print('2. for edit pet')
    print('3. for remove pet')
    print('4. for view pet')
    print('5. for view by category')
    print('6. for mark an vet consult')
    print('0. leave program.')

    option = user_main_menu()

    if option == 1:
      pet_manager.add_pet()
    elif option == 2:
      clear_screen()
      pet_manager.edit_pet()
    elif option == 3:
      clear_screen()
      pet_manager.remove_pet()
    elif option == 4:
      clear_screen()
      pet_manager.view_pet()
    elif option == 5:
      clear_screen()
      pet_manager.view_category_pet()
    elif option == 6:
      clear_screen()
      pet_manager.view_consult()
    elif option == 0:
      clear_screen()
      print('Goodbye!')
      break


# Call main program
if __name__ == '__main__':
  main()
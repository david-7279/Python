from models.clear_screen import clear
from time import sleep

# MAIN MENU
def main_menu_option():
    choices = [1, 2, 3, 0]
    while True:
        try:
            option = int(input("Select an option: "))
            clear()
            if option in choices:
                return option
            else:
                print(f"Invalid option '{option}'! Please enter a number between 0 and 3.")
                sleep(1)
                input("Press enter to continue...")
                clear()
                main_menu()
        except ValueError:
            clear()
            print(f"Invalid input! Please enter a number between 0 and 3.")
            sleep(1)
            input("Press enter to continue...")
            clear()
            main_menu()
        except Exception as e:
            print(f"An unexpected error occurred '{e}'.")
            sleep(1)
            input("Press enter to continue...")
            clear()


def main_menu():
  print("1. Weak Upgrade")
  print("2. Moderate Upgrade")
  print("3. Strong Upgrade")
  print("0. Exit the Program")

  option = main_menu_option()
  
  match option:
    case 1:
      pass
    case 2:
      pass
    case 3:
      pass
    case 0:
      while True:
        confirmation = input("Are you sure want to leave (Yes/No)? ").lower()
        if confirmation in ['y', 'yes']:
          clear()
          print("Exiting the program...")
          sleep(1)
          clear()
          exit()
        elif confirmation in ['n', 'no']:
          clear()
          print("I'm glad you are not leaving!")
          sleep(1)
          input("Press enter to continue...")
          clear()
          break
        else:
          print(f"\nInvalid confirmation '{confirmation}'! Please, choose an valid confirmation (Yes or No).")
          sleep(1)
          input("Press enter to continue...")
          clear()
          continue
    case _:
      pass

# UPGRADE
def upgrade_menu():
  print("0. Go back")
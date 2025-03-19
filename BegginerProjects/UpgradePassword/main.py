from models.menu import main_menu
from models.clear_screen import clear
from time import sleep

def main_menu_option():
    choices = [1, 2, 3, 0]
    while True:
        try:
            main_menu()
            option = int(input("Select an option: "))
            if option in choices:
                return option
            else:
                print(f"\nInvalid option: {option}! Please enter a number between 0 and 3.")
                sleep(1)
                input("Press enter to continue...")
                clear()
        except ValueError:
            print(f"\nInvalid input! Please enter a number between 0 and 3.")
            sleep(1)
            input("Press enter to continue...")
            clear()
        except Exception as e:
            print(f"An unexpected error occurred: {e}.")
            sleep(1)
            input("Press enter to continue...")
            clear()


if __name__ == "__main__":
    while True:  
      clear()
      option = main_menu_option()
      clear()

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
                    print(f"\nInvalid confirmation: {confirmation}! Please, choose an valid confirmation (Yes or No).")
                    sleep(1)
                    input("Press enter to continue...")
                    clear()
                    continue
          case _:
              pass
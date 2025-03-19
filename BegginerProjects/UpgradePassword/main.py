from models.menu import main_menu
from models.clear_screen import clear
from time import sleep

def main_menu_option():
    choices = [1, 2, 3, 0]
    while True:
        try:
            option = int(input("Select an option: "))
            if option in choices:
                return option
            else:
                print(f"Invalid option: {option}! Please, select an valir option!")
                input("Press enter to continue...")
                continue
        except ValueError:
            print(f"Invalid input: {option}! Please, try again!")
        except Exception as e:
            print(f"An error ocurred: {e}. Plese, try again!")


if __name__ == "__main__":
    while True:  
      clear()
      main_menu()
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
                    print("Exiting the program...")
                    sleep(1)
                    clear()
                    exit()
                elif confirmation in ['n', 'no']:
                    print("I'm glad you are not leaving!")
                    sleep(1)
                    input("Press enter to continue...")
                    clear()
                    break
                else:
                    print(f"Invalid confirmation: {confirmation}! Please, choose an valid confirmation!")
                    sleep(1)
                    input("Press enter to continue...")
                    clear()
                    continue
          case _:
              pass
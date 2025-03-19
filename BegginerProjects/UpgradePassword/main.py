from models.menu import main_menu
from models.clear_screen import clear

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
              pass
          case _:
              pass
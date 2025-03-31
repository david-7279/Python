from src.ui import clear
from src.core import Validator
from src.ui import Menu

if __name__ == "__main__":
  validator = Validator()
  menu = Menu()
  while True:  
    clear()
    validator.user_password()
    clear()
    menu.main_menu(validator)
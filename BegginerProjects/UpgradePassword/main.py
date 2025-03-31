from src.core import Validator
from src.ui import Menu, Utils

if __name__ == "__main__":
  validator = Validator()
  menu = Menu()
  utils = Utils()
  while True:  
    utils.clear()
    validator.user_password()
    utils.clear()
    menu.main_menu(validator)
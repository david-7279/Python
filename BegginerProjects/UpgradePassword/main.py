from src.ui import clear, main_menu
from src.core import Validator

if __name__ == "__main__":
  validator = Validator()
  while True:  
    clear()
    validator.user_password()
    clear()
    main_menu(validator)
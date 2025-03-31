from src.ui import clear, main_menu
from src.core import Validator

if __name__ == "__main__":
  while True:  
    clear()

    default_password = Validator()
    default_password.user_password()
        
    clear()
    main_menu()
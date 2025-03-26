from models.menu import main_menu
from models.validate import user_password
from models.clear_screen import clear

if __name__ == "__main__":
    while True:  
      clear()
      user_password()
      clear()
      main_menu()
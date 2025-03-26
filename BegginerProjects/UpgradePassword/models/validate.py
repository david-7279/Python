from models.clear_screen import clear
from time import sleep

# USER PASSOWRD
def user_password():
  while True:
    try:
      password = input('Enter your password: ')
      if password == '' or len(password) == 0:
        print(f"Empty password! Please enter an valid password")
        sleep(1)
        input("Press enter to continue...")
        clear()
        continue
      else:
        print("Your password was store sucessufully!")
        sleep(1)
        clear()
        print("We are characterizing your password...")
        sleep(1)
        return password
    except Exception as e:
      print(f"An unexpected error occurred '{e}'.")
      sleep(1)
      input("Press enter to continue...")
      clear()
  
  return password


# CHARACTERIZING
def characterizing(password):
  pass
  

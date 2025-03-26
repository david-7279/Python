from models.clear_screen import clear, clear_input
from time import sleep

# USER PASSOWRD
def user_password():
  while True:
    try:
      password = input('Enter your password: ')
      if password == '' or len(password) == 0:
        print(f"Empty password! Please enter an valid password")
        clear_input()
        continue
      else:
        print("Your password was store sucessufully!")
        sleep(1)
        clear()
        characterizing(password)
        return
    except Exception as e:
      print(f"An unexpected error occurred '{e}'.")
      clear_input()


# CHARACTERIZING
def characterizing(password):
  print("We are characterizing your password...")
  sleep(1)

  

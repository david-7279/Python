from ..ui.utils import clear, clear_input
from time import sleep

class Validator:
  def __init__(self):
    pass

  # USER PASSOWRD
  def user_password(self):
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
          self.characterizing(password)
          return
      except Exception as e:
        print(f"An unexpected error occurred '{e}'.")
        clear_input()


  # CHARACTERIZING
  def characterizing(self, password):
    print("We are characterizing your password...")
    sleep(1)
    clear()

    letters = []
    numbers = []
    special = []

    for p in password:
      if p.isalpha():
        letters.append(p)
      elif p.isdigit():
        numbers.append(p)
      else:
        special.append(p)

    length = len(password)
    lettersLength = len(letters)
    numbersLength = len(numbers)
    specialLength = len(special)

    print(f"Passowrd length: '{length}'")
    print(f"Letters: '{lettersLength}', Numbers: '{numbersLength}', Special Characters: '{specialLength}'")
  
    if length > 1 and numbersLength <= 4 and specialLength <= 2:
      print("Your password is WEAK\n")
    elif length > 12 and (numbersLength > 4 or specialLength > 2):
        print("Your password is MODERATE\n")
    elif length > 24 or (numbersLength > 12 and specialLength > 12):
        print("Your password is STRONG\n")
    else:
      print("Your password exceeds the defined criteria\n")

    clear_input()
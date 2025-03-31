from ..ui.utils import Utils
from ..core.password_upgrader import Upgrader
from time import sleep

class Validator:
  def __init__(self):
    self.password = None
    self.length = 0
    self.letters_count = 0
    self.numbers_count = 0
    self.special_count = 0
    self.strength = None

  # USER PASSOWRD
  def user_password(self):
    utils = Utils()
    while True:
      try:
        password = input('Enter your password: ')
        if password == '' or len(password) == 0:
          print(f"Empty password! Please enter an valid password")
          utils.clear_input()
          continue
        else:
          print("Your password was store sucessufully!")
          sleep(1)
          utils.clear()
          self.password = password
          self.characterizing(password)
          return
      except Exception as e:
        print(f"An unexpected error occurred '{e}'.")
        utils.clear_input()


  # CHARACTERIZING
  def characterizing(self, password):
    utils = Utils()
    print("We are characterizing your password...")
    sleep(1)
    utils.clear()

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

    self.length = len(password)
    self.letters_count = len(letters)
    self.numbers_count = len(numbers)
    self.special_count = len(special)

    print(f"Passowrd length: '{self.length}'")
    print(f"Letters: '{self.letters_count}', Numbers: '{self.numbers_count}', Special Characters: '{self.special_count}'")
  
    if self.length > 1 and self.numbers_count <= 4 and self.special_count <= 2:
      self.strength = "WEAK"
      print("Your password is WEAK\n")
    elif self.length > 12 and (self.numbers_count > 4 or self.special_count > 2):
        self.strength = "MODERATE"
        print("Your password is MODERATE\n")
    elif self.length > 24 or (self.numbers_count > 12 and self.special_count > 12):
        self.strength = "STRONG"
        print("Your password is STRONG\n")
    else:
      self.strength = "STRONG"
      print("Your password exceeds the defined criteria\n")

    utils.clear_input()
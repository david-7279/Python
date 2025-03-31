from ..ui import clear_input
import random

class Weak:
  def __init__(self, validator):
    self.validator = validator

  def weak_info(self):
    print("Weak Upgrade Information:")
    print("1. Shuffle your password")
    print("2. Verify the length of password (Weak: 12)")
    print("3. Add random letters, random numbers, and random special characters, based on your password length")
    print("4. Shuffle your password again")
    self.weak_confirmation()


  def weak_confirmation(self):
    while True:
      try:
        confirmation = input("\nWant to upgrade your password? (Yes/No) ").lower()
        if confirmation in ['yes', 'y']:
          self.weak_upgrade()
        elif confirmation in ['no', 'n']:
          print("Your password remains the same!")
          clear_input()
          break
        else:
          print(f"\nInvalid confirmation '{confirmation}'! Please, choose an valid confirmation (Yes or No).")
          clear_input()
          self.weak_info()
          continue
      except Exception as e:
        print(f"An unexpected error occurred '{e}'.")
        clear_input()


  def weak_upgrade(self):
    password = self.validator.password
    length = self.validator.length

    # Conver password to a list
    password_list = list(password)

    # Shuffle password
    random.shuffle(password_list)
    
    # Verify the Length
    if password_list < 12:
      pass
      # Adiciona caracteres aleatórios (letras, números, especiais)


    # 3. Adiciona mais caracteres aleatórios (baseado no tamanho atual)


    # 4. Shuffle again

    # Convert the list back to string

    # Update the data for Validator
    
    # Avaluate the password again
    self.validator.characterizing()
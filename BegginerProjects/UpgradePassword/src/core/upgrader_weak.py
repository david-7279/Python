from ..ui import clear_input
import random

class Weak:
  def __init__(self, password):
    self.password = password

  def weak_info(self):
    print("Weak Upgrade Information:")
    print("Shuffle your password")
    print("Verify the length of password (Weak: 12)")
    print("Add random letters, random numbers and random special characters, based on your password length")
    print("3. Shuffle your password again")
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


  def weak_upgrade(self, password):
    # Shuffle password
    shuffle_password = random(password)

    # Add random letters, numbers and special characters based on length
    

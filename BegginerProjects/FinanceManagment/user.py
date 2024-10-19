from time import sleep
import os

# Clear the terminal
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  sleep(0.5)


class User:
  def __init__(self):
    self.name = ''
    self.balance = 0.0


  def create_user(self):
    while True:
      try:
        self.name = input('Enter your name: ')
        if not self.name or self.name.isdigit():
          print('Please, write an valid name.')
          continue

        self.balance = float(input('Enter your current balance: $'))
        if not self.balance:
          print('Please, write an valid balance.\n')
          continue
        elif self.balance < 0:
          print('Balance cannot be negative. Please, write an valid balance.\n')
          continue
        
        print(f'User created sucessfully!\n')
        break
      except ValueError:
        print('Invalid number. Please, try again.\n')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.\n') 
  
  def edit_username(self):
    while True:
      try:
        new_name = input('Enter your new name: ')
        if not new_name or new_name.isdigit() or new_name == self.name:
          print('Please, write an valid name.')
          continue
        else:
          self.name = new_name
          print(f'New name updated to {new_name}\n')
          return
      except ValueError:
        print('Invalid number. Please, try again.\n')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.\n') 
  

  def edit_balance(self):
    while True:
      try:
        new_balance = float(input('Enter your current balance: $'))
        if not self.balance:
          print('Please, write an valid balance.\n')
          continue
        elif self.balance < 0:
          print('Balance cannot be negative. Please, write an valid balance.\n')
          continue
        else:
          self.balance = new_balance
          print(f'Balance updated to ${self.balance:.2f}\n')
          return
      except ValueError:
        print('Invalid number. Please, try again.\n')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.\n') 
  
  
  def remove_user(self):
    while True:
      try:
        confirmation = input('Are your sure you want to remove the user (Yes/No)? ').lower()
        if confirmation in ['yes', 'y']:
          print('User removed suceffully!\n')
          self.name = ''
          self.balance = 0.0
          return
        elif confirmation in ['no', 'n']:
          print('No changes made. The user remains the same\n')
          return
        else:
          print(f'Invalid confirmation. Please, try again.')
          continue
      except ValueError:
        print('Invalid number. Please, try again.\n')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.\n') 
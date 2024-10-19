from user import User
from time import sleep
import os

# Clear the terminal
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  sleep(0.5)


# Class for Management Finacances
class Finance:
  def __init__(self, balance):
    self.balance = balance
    self.payments = []
    self.categories = ['Education', 'Housing', 'Entertainment', 'Clothing', 'Food']
    pass

  def view_categories(self):
    print('Payment categories: ')
    for index, category in enumerate(self.categories, start=1):
      print(f'[{index}] {category}')


  def add_payment(self, user):  
    if user.balance <= 0:
      print(f'You dont have enough money to do payments. Your current balance is {user.balance}\n')
      return
     
    self.view_categories()
    print('[0] To go back\n')

    try:
      payment_index = int(input('Choose and category: '))
      if 1 <= payment_index <= len(self.categories):
        payment_category = self.categories[payment_index - 1]

        payment_value = float(input(f'Write the value amount for {payment_category} (current balance ${user.balance}): $'))
        if payment_value > user.balance:
          print(f'Insufecient balance for this payment. Your current balance is ${self.balance}\n')
          return
        else:
          user.balance -= payment_value
          self.payments.append({'category': payment_category, 'value': payment_value})
          print(f'Payment of ${payment_value} for {payment_category} completed sucessfully! Your current balance is ${user.balance}\n')
          return
      elif payment_index == 0:
        print(f'No changes made. All payments remains the same, and your current balance is ${user.balance}.\n')
        return
      else:
        print('Invalid category!\n')
      
    except ValueError:
      print('Invalid input. Please, try again.')
    except Exception as e:
      print(f'An error ocurred: {e}. Please, try again.')
    
    
  def analyze_finances(self, user):
    if not self.payments:
      print('No payment to analyze.\n')
      return 

    category_totals = {category: 0 for category in self.categories}

    for payment in self.payments:
      category = payment['category']
      value = payment['value']
      category_totals[category] += value
    
    for category in self.categories:
      print(f'{category}: ${category_totals[category]:.2f}')

    total_spend = sum(value['value'] for value in self.payments)
    print(f'\nTotal spent: ${total_spend:.2f}')
    print(f'Your Current balance is: ${user.balance} \n')


  def view_profile(self, user):
    print('Your information:')
    print(f'Name: {user.name}')
    print(f'Balance: ${user.balance}\n')

    print('1. for edit name')
    print('2. for edit balance')
    print('0. to go back\n')

    choices = [1, 2, 0]
    while True:
      try:
        option = int(input('Choose an option: '))
        if option in choices:
          if option == 1:
            clear_screen()
            user.edit_username()
            return
          elif option == 2:
            clear_screen()
            user.edit_balance()
            return
          elif option == 0:
            print('No changes made. The user remains the same.\n')
            sleep(0.7)
            clear_screen()
            return
        else:
          print(f'Option invalid: {option}. Plese, write an valid option.')
      except ValueError:
        print(f'Invalid number: {option}. Please, write an integer number.')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.')
    
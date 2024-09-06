class Account:
  def __init__(self, name, nif, balance = 0):
    self.name = name
    self.nif = nif
    self.balance = balance
    self.transactions = []

  
  def deposit(self, value):
    if value > 0:
      self.balance += value
      self.transactions.append(f'{self.nif} | {self.name} - Deposit {value:.2f}$')
    else:
      print(f'Invalid {value}, please deposit an amount greater than zero.')


  def withdraw(self, value):
    if value <= self.balance:
      self.balance -= value
      self.transactions.append(f'{self.nif} | {self.name} - Withdraw {value:.2f}$')
    else:
      print(f'Insufficient balance.\n')

  
  def print_transactions(self):
    if not self.transactions:
      print('Transactions not found.')
    for transactions in self.transactions:
      print(f'{transactions}')
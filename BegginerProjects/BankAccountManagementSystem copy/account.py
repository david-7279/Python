class Account:
  def __init__(self, name, nif, balance = 0):
    self.name = name
    self.nif = nif
    self.balance = balance
    self.transactions = []


  def deposit(self, value):
    self.balance += value
    self.transactions.append(f'{self.name}, {self.nif} - Deposit {value:.2f}$')


  def withdraw(self, value):
    if value <= self.balance:
      self.balance -= value
      self.transactions.append(f'{self.name}, {self.nif} - Withdraw {value:.2f}$')
    else:
      print('Insufficient balance')


  def print_balance(self):
    print(f'{self.name} - your current balance: {self.balance:.2f}$')


  def print_transactions(self):
    if not self.transactions:
      print('No transactions found.')
    for transactions in self.transactions:
      print(transactions)
from account import Account

class Bank:
  def __init__(self):
    self.accounts = []


  def create_account(self, name, nif, initial_balance = 0):
    account = Account(name, nif, initial_balance)
    self.accounts.append(account)
    print(f'Account created sucessufully: {name}, {nif} - {initial_balance:.2f}$')


  def find_account(self, nif):
    for account in self.accounts:
      if account.nif == nif:
        return account
    return None


  def delte_account(self, nif):
    for account in self.accounts:
      if account.nif == nif:
        self.accounts.remove(account)
        print(f'Account with NIF {nif} deleted successfully.')
        return True
    print(f'Account with NIF {nif} not found')
    return None

  
  def print_accounts(self):
    if not self.accounts:
      print('No accounts available')
    for account in self.accounts:
      print(f'{account.name}, {account.nif} - {account.balance:.2f}$')


  def transfer(self, from_nif, to_nif, amount):
      from_account = self.find_account(from_nif)
      to_account = self.find_account(to_nif)
      if from_account and to_account:
        if from_account.balance >= amount:
          from_account.withdraw(amount)
          to_account.deposit(amount)
          print(f'Transfer of {amount:.2f}$ from {from_nif} to {to_nif} completed sucessfully.')
        else:
          print('Insuficient balance for transfer.')
      else:
        print('One or both accounts not found.')

    
  def print_account_transactions(self, nif):
      account = self.find_account(nif)
      if account:
        account.print_transactions()
      else:
        print(f'Acoount with NIF {nif} not found.')

  
  def apply_service_fee(self, fee_amount):
    for account in self.accounts:
      if account.balance >= fee_amount:
        account.withdraw(fee_amount)
        print(f'Service fee of {fee_amount:.2f}$ applied to account {account.nif}.')
      else:
        print(f'Insufficient balance to aply service fee for account {account.nif}.')

  
  def close_account(self, nif, transfer_to_nif):
    account_to_close = self.find_account(nif)
    if account_to_close:
      if transfer_to_nif:
        transfer_account = self.find_account(transfer_to_nif)
        if transfer_account:
          self.transfer(nif, transfer_to_nif, account_to_close.balance)
        else:
          print(f'Transfer account with NIF {transfer_to_nif} not found.')
          return
      self.delte_account(nif)
      print(f'Account with NIF {nif} closed sucessfully.')
    else:
      print(f'Account with NIF {nif} not found.')

  
  def generate_report(self):
    total_balance = sum(account.balance for account in self.accounts)
    num_accounts = len(self.accounts)
    print(f'Total balance acrross all accounts: {total_balance:.2f}$')
    print(f'Number of accounts: {num_accounts}')
    for account in self.accounts:
      print(f'{account.name}, {account.nif} : {account.balance}$')

  
  def find_overdrawn_accounts(self):
    overdrawn_accounts = [account for account in self.accounts if account.balance < 0]
    if overdrawn_accounts:
      print('Overdrawn accounts: ')
      for account in overdrawn_accounts:
        print(f'{account.name}, {account.nif} : {account.balance:.2f}$')
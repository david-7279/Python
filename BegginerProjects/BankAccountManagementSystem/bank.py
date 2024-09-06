from account import Account

class Bank:
  def __init__(self):
    self.accounts = []


  def create_account(self, name, nif, initial_balance = 0):
    account = Account(name, nif, initial_balance)
    self.accounts.append(account)
    print(f'Account created sucessfully - {nif} | {name} : {initial_balance:.2f}$')


  def find_account(self, nif):
    if not self.accounts:
      print(f'No accounts available.')
    for account in self.accounts:
      if account.nif == nif:
        return account
    else:
      print(f'Account with the NIF {nif} not found.')

  
  def delete_account(self, nif):
    if not self.accounts:
      print(f'No accounts available.')
    for account in self.accounts:
      if account.nif == nif:
        self.accounts.remove(account)
        print(f'Account with the NIF {nif} ({account.name}) removed sucessfully.\n')
        return True
    print(f'Account with the NIF {nif} not found.\n')
 
  
  def print_accounts(self):
    if not self.accounts:
      print(f'No accounts available.')
    for account in self.accounts:
      print(f'{account.nif} | {account.name} : {account.balance:.2f}$')

  
  def transfer(self, from_nif, to_nif, amount):
    if not self.accounts:
      print(f'No accounts available.')
    from_account = self.find_account(from_nif)
    to_account = self.find_account(to_nif)
    if from_account and to_account:
      if from_account.balance >= amount:
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f'Transfer of {amount:.2f}$ from {from_nif} ({from_account.name}) to {to_nif} ({to_account.name}) completed sucessfully.')
      else:
        print('Insuficient balance for transfer\n')
    else:
      print('One or both accounts not found.\n')


  def print_transactions(self, nif):
    if not self.accounts:
      print(f'No accounts available.')
    account = self.find_account(nif)
    if account:
      account.print_transactions()
    else:
      print(f'Account with the NIF {nif} not found.\n')
    

  def apply_service_fee(self, fee_amount):
    if not self.accounts:
      print(f'No accounts available.')
    for account in self.accounts:
      if account.balance >= fee_amount:
        account.balance -= fee_amount
        print(f'Service fee of {fee_amount:.2f}$ apllied into account {account.nif}')
      else:
        print(f'Insufficient balance to aply service fee for account {account.nif}.\n')


  def close_account(self, nif, transfer_to_nif):
    if not self.accounts:
      print(f'No accounts available.')
    account_to_close = self.find_account(nif)
    if account_to_close:
      if transfer_to_nif:
        transfer_account = self.find_account(transfer_to_nif)
        if transfer_account:
          self.transfer(nif, transfer_to_nif, account_to_close.balance)
          print(f'Account with NIF {nif} ({account_to_close.name}) closed sucessfully.')
        else:
          print(f'Transfer account with NIF {transfer_to_nif} not found.\n')
          return
      self.delete_account(nif)
    else:
      print(f'Account with NIF {nif} not found.\n')

  
  def generate_report(self):
    if not self.accounts:
      print(f'No accounts available.')
    total_balance = sum(account.balance for account in self.accounts)
    num_accounts = len(self.accounts)
    print(f'Total balance: {total_balance:.2f}$')
    print(f'Number of accounts: {num_accounts}')
    for account in self.accounts:
      print(f'\t{account.nif} | {account.name} : {account.balance:.2f}$')


  def find_overdrawn_accounts(self):
    if not self.accounts:
      print(f'No accounts available.')
    overdrawn_accounts = [account for account in self.accounts if account.balance < 0]
    if overdrawn_accounts:
      print(f'Overdrawn account: ')
      for account in overdrawn_accounts:
        print(f'{account.name}, {account.nif} : {account.balance:.2f}$')
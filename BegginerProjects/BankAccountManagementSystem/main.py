from account import Account
from bank import Bank

def main():
  bank = Bank()
  bank.create_account('David', 1, 300)
  bank.create_account('Soares', 2, 600)
  bank.create_account('Vieira', 3, 100)

  bank.find_overdrawn_accounts()

  print('\nFinding accounts:')
  bank.find_account(4)

  print('\nDeleting accounts:')
  bank.delete_account(3)

  print('Printing accounts:')
  bank.print_accounts()

  print('\nTransferring money into accounts:')
  bank.transfer(1, 2, 150)

  print('\nDeposit money:')
  a1 = bank.find_account(1)
  if a1:
    deposit_value = 500
    a1.deposit(deposit_value)
    print(f'Deposit of {deposit_value:.2f}$ into account {a1.nif} ({a1.name}) completed sucessfully.')

  print('\nWithdraw money:')
  a2 = bank.find_account(2)
  if a2:
    withdraw_value = 100
    a2.withdraw(withdraw_value)
    print(f'Withdraw of {withdraw_value:.2f}$ into account {a2.nif} ({a2.name}) completed sucessfully.')

  print('\nShow transactions:')
  bank.print_transactions(1)
  bank.print_transactions(2)

  print('\nApply service fee:')
  bank.apply_service_fee(50)

  print('\nClosing account:')
  bank.close_account(1, 2)

  print('Generating report:')
  bank.generate_report()

if __name__ == '__main__':
  main()
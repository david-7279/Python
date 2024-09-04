from account import Account
from bank import Bank

def main():
    bank = Bank()
    bank.create_account('David', 111222333, 400)
    bank.create_account('Soares', 999888777, 400)
    bank.create_account('Vieira', 444555666, 0)
    bank.create_account('Vieira', 123456789, -100)
    print('')

    bank.find_overdrawn_accounts()
    print('')

    account1 = bank.find_account(111222333)
    if account1:
      account1.print_balance()
      account1.deposit(200)
      print('Successfully deposited')
      account1.print_balance()
      account1.withdraw(400)
      print('Successfully withdrawn')
      account1.print_balance()
      print('')
    else:
      print(f'{account1} not found')

    account2 = bank.delte_account(999888777)
    print('\nReport')
    bank.print_accounts()

    print('\nTransfer money into different account')
    account1 = bank.transfer(111222333, 123456789, 100)
    print('\nReport')
    bank.generate_report()

    print(f'\nAccount transactions')
    account1 = bank.print_account_transactions(111222333)

    print(f'\nService fee aplied')
    bank.apply_service_fee(50)
    print('')
    bank.generate_report()

    print(f'\nClose account')
    bank.close_account(111222333, 444555666)
    print('')
    bank.generate_report()

if __name__ == '__main__':
    main()
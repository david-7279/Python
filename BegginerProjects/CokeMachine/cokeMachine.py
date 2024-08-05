def get_valid_coins():
    choices = [25, 10, 5]
    while True:
      try:
        insert_coin = int(input('Insert Coin: '))
        if insert_coin in choices:
          return insert_coin
        else:
          return None
      except ValueError:
        print(f'Amount Due: 50')


def subtract_due(total_due):
    while total_due > 0:
      coin = get_valid_coins()
      total_due -= coin

      if total_due > 0:
        print(f'Amount Due: {total_due}')
      else:
        print(f'Changed Owed: {abs(total_due)}')
        break


def main():
    total_due = 50
    print(f"Amount Due: {total_due}")
    subtract_due(total_due)


if __name__ == "__main__":
    main()
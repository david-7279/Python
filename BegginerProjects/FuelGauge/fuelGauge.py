def get_valid_fuel():
    while True:
      try:
        fraction = input('Fraction: ')
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if y == 0:
          raise ZeroDivisionError
        if x > y:
          print('Invalid fraction! The numerator cannot be greater than the denominator.')
          continue
        return x, y
      except ValueError:
        print('Invalid value! Please, try again.')
      except ZeroDivisionError:
        print('Invalid fraction! Division by zero ocurred.')


def fuel_indicator(x, y):
    percentage = (x / y) * 100

    if percentage <= 1:
      return 'E'
    elif percentage >= 99:
      return 'F'
    else:
      return f'{round(percentage)}%'


def main():
    x, y = get_valid_fuel()
    indicator = fuel_indicator(x, y)
    print(f'Fuel Indicator: {indicator}')


if __name__ == "__main__":
    main()
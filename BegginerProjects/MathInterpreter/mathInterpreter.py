def getValidExpression():
    while True:
      try:
        x, y, z = input('Expression: ').split()
        x = int(x)
        z = int(z)
        if y in ['+', '-', '*', '/']:
          return x, y, z
        else:
          print('Invalid operator! Please, use one of +, -, *, /.')
      except ValueError:
        print('Invalid expression! Ensure to enter two integers separated by an operator (+, -, *, /).')


def calculateExpression(x, y, z):
    if y == '+':
      return x + z
    elif y == '-':
      return x - z
    elif y == '*':
      return x * z
    elif y == '/':
      return x / z


def main():
    x, y, z = getValidExpression()
    result = calculateExpression(x, y, z)
    print(f'{result:.1f}')


if __name__ == "__main__":
    main()

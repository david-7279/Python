def userInput():
    greeting = input('Greeting: ').strip().lower()
    if greeting != '':
      return greeting
    else:
      print(f'Invalid greeting! Please, try again.')
      return None


def verifyGreeting(greeting):
    if greeting == 'hello':
      return '$0'
    elif greeting.startswith('h') and  greeting != 'hello':
      return '$20'
    else:
      return '$100'


def main():
    greeting = None

    while greeting is None:
      greeting = userInput()

    verify = verifyGreeting(greeting)
    print(f'{verify}')
    

if __name__ == "__main__":
    main()
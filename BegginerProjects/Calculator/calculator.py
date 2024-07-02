import random, os
from time import sleep

def clearScreen():
    os.system('cls')
    sleep(1)
    

def userInput():
    choices = ['+', '-', '*', '/', '%', 'r']
    try:
      option = input("Choose an option: ").lower()
      if option in choices:
        print()
        return option
      else:
        print(f'Invalid option [{option}]! Please, try again.')
    except ValueError:
      print(f'Invalid number [{option}]! Please, try again.')


def addition():
    try:
      print('Addition')
      num1 = int(input('Enter the first number: '))
      num2 = int(input('Enter the second number: '))
      if isinstance(num1, int) and isinstance(num2, int):
        print(f'Addition: {num1} + {num2} = {num1 + num2}')
      else:
        print(f'Numbers [{num1}, {num2}] not an integer!\nPlease, try again.]')
        return False
    except:
      print(f'Invalid numbers [{num1}, {num2}]!\nPlease try again.')


def subtraction():
    try:
      print('Subtraction')
      num1 = int(input('Enter the first number: '))
      num2 = int(input('Enter the second number: '))
      if isinstance(num1, int) and isinstance(num2, int):
        print(f'Subtraction: {num1} - {num2} = {num1 - num2}')
      else:
        print(f'Numbers [{num1}, {num2}] not an integer!\nPlease, try again.]')
        return False
    except:
      print(f'Invalid numbers [{num1}, {num2}]!\nPlease try again.')


def multiplication():
  try:
    print('Multiplication')
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    if isinstance(num1, int) and isinstance(num2, int):
      print(f'Multiplication: {num1} * {num2} = {num1 * num2}')
    else:
      print(f'Numbers [{num1}, {num2}] not an integer!\nPlease, try again.]')
      return False
  except:
    print(f'Invalid numbers [{num1}, {num2}]!\nPlease try again.')


def division():
    try:
      print('Division')
      num1 = int(input('Enter the first number: '))
      num2 = int(input('Enter the second number: '))
      if isinstance(num1, int) and isinstance(num2, int):
        print(f'Division: {num1} / {num2} = {num1 / num2}')
      else:
        print(f'Numbers [{num1}, {num2}] not an integer!\nPlease, try again')
    except:
      print(f'Invalid numbers [{num1}, {num2}]!\nPlease try again.')


def module():
    try:
      print('Module')
      num1 = int(input('Enter the first number: '))
      num2 = int(input('Enter the second number: '))
      if isinstance(num1, int) and isinstance(num2, int):
        print(f'Module: {num1} / {num2} = {num1 % num2}')
      else:
        print(f'Numbers [{num1}, {num2}] not an integer!\nPlease, try again')
    except:
      print(f'Invalid numbers [{num1}, {num2}]!\nPlease try again.')
    

def randomize():
    print('Randomize Expression')

    randomNumberLength = random.randint(1, 10)
    numberList = []
    operationList = []

    for _ in range(randomNumberLength):
      randomNumbers = random.randint(1, 100)
      numberList.append(randomNumbers)

    for _ in range(randomNumberLength - 1):
      randomOperations = random.choice(['+', '-', '*', '/', '%'])
      operationList.append(randomOperations)
      
    expression = ''
    for i in range(randomNumberLength - 1):
      expression += f"{numberList[i]} {operationList[i]} "
    expression += str(numberList[-1])

    print(f'Generated numbers: {numberList}')
    print(f'Generated operations: {operationList}')
    print(f'Constructed expression: {expression}')

    try:
      result = eval(expression) # Evaluates the str expression as a normal operation | ("2 + 3") = 23, but with eval method ("2 + 3") = 5
      print(f'Result: {result:.2f}')
    except ZeroDivisionError:
      print(f'Error: Division by zero occurred.')
    except Exception  as error:
      print(f'Error: {error}.')
    

def main():
    print('Welcome to Pythonic Calculator!')
    while True:
      print('\n+. for addition')
      print('-. for subtraction')
      print('*. for multiplication')
      print('/. for division')
      print('%. for module')
      print('R. for randomize expression')

      option = userInput()

      if option == '+':
        clearScreen()
        addition()
      elif option == '-':
        clearScreen()
        subtraction()
      elif option == '*':
        clearScreen()
        multiplication()
      elif option == '/':
        clearScreen()
        division()
      elif option == '%':
        clearScreen()
        module()
      elif option == 'r':
        clearScreen()
        randomize()
      else:
        print(f'Invalid option [{option}]! Please, try again.')
        clearScreen()
        

if __name__ == "__main__":
  main()
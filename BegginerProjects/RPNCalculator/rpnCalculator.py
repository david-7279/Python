import os
from time import sleep

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(1)


def userOption():
    choices = [1, 2, 3]
    while True:
      try:
        option = int(input('Choose an option: '))
        if option in choices:
          return option
        else:
          print(f'Invalid option {option}! Please, try again.')
      except ValueError:
        print(f'Invalid number! Please, try again.')


def calculator():
    stack = []
    operandsChoices = ['+', '-', '*', '/']

    expression = input('Create an expression: ')
    tokens = expression.split()

    for token in tokens:
      # Verify if the toke is an number
      try:
        num = float(token)
        stack.append(num)

      except ValueError:
        if token in operandsChoices:
          # Verify if have enough operands in the stack
          if len(stack) < 2:
            print('Error: Not enough operands \ns')
            return

          operand2 = stack.pop()
          operand1 = stack.pop()
          
          if token == '+':    
            result = operand1 + operand2
          elif token == '-':  
            result = operand1 - operand2
          elif token == '*':  
            result = operand1 * operand2
          elif token == '/': 
            if operand2 == 0:
              print('Error: Division by zero. \n')
            result = operand1 / operand2
          
          stack.append(result)
        else:
          print(f'Invalid token {token}')
          return

    # Verify the final result
    if len(stack) == 1:
      finalResult = stack.pop()
      print(f'Final result: {finalResult} \n') 
    else:
      print('Error: The stack did not end with a single result. \n')



def definition():
    print('What is RPN Calculator?')
    print('A calculator that uses inverse Polish notation, where operators follow their operands.')
    sleep(3)
    print('This approach eliminates the need for parentheses to define the order of operations.')
    sleep(2)
    print('An exmaple to understand better: \n')
    print('Input: 3 4 + 2 * 7 /')
    print('Token: ["3", "4", "+", "2", "*", "7", "/"]')
    print('Stack: []\n')
    sleep(5)
    print('Step by step')
    print('1. "3" -> Stack: [3]')
    print('2. "4" -> Stack: [3, 4]')
    print('4. "+" -> UnStack "4" and "3", Stack: [7]')
    print('5. "2" -> Stack: [7, 2]')
    print('6. "*" -> UnStack "2" and "7", Stack: [14]')
    print('7. "7" -> Stack: [14, 7]')
    print('6. "/" -> UnStack "7" and "14", Stack: [2]\n')
    sleep(8)
    print('Final result: 2 \n\n')


def main():
    print('Welcome to RPN Calculator!\n')

    while True:
      print('1. to calculate numbers')
      print('2. what is RPN Calculator?')
      print('3. for leave the program')

      option = userOption()
      clearScreen()

      if option == 1:
        calculator()
      elif option == 2:
        definition()
      else:
        print('Goodbye!')
        break
    

if __name__ == "__main__":
    main()
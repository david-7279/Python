import os
from time import sleep

# Name List Array
from listNames import listNames

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(1)


def userOption():
    choices = [1, 2, 3, 4, 5, 6]

    while True:
      try:  
        option = int(input('Choose an option: '))
        if option in choices:
          return option
        else:
          print(f'Invalid option {option}! Please, try again.')

      except ValueError:
        print(f'Invalid number {option}! Please, try again.')


def nameList():
    if listNames:
      for name in listNames:
        print(name)
    else:
      print('List is empty, nothing to see!')


def searchName(): 
    searchName = input('Search for a name: ').strip()

    if searchName in listNames:
      print(f'[{searchName}] is in the list!')
    else:
      addName = input(f'{searchName} is not in the list! Add it? ("Y/N") ').strip().lower()
      if addName == 'y':
        listNames.append(searchName)
        print(f'{searchName} added to the list!')
      else:
        print(f'{searchName} not added.')



def writeName():
    newName = input('Write an name: ').strip()

    if newName in listNames:
      print(f'[{newName}] is in the list!')
    else:
      addName = input(f'{newName} is not in the list! Add it? ("Y/N") ').strip().lower()
      if addName == 'y':
        listNames.append(newName)
        print(f'{newName} added to the list!')
      else:
        print(f'{newName} not added.')


def sortNames():
    if listNames:
      if sorted(listNames) == listNames:
        print('Sorted List!')
        nameList()
      else:
        listNames.sort()
        print('List sorted: ') 
        nameList()
    else:
      print('List is empty, nothing to sort!')
     

def deleteList():
    deleteConfirmation = input('Are you sure want to delete the list? ("Y/N") ').strip().lower()

    if deleteConfirmation == 'y':
      clearScreen()
      if listNames:
        listNames.clear()
        print('Deleting the list ...')
        sleep(1.7)
        print('List deleted!')
      else:
        print('List already empty!')
    else:
      print('List not deleted!')
    

def main():
    print('Welcome to Name Sorter!')

    while True:
      print('')
      print('1. to print the list of names')
      print('2. to search for a name')
      print('3. to write a new name')
      print('4. for sorting list names')
      print('5. to delete the list names')
      print('6. to leave the program')

      option = userOption()
      clearScreen()

      if option == 1:
        nameList()
      elif option == 2:
        searchName()
      elif option == 3:
        writeName()
      elif option == 4:
        sortNames()
      elif option == 5:
        deleteList()
      elif option == 6:
        print('Goodbye!')
        break
      else:
        print(f'Invalid option {option}! Please, try again.')
    

if __name__ == "__main__":
    main()
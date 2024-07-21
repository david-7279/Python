from time import sleep
import os

# Global array for items 
listItems = []

def clearScreen():
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def userOprion():
    choices = [1, 2, 3, 4, 5]
    while True:
      try:
        option = int(input('Choose an option: '))
        if option in choices:
          return option
        else:
          print(f'\nInvalid option {option}! Please, try again.\n')
      except ValueError as error:
        print(f'\nInvalid value {error}! Please, try again.\n')


def addItem():
    index = len(listItems) + 1
    name = input('Enter a name of the item: ').strip()
    category = input('Enter a category of the item\n\t"F" for food\n\t"M" for meat\n\t"V" for vegetables and fruit\n\t"S" for snacks\n\t"B" for beauty\n\t"H" for household essentials\n\t"D" for drinks\n\t"E" for eletronics\n\t"T" for tabbacco\n\t"O" for others\n\t: ').strip().upper()
    categoryChoices = {'F': 'Food', 'M': 'Meat', 'V': 'Vegetables and Fruits', 'S': 'Snacks', 'B': 'Beauty', 'H': 'Household Essentials', 'D': 'Drinks', 'E': 'Eletronics', 'T': 'Tabbacco', 'O': 'Other'}

    try:
      price = float(input('Enter a price of the item: '))
      quantity = int(input('Enter a quantity of the item: '))

      if (quantity >= 0) and (price >= 0) and name and category in categoryChoices:
        categoryFull = categoryChoices[category]
        listItems.append({'index': index, 'name': name, 'category': categoryFull, 'price': price, 'quantity': quantity})
        print(f'\nItem {name} added sucessfully.\n')
        return True
      else:
        print(f'\nInvalid item {name}! The item needs a name and a category, price and quantity has to be greather than zero.\n')
        return False
    except ValueError as error:
      print(f'\nInvalid value {error}! Please, try again.\n')
    

def removeItem():
    if not listItems:
      print('Items list is empty!\n')
      return

    viewItems()

    try:
      itemToRemove = int(input('Choosen an index to remove the item: '))

      if itemToRemove <= 0 or itemToRemove > len(listItems):
        print(f'Invalid item {itemToRemove}! Please, try again.\n')
        return

      removeItem = listItems.pop(itemToRemove - 1)

      for i, items in enumerate(listItems):
        items['index'] = i + 1

      clearScreen()
      print('Deleting item ... ')
      sleep(0.3)
      clearScreen()
      print(f'Item {removeItem['name']} deleting sucessfully.\n')
      
    except ValueError as error:
        print(f'\nInvalid value {error}! Please, try again.\n')
        

def viewItems():
    if not listItems:
      print('Items list is empty!\n')
      return

    totalCost = 0

    for item in listItems:
      itemCost = item['price'] * item['quantity']
      totalCost += itemCost
      print(f'[{item['index']}] {item['category']} - {item['name']} ({item['quantity']}): {itemCost:.2f}$')
    print(f'\nTotal cost of all items: {totalCost:.2f}$')


def clearList():
    if not listItems:
      print('Items list is empty!\n')
      return

    clear = input('Do you want to clear the shopping list? (Y/N): ').strip().lower()
    clearScreen()
    if clear == 'y':
      listItems.clear()
      print('Deleting the list ... \n')
      sleep(0.3)
      clearScreen()
      print('Items list is clear!\n')
    else:
      print('Clear list cancelled!\n')
      return    
      

def main():
    print('Welcome to Shopping List Manager!')

    while True:
      print('\n1. to add item to the list')
      print('2. to remove item in the list')
      print('3. to view all items in the list')
      print('4. to clear the list')
      print('5. to leave the program')

      option = userOprion()
      clearScreen()

      if option == 1:
        addItem()
      elif option == 2:
        removeItem()
      elif option == 3:
        viewItems()
      elif option == 4:
        clearList()
      elif option == 5:
        print('Goodbye!\n')
        break


if __name__ == "__main__":
    main()
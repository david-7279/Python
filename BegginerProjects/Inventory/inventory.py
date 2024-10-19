from time import sleep
import os

# Clear the terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(1)


class Inventory:
  def __init__(self):
        self.inventory = []

  def add_item(self):
    while True:
      try:
        sleep(1) 
        os.system('cls' if os.name == 'nt' else 'clear')
        clear_screen()
        name = input('Name of the item: ').title()
        if not name:
          
          print(f'Invalid name: {name}. Please, try again')
          continue

        category = input('Category of the item: ').title()
        if not category:
          print(f'Invalid category: {category}. Please, try again.')
          continue

        price = float(input('Price of the item: '))
        if price <= 0:
          print(f'Invalid price: {price:.2f}. Please, choose a valid price greater than zero.')
          continue

        quantity = int(input('Quantity number of the item: '))
        if quantity <= 0:
          print(f'Invalid quantity: {quantity}. Please, choose a valid quantity greater than zero.')
          continue

        # If all inputs are valid, add item to the inventory
        item = {
          "name": name,
          "category": category,
          "price": price,
          "quantity": quantity
        }

        self.inventory.append(item)
        print('Item added successfully into inventory.\n')
        self.save_inventory()
        sleep(0.7)
        clear_screen()
        return

      except ValueError as e:
        print(f'Invalid number: {e}. Please, try again.')
      except Exception as e:
        print(f'An error occurred: {e}. Please, try again.')   
      

  def update_item(self):
    if not self.inventory:
      print('No items available in the inventory.\n')
      return
    
    print('Inventory items: ')
    for index, item in enumerate(self.inventory, start=1):
      print(f'[{index}] {item["name"]} ({item["category"]}): ${item["price"]:.2f} - {item["quantity"]} in stock')
    print('[0] To leave\n')
    while True:
      try:
        item_index = int(input('Choose an item to update: '))
        if 1 <= item_index <= len(self.inventory):
          updated_item = self.inventory[item_index - 1]

          new_name = input(f'New name of the item (Leave blank to keep the current "{updated_item['name']}"): ').title() or updated_item['name']
          new_category = input(f'New category of the item (Leave blank to keep the current "{updated_item['category']}"): ').title() or updated_item['category']

          new_price_input = input(f'New price of the item (Leave blank to keep the current "{updated_item['price']}"): ')
          new_price = float(new_price_input) if new_price_input else updated_item['price']

          new_quantity_input = input(f'New quantity of the item (Leave blank to keep the current "{updated_item['quantity']}"): ')
          new_quantity = int(new_quantity_input) if new_quantity_input else updated_item['quantity']

          updated_item.update({
            "name": new_name,
            "category": new_category,
            "price": new_price,
            "quantity": new_quantity
          })

          print(f'Item updated successfully!\n{updated_item["name"]} ({updated_item["category"]}) - ${updated_item["price"]:.2f}, {updated_item["quantity"]} in stock\n')
          self.save_inventory()
          return
        
        elif item_index == 0:
          print('No changes made. All items remains the same.\n')
          return
        else:
          print(f'Item with index of [{index}] not found. Please, try again.') 
          return

      except ValueError:
        print(f'Invalid number: {item_index}. Please, try again.')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.')
    
  
  def remove_item(self):
    if not self.inventory:
      print('No items available in the inventory.\n')
      return

    print('Inventory items: ')
    for index, item in enumerate(self.inventory, start=1):
      print(f'[{index}] {item["name"]} ({item["category"]}): ${item["price"]:.2f} - {item["quantity"]} in stock')
    print(f'[0] To leave\n')

    while True:
      try:
        item_index = int(input('Choose an item to remove: '))
        if 1 <= item_index <= len(self.inventory):
          removed_item = self.inventory.pop(item_index - 1)
          print(f'Item removed sucessfully. [{item_index}] {removed_item['name']}\n')
          self.save_inventory()
          return
        elif item_index == 0:
          print(f'No changes made. All items remains the same.\n')
          return
        else:
          print(f'Item with index of [{index}] not found. Please, another time.\n')
        
      except ValueError:
        print(f'Invalid number: {item_index}. Please, try again.')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.')

    
  
  def view_inventory(self):
    if not self.inventory:
      print('No items available in the inventory.\n')
      return
    
    print('Inventory items: ')
    for index, item in enumerate(self.inventory, start=1):
      print(f'[{index}] {item["name"]} ({item["category"]}): ${item["price"]:.2f} - {item["quantity"]} in stock')
    print('')
    
  
  def view_category_item(self):
    if not self.inventory:
      print('No items available in the inventory.\n')
      return
    
    categories = sorted(set(item['category'] for item in self.inventory))
    if not categories:
      print('No categories available in the inventory.\n')
      return

    print('Inventory categories created: ')
    for index, category in enumerate(categories, start=1):
      print(f'[{index}] {category}')
    print('[0] To leave.\n')

    while True:
      try:
        select_category = int(input('Choose an index of category to view the items: '))
        if 1 <= select_category <= len(categories):
          select_category = categories[select_category - 1]
          print(f'\nItems in category [{select_category}]')

          item_found = False # Flag
          for item in self.inventory:
            if item['category'] == select_category:
              print(f'- {item["name"]}: ${item["price"]:.2f} - {item["quantity"]} in stock')
              item_found = True
          print('')
          if not item_found:
              print('No items found in this category.\n')
          return
        elif select_category == 0:
          return
      except ValueError:
        print('Invalid number: .Please, try again.')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.')
    
  
  def clear_inventory(self):
    if not self.inventory:
      print('No items available in the inventory.\n')
      return
    
    while True:
      try:
        confirmation = input('Are you sure you want to delete all the items in the inventory (Yes/No)? ').lower()
        if confirmation == 'yes' or confirmation == 'y':
          self.inventory.clear()
          print('All items in the inventory removed sucessfully!\n')
          self.save_inventory()
          return
        else:
          print('No changes made. All items remains the same.\n')
          return
      except TypeError as t:
        print(f'An error ocurred: {t}. Please, try again.')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.')
    

  # IMPLEMENT SUM OF STOCK, SUM OF PRICE, NUM OF ITEMS
  def save_inventory(self, filename = 'Inventory.txt'):
    if not self.inventory:
      print('No items available in the inventory.\n')
      return
    
    categories = {}

    for item in self.inventory:
      category = item['category']
      if category not in categories:
        categories[category] = []
      categories[category].append(item)
    
    sorted_category = sorted(categories.keys())

    with open(filename, 'w') as file:
      for category in sorted_category:
        file.write(f'[{category}]\n')
        for item in categories[category]:
          file.write(f'   [{item['quantity']:3d}] {item['name']}: ${item['price']:.2f}\n')
        file.write('\n')
    
    print(f'Inventory saved sucessfully to {filename}.\n')
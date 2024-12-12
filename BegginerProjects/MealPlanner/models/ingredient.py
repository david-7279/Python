from time import sleep
import json, os
INGREDIENTS_FILE = "./data/ingredients.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(0.5)
  
class Ingredient:
  def __init__(self):
    self.ingredients = []
    self.load_ingredients()

  def load_ingredients(self):
    if os.path.exists(INGREDIENTS_FILE):
      with open(INGREDIENTS_FILE, 'r') as file:
        self.ingredients = json.load(file)
    else:
      print(f"File {INGREDIENTS_FILE} does not exist.")

  def save_ingredients(self, file_path=INGREDIENTS_FILE):
    with open(file_path, 'w') as file:
      json.dump(self.ingredients, file, indent=4)

  def main_menu(self):
    choices = [1, 2, 3, 4, 0]
    while True:
      try:
        print('1. Add Ingredient')
        print('2. Update Ingredient')
        print('3. Remove Ingredient')
        print('4. View Ingredient')
        print('0. Return to the main menu')
        option = int(input('Choose an option: '))
        clear_screen()

        if option not in choices:
          print(f'Invalid option: {option}! Please, choose an valid option.')
          input('Press enter to continue...')
          clear_screen()
          continue

        if option == 1:
          self.add_ingredient()
        elif option == 2:
          self.update_ingredient()
        elif option == 3:
          self.remove_ingredient()
        elif option == 4:
          self.view_ingredients()
        elif option == 0:
          print('Going back...')
          sleep(0.8)
          clear_screen()
          return

      except ValueError:
        print(f'Invalid input! Please, try again.')
        input('Press enter to continue...')
        clear_screen()
        continue

      except Exception as e:
        print(f'An error ocurred: {e}! Please, try again.')
        input('Press enter to continue...')
        clear_screen()
        continue
        
  def add_ingredient(self):    
    while True:
      try:
        name = input('Enter the ingredient name: ').title()
        if not name or name.isdigit():
          raise ValueError
        
        quantity = int(input('Enter the ingredient quantity: '))
        if not quantity or quantity <= 0:
          raise ValueError
        
        unit = input('Enter the ingredient unit: ').title()
        if not unit or unit.isdigit():
          raise ValueError
        
        calories = int(input('Enter the ingredient calories: '))
        if not calories or calories <= 0:
          raise ValueError
      
        self.ingredients.append({"name": name, "quantity": quantity, "unit": unit, "calories": calories})
        print(f'\n{name} added successfully!')
        input('Press enter to continue...')
        clear_screen()
        break

      except ValueError:
        print('Invalid input! Please, try again.')
        input('Press enter to continue...')
        clear_screen()
        continue
      except Exception as e:
        print(f'An error ocurred: {e}! Please, try again.')
        input('Press enter to continue...')
        clear_screen()
        continue
    
  def update_ingredient(self):
    if not self.ingredients:
      print('No ingredients in the list')
      input('Press enter to continue...')
      clear_screen()
      return
    
    while True:
      try:
        for index, ingredient in enumerate(self.ingredients, start=1):
          print(f'[{index}] Name: {ingredient['name']}, Quantity: {ingredient['quantity']}, Unit: {ingredient['unit']}, Calories: {ingredient['calories']}')
        print('[0] Cancel')

        ingredient_index = int(input('Choose an ingredient to update: '))
        if 1 <= ingredient_index <= len(self.ingredients):
          selected_ingredient = self.ingredients[ingredient_index - 1]
          print(f'\nYou selected {selected_ingredient['name']}')
          input('Press enter to update the ingredient...')
          clear_screen()

          new_name = input(f'Enter the ingredient name (leave blank to keep the same [{selected_ingredient['name']}]): ').title() or selected_ingredient['name']
          
          new_quantity_input = input(f'Enter the ingredient quantity (leave blank to keep the same [{selected_ingredient['quantity']}]): ') or selected_ingredient['quantity']
          new_quantity = int(new_quantity_input) if new_quantity_input else selected_ingredient['quantity']

          new_unit = input(f'Enter the ingredient unit (leave blank to keep the same [{selected_ingredient['unit']}]): ').title() or selected_ingredient['unit']
          
          new_calories_input = input(f'Enter the ingredient calories (leave blank to keep the same [{selected_ingredient['calories']}]): ') or selected_ingredient['calories']
          new_calories = int(new_calories_input) if new_calories_input else selected_ingredient['calories']

          selected_ingredient.update({
            "name": new_name,
            "quantity": new_quantity,
            "unit": new_unit,
            "calories": new_calories
          })
          self.save_ingredients()
          print(f'\n{new_name} updated successfully!')
          input('Press enter to continue...')
          clear_screen()
          break
        elif ingredient_index == 0:
          clear_screen()
          print('Going back...')
          sleep(0.8)
          clear_screen()
          return
        
        else:
          raise ValueError

      except ValueError:
        print('Invalid input! Please, try again.')
        input('Press enter to continue...')
        clear_screen()
        continue

      except Exception as e:
        print(f'An error ocurred: {e}! Please, try again.')
        input('Press enter to continue...')
        clear_screen()
        continue

  def remove_ingredient(self):
    if not self.ingredients:
      print('No ingredients in the list')
      input('Press enter to continue...')
      clear_screen()
      return
    
    while True:
      try:
        for index, ingredient in enumerate(self.ingredients, start=1):
          print(f'[{index}] Name: {ingredient['name']}, Quantity: {ingredient['quantity']}, Unit: {ingredient['unit']}, Calories: {ingredient['calories']}')
        print('[0] Cancel')

        ingredient_index = int(input('Choose an ingredient to remove: '))
        if 1 <= ingredient_index <= len(self.ingredients):
          selected_ingredient = self.ingredients[ingredient_index - 1]
          print(f'\nYou selected {selected_ingredient['name']}')

          confirmation = input('Are you sure you want to remove this ingredient (Yes/No)? ').lower()
          clear_screen()
          if confirmation in ['yes', 'y']:
            self.ingredients.remove(selected_ingredient)
            self.save_ingredients()
            print(f'{selected_ingredient['name']} removed successfully!')
            input('Press enter to continue...')
            clear_screen()
            break
          elif confirmation in ['no', 'n']:
            print(f'{selected_ingredient['name']} not removed!')
            input('Press enter to continue...')
            clear_screen()
            continue
          else:
            print(f'Invalid confirmation: {confirmation}. Please, choose an valid confirmation')
            input('Press enter to continue...')
            clear_screen()
            continue

        elif ingredient_index == 0:
          clear_screen()
          print('Going back...')
          sleep(0.8)
          clear_screen()
          return
        else:
          raise ValueError
        
      except ValueError:
        print('Invalid input! Please, try again.')
        input('Press enter to continue...')
        clear_screen()
        continue
        
      except Exception as e:
        print(f'An error ocurred: {e}! Please, try again.') 
        input('Press enter to continue...')
        clear_screen()
        continue

  def view_ingredients(self):
    if not self.ingredients:
      print('No ingredients in the list')
      input('Press enter to continue...')
      clear_screen()
      return
    
    for index, ingredient in enumerate(self.ingredients, start=1):
      print(f'[{index}] Name: {ingredient['name']}, Quantity: {ingredient['quantity']}, Unit: {ingredient['unit']}, Calories: {ingredient['calories']}')
    
    input('\nPress enter to continue...')
    clear_screen()
    return
    if not self.ingredients:
      print('No ingredients in the list')
      input('Press enter to continue...')
      clear_screen()
      return
    
    with open(file_path, 'w') as file:
      json.dump(self.ingredients, file, indent=4)
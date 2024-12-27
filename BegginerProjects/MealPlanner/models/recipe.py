from time import sleep
from models import Ingredient
import json, os
RECIPES_FILE = "./data/recipes.json"
INGREDIENTS_FILE = "./data/ingredients.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(0.5)
  
class Recipe:
  def __init__(self):
    self.recipes = []
    self.load_recipes()
    self.ingredients = []
    self.load_ingredients()

  def load_recipes(self):
    if os.path.exists(RECIPES_FILE):
      with open(RECIPES_FILE, 'r') as file:
        self.recipes = json.load(file)
    else:
      print(f"File {RECIPES_FILE} does not exist.")

  def save_recipess(self, file_path=RECIPES_FILE):
    with open(file_path, 'w') as file:
      json.dump(self.recipes, file, indent=4)


  def load_ingredients(self):
    if os.path.exists(INGREDIENTS_FILE):
      with open(INGREDIENTS_FILE, 'r') as file:
        self.ingredients = json.load(file)
    else:
      print(f"File {INGREDIENTS_FILE} does not exist.")

  def main_menu(self):
    choices = [1, 2, 3, 4, 0]
    while True:
      try:
        print('1. Add Recipe')
        print('2. Update Recipe')
        print('3. Remove Recipe')
        print('4. View Recipe')
        print('0. Return to the main menu')
        option = int(input('Choose an option: '))
        clear_screen()

        if option not in choices:
          print(f'Invalid option: {option}! Please, choose an valid option.')
          input('Press enter to continue...')
          clear_screen()
          continue

        if option == 1:
          self.add_recipe()
        elif option == 2:
          self.update_recipe()
        elif option == 3:
          self.remove_recipe()
        elif option == 4:
          self.view_recipe()
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
        

  def add_recipe(self):   
    while True:
      try:
        title = input('Enter the recipe title: ').title()
        if not title or title.isdigit():
          raise ValueError
        
        description = input('Enter the recipe description: ')
        if not description or description.isdigit():
          raise ValueError
        
        print('\nAvailable Ingredients:')
        ingredient = Ingredient()
        for index, ingredient in enumerate(self.ingredients, start=1):
          print(f'[{index}] Name: {ingredient['name']}, Quantity: {ingredient['quantity']}, Unit: {ingredient['unit']}, Calories: {ingredient['calories']}')
    
        ingredients_input = input('Select the ingredients (separate by "," to select more than one): ')
        ingredients_list = [int(i.strip()) for i in ingredients_input.split(',') if i.strip().isdigit()]
        if not ingredients_list:
          raise ValueError
        
        #TODO After selecting the ingredient, ask for the user insert the quantity of each ingredient

        self.recipes.append({"title": title, "description": description, "ingredients": ingredients_list})
        print(f'{title} added successfully!')
        input('Press enter to continue...')
        clear_screen()
        break

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
    
  def update_recipe(self):
    if not self.recipes:
      print('No recipes in the list')
      input('Press enter to continue...')
      clear_screen()
      return

  def remove_recipe(self):
    if not self.recipes:
      print('No recipes in the list')
      input('Press enter to continue...')
      clear_screen()
      return

  def view_recipe(self):
    if not self.recipes:
      print('No recipes in the list')
      input('Press enter to continue...')
      clear_screen()
      return
    
    for index, recipe in enumerate(self.recipes, start=1):
      print(f'[{index}] {recipe["title"]}, {recipe["description"]}')
      print('    Ingredients:')
      for ingredient in recipe['ingredients']:
        print(f'     - {ingredient["name"]}: {ingredient["quantity"]} {ingredient["unit"]}')
      print('    Steps:')
      for step in recipe['steps']:
        print(f'     - {step}')
      print('')
    
    input('Press enter to continue...')
    clear_screen()
    return
    
  def save_recipe(self):
    if not self.recipes:
      print('No recipes in the list')
      input('Press enter to continue...')
      clear_screen()
      return
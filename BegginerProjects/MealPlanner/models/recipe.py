from time import sleep
import json, os
RECIPES_FILE = "./data/recipe.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(0.5)
  
class Recipe:
  def __init__(self):
    self.recipes = []

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
    if not self.recipes:
      print('No recipes in the list')
      return
    
  def update_recipe(self):
    if not self.recipes:
      print('No recipes in the list')
      return

  def remove_recipe(self):
    if not self.recipes:
      print('No recipes in the list')
      return

  def view_recipe(self):
    if not self.recipes:
      print('No recipes in the list')
      return
    
  def save_recipe(self):
    if not self.recipes:
      print('No recipes in the list')
      return
from models import Ingredient, Recipe
from time import sleep
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(0.5)

def user_main_menu():
  choices = [1, 2, 0]
  while True:
    try:
       option = int(input('Choose an option: '))
       if option in choices:
          return option
       else:
          print(f'Invalid choice: {option}. Please, choose an valid option.\n')
          input('Press enter to continue...')
    except ValueError:
       print('Invalid input. Plese, try again.')
    except Exception as e:
       print(f'An error ocurred: {e}. Please, try again.')


def main():
   clear_screen()
   print('Welcome to the Meal Planner')

   ingredient = Ingredient()
   recipe = Recipe()

   while True:
      print('1. Manage Ingredients')
      print('2. Manage Recipes')
      print('0. Exit')

      main_menu = user_main_menu()
      clear_screen()

      if main_menu == 1:
         ingredient.main_menu()
      elif main_menu == 2:
         recipe.main_menu()
      elif main_menu == 0:
         while True:
            confirmation = input('Are your sure you want to exit the Meal Planner (Yes/No)? ').lower()
            clear_screen()
            if confirmation in ['yes', 'y']:
               print('Goodbye, have a nice day')
               exit()
            elif confirmation in ['no', 'n']:
               print('I\'m glad that you stay')
               input('Press enter to continue...')
               clear_screen()
               break
            else:
               print(f'Invalid confirmation: {confirmation}. Please, choose an valid confirmation')
               input('Press enter to continue...')
               continue


if __name__ == "__main__":
    main()
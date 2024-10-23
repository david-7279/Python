from game import Game
from time import sleep
import os

# Cleart the console
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  sleep(0.5)


# User menu choice
def user_main_menu():
  choices = [1, 2, 3, 4, 0]
  while True:
    try:
      option = int(input('Choose an option: '))
      if option in choices:
        return option
      else:
        print(f'Invalid option: {option}. Please, choose an valid choice.\n')
    except ValueError:
      print(f'Invalid input: {option}. Please, write an valid number.\n')
    except Exception as e:
      print(f'An error ocurred: {e}. Please, try again.\n')


# Show current town
def show_current_town():
  print(f'Current town')


# Main program
def main():
  clear_screen()
  game = Game()

  # Towns definitions
  towns = [
    {"name": "Water Town", "description": "slime, they seem cute but they are dangerous"},
    {"name": "Olympus Town", "description": "zombie, the monsters here are strong and wise"},
    {"name": "Dark Town", "description": "vampire, a spooky place, home of dark creatures"},
    {"name": "Mountain Town", "description": "werewolf, monsters live in the high peaks"},
    {"name": "Cloud Town", "description": "globin, monsters float in the skies"},
    {"name": "Elf Town", "description": "gnome, a peaceful town but full of mysterious elves"},
    {"name": "Tokyo Town", "description": "oni, a modern town with legendary monsters"}
  ]

  print('Hello to Console Game. The main objetive its to defeat the dangerous fox!')
  print(f'Welcome to {towns[0]['name']} the main monster here is a {towns[0]['description']}.\n')

  while True:
    print('1. Go to the shop')
    print(f'2. Go to the next town ({towns[1]['name']})')
    print('3. Go to the cave')
    print('4. Go fight the boos')
    print('0. Leave the program')

    option = user_main_menu()
    clear_screen()
    
    if option == 1:
      game.shop()
    elif option == 2:
      game.next_town()
    elif option == 3:
      game.cave()
    elif option == 3:
      game.boss_fight()
    else:
      print('Goodbye Adventure!')
      break
    

# Call the main program
if __name__ == '__main__':
  main()
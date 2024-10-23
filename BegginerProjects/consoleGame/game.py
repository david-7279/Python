from time import sleep
import os

# Cleart the console
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  sleep(0.5)

# PLAYER STATUS
player = [
  {"healh": 0, "money": 50, "weapon": "hand", "power": 0, "monsters": 0, "boss": 0}
]

# SHOP ITEMS
weapon_items = [
  {"name": "hand", "category": "none", "power": 5, "health": 50, "price": 0},
  {"name": "stick", "category": "wood", "power": 10, "health": 100, "price": 10},
  {"name": "wood sword", "category": "wood", "power": 15, "health": 100, "price": 15},
  {"name": "bow", "category": "wood", "power": 25, "health": 50, "price": 20},
  {"name": "stone sword", "category": "sword", "power": 20, "health": 110, "price": 20},
  {"name": "metal sword", "category": "sword", "power": 25, "health": 90, "price": 23},
  {"name": "double metal sword", "category": "sowrd", "power": 35, "health": 150, "price": 30},
  {"name": "katana", "category": "katana", "power": 45, "health": 100, "price": 30},
  {"name": "bow with mythic magic", "category": "magic", "power": 55, "health": 50, "price": 45},
  {"name": "bow with fire magic", "category": "magic", "power": 55, "health": 50, "price": 45},
  {"name": "bow with ice magic", "category": "magic", "power": 55, "health": 50, "price": 45},
  {"name": "bow with dark magic", "category": "magic", "power": 60, "health": 40, "price": 45},
  {"name": "santoryu", "category": "katana", "power": 70, "health": 200, "price": 60},
  {"name": "santoryu with dark magic", "category": "katana", "power": 90, "health": 120, "price": 60},
  {"name": "mythical dark magic", "category": "magic", "power": 120, "health": 120, "price": 120},
  {"name": "katana mythical dark magic", "category": "magic", "power": 180, "health": 150, "price": 200},
  {"name": "santoryu mythical dark magic", "category": "magic", "power": 200, "health": 100, "price": 220},
]

health_items = [
  {"name": "small potion health", "category": "item", "health": 15, "price": 5},
  {"name": "medium potion health", "category": "item", "health": 45, "price": 35},
  {"name": "big potion health", "category": "item", "health": 70, "price": 50},
]

# TOWNS
town = [
  {"name": "water town"},
  {"name": "olympsus town"},
  {"name": "dark town"},
  {"name": "montain town"},
  {"name": "cloud town"},
  {"name": "elf town"},
  {"name": "tokyo town"},
]

# MONSTER STATUS
monsters = [
  {"name": "slime", "health": 10, "power": 10, "reward": 1},
  {"name": "zombie", "health": 15, "power": 20, "reward": 2},
  {"name": "vampire", "health": 20, "power": 30, "reward": 2},
  {"name": "werewolf", "health": 25, "power": 40, "reward": 5},
  {"name": "goblin", "health": 30, "power": 50, "reward": 5},
  {"name": "gnome", "health": 40, "power": 60, "reward": 7},
  {"name": "oni", "health": 60, "power": 70, "reward": 10},
]

# BOSS STATUS
boss = [
  {"name": "evil fox", "health": 200, "power": 110}
]


class Game:
  def __init__(self):
    pass

  def shop(self):
    choices = [1, 2, 0]
    while True:
      try:
        print('Shopping list')
        print('1. shopping health items')
        print('2. shopping weapons')
        print('0. go back')

        option = int(input('Choose an option: '))
        clear_screen()
        if option in choices:
          # HEALTH SELECTED
          if option == 1:
            if player['money'] <= health_items['price']:
              for index, health in enumerate(health_items, start=1):
                print(f'[{index}] {health['name']}, health gain [{health['health']}] costs ${health['price']}')
              print('[0] go back')
              
            item_index = int(input('Choose an health potion: '))
            if 1 <= item_index <= len(health_items):
              selected_helth = health_items[item_index - 1]
              if selected_helth['price'] > player['money']:
                print(f'Not enough money to pursache this item.\n')
              else:
                print(f'Selected helth item: {selected_helth['name']}')
                print('Item pursached sucessfully!\n')
                player['money'] -= selected_helth['price']
                player['health'] += selected_helth['health']
                print(f'Player status: \nHealth: {player['health']}, Money:{player['money']}\n')
            else:
              print(f'Invalid item: {item_index}. Please, choose an valid item!\n')
              clear_screen()
              continue   

          # WEAPON SELECTED       
          elif option == 2:
            if weapon_items['price'] <= player['money']:
              for index, weapon in enumerate(weapon_items, start=1):
                print(f'[{index}] {weapon['name']}, weapon power {weapon['power']} ({weapon['category']}), weapon health {weapon['health']} costs ${weapon['price']}')
              print('[0] go back')

              item_index = int(input('Choose an weapon: '))
              if 1 <= item_index <= len(weapon_items):
                selected_weapon = weapon_items[item_index - 1]
                if selected_weapon['price'] > player['money']:
                  print(f'No enough money to purshace this item.\n')
                else:
                  print(f'Seleted weapon: {selected_weapon['name']}')
                  print('Item purshaced sucessfully!\n')
                  player['money'] -= selected_weapon['price']
                  player['weapon'] = selected_weapon['name']
                  player['power'] = selected_weapon['power']
              else:
                print(f'Invalid item: {item_index}. Please, choose an valid item!\n')
                clear_screen()
                continue
            else:
              print(f'Not enough money: ${player['money']} to purshce an weapon!\n')
          # EXITING THE SHOP
          elif option == 0:
            print('Exiting the shop\n')
            clear_screen()
            return
          
          else:
            print(f'Invalid option: {option}. Please, choose an valid option.\n')
        else:
          print(f'Invalid option: {option}. Please, choose an valid option.\n')
      except ValueError:
        print('Invalid input. Please, try again.\n')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.\n')
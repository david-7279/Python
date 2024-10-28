from time import sleep
import os

# Cleart the console
def clear_screen():
  sleep(1)
  os.system('cls' if os.name == 'nt' else 'clear')

# PLAYER STATUS
player = [
  {"health": 100, "money": 5, "weapon": "hand", "power": 5, "monsters": 0, "boss": 0}
]

# SHOP ITEMS
weapon_items = [
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
  def __init__(self, towns):
    self.towns = towns
    self.current_town_index = 0

  def main_menu(self):
    choices = [1, 2, 3, 4, 5, 0]
    while True:
      try:
        current_town = self.towns[self.current_town_index]
        town_name = current_town['name']
        description = current_town['description']

        print(f'Welcome to {town_name} the main monster here is a {description}.\n')
        print('1. Go to the shop')
        # Show enxt town if exist other town
        if self.current_town_index < len(self.towns) - 1:
          print(f'2. Go to the next town ({self.towns[self.current_town_index + 1]['name']})')
        # Show previous town if exists the user navigation between towns
        if self.current_town_index > 0:
          print(f'3. Go to the next town ({self.towns[self.current_town_index - 1]['name']})')
        print('4. Go to the cave')
        print('5. Go fight the boos')
        print('0. Leave the program')

        option = int(input('Choose an option: '))
        clear_screen()
        if option in choices:
          if option == 1:
            self.shop()
          elif option == 2:
            self.next_town()
          elif option == 3:
            self.prev_town()
          elif option == 4:
            print("Going to fight the monsters... (função não implementada ainda)")
          elif option == 5:
            print("Going to fight the boss... (função não implementada ainda)")
          elif option == 0:
            print('Goodbye Adventure!')
            break
          else:
            print('Option not available for the current town.')
        else:
          print(f'Invalid option: {option}. Please, write a valid option.\n')

      except ValueError:
        print('Invalid input. Please, try again.\n')
      except Exception as e:
        print(f'An error occurred: {e}. Please, try again.\n')


  def shop(self):
    choices = [1, 2, 0]
    while True:
      try:
        print('Player status')
        print(f'Player health: {player[0]['health']}, Player money: ${player[0]['money']}, Player weapon: {player[0]['weapon']}, Player Power: {player[0]['power']}\n')

        print('Shopping list')
        print('1. shopping health items')
        print('2. shopping weapons')
        print('0. go back')

        option = int(input('Choose an option: '))
        clear_screen()

        if option in choices:
          # HEALTH SELECTED
          if option == 1:
            print('Player status')
            print(f'Player health: {player[0]['health']} Player money: ${player[0]['money']}\n')

            available_health_items = [item for item in health_items if item['price'] <= player[0]['money']]

            if not available_health_items:
              print("You don't have enough money to buy any health items.\n")
              sleep(2)
              clear_screen()
              continue

            print('Health potions available to buy:')
            for index, health in enumerate(available_health_items, start=1):
              if health['price'] <= player[0]['money']:
                print(f'[{index}] {health["name"]}, health gain [{health["health"]}] costs ${health["price"]}')
            print('[0] Go back')
              
            item_index = int(input('Choose an health potion: '))
            if 1 <= item_index <= len(health_items):
              selected_helth = health_items[item_index - 1]
              if selected_helth['price'] > player[0]['money']:
                print(f'Not enough money to purchase this item.\n')
                return
              else:
                print(f'\nSelected helth item: {selected_helth['name']}')
                player[0]['money'] -= selected_helth['price']
                player[0]['health'] += selected_helth['health']
                print('Item purchased successfully!\n')
                sleep(2)
                clear_screen()
            else:
              print(f'Invalid item: {item_index}. Please, choose an valid item!\n')
              sleep(2)
              clear_screen()
              continue
                 
          # WEAPON SELECTED       
          elif option == 2:
            print('Player status')
            print(f'Player money: ${player[0]['money']}, Player weapon: {player[0]['weapon']}, Player Power: {player[0]['power']}\n')

            available_weapon_items = [item for item in weapon_items if item['price'] <= player[0]['money']]

            if not available_weapon_items:
              print("You don't have enough money to buy any weapon items.\n")
              sleep(2)
              clear_screen()
              continue

            print('Weapons available to buy:')
            for index, weapon in enumerate(available_weapon_items, start=1):
              if weapon['price'] <= player[0]['money']:
                print(f'[{index}] {weapon['name']}, weapon power {weapon['power']} ({weapon['category']}), weapon health {weapon['health']} costs ${weapon['price']}')
            print('[0] go back')

            item_index = int(input('Choose an weapon: '))
            if 1 <= item_index <= len(weapon_items):
              selected_weapon = weapon_items[item_index - 1]
              if selected_weapon['price'] > player[0]['money']:
                print(f'No enough money to purshace this item.\n')
              else:
                  print(f'\nSeleted weapon: {selected_weapon['name']}')
                  player[0]['money'] -= selected_weapon['price']
                  player[0]['weapon'] = selected_weapon['name']
                  player[0]['power'] = selected_weapon['power']
                  print('Item purshaced sucessfully!\n')
                  sleep(2)
                  clear_screen()
            else:
                print(f'Invalid item: {item_index}. Please, choose an valid item!\n')
                sleep(2)
                clear_screen()
                continue

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


  def next_town(self):
    if self.current_town_index < len(self.towns) - 1:
        clear_screen()
        print('Traveling to the next town ... ')
        self.current_town_index += 1
        clear_screen()
    else:
        print("You are already in the last town.")

  def prev_town(self):
    if self.current_town_index > 0:
        clear_screen()
        print('Traveling to the previous town ... ')
        self.current_town_index -= 1
        clear_screen()
    else:
        print("You are already in the first town.")

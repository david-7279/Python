from time import sleep
import os

# Cleart the console
def clear_screen():
  sleep(1)
  os.system('cls' if os.name == 'nt' else 'clear')

# PLAYER STATUS
player = [
  {"health": 100, "money": 10, "weapon": "hand", "power": 5, "monsters": 0, "boss": 0}
]

# SHOP ITEMS
weapon_items = [
    {"name": "stick", "category": "wood", "power": 10, "price": 10},
    {"name": "wood sword", "category": "wood", "power": 15, "price": 15},
    {"name": "bow", "category": "wood", "power": 20, "price": 20},

    {"name": "stone sword", "category": "sword", "power": 20, "price": 20},
    {"name": "metal sword", "category": "sword", "power": 25, "price": 25},
    {"name": "double metal sword", "category": "sword", "power": 35, "price": 30},

    {"name": "katana", "category": "katana", "power": 45, "price": 30},
    {"name": "santoryu", "category": "katana", "power": 70, "price": 60},
    {"name": "santoryu with dark magic", "category": "katana", "power": 90, "price": 80},

    {"name": "bow with mythic magic", "category": "magic", "power": 55, "price": 60},
    {"name": "bow with fire magic", "category": "magic", "power": 55, "price": 60},
    {"name": "bow with ice magic", "category": "magic", "power": 55, "price": 60},
    {"name": "bow with dark magic", "category": "magic", "power": 60, "price": 60},
    {"name": "mythical dark magic", "category": "magic", "power": 120, "price": 90},
    {"name": "katana mythical dark magic", "category": "magic", "power": 180, "price": 150},
    {"name": "santoryu mythical dark magic", "category": "magic", "power": 200, "price": 220},
]

health_items = [
  {"name": "small potion health", "category": "item", "health": 15, "price": 5},
  {"name": "medium potion health", "category": "item", "health": 50, "price": 35},
  {"name": "big potion health", "category": "item", "health": 75, "price": 50},
]

# MONSTER STATUS
monsters = [
  {"name": "slime", "health": 10, "power": 10, "reward": 5},
  {"name": "zombie", "health": 15, "power": 20, "reward": 10},
  {"name": "vampire", "health": 20, "power": 30, "reward": 15},
  {"name": "werewolf", "health": 25, "power": 40, "reward": 25},
  {"name": "goblin", "health": 30, "power": 50, "reward": 30},
  {"name": "gnome", "health": 40, "power": 60, "reward": 45},
  {"name": "oni", "health": 60, "power": 70, "reward": 60},
]

# BOSS STATUS
boss = [
  {"name": "evil fox", "health": 200, "power": 120}
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
        print('1. go to the shop')
        # Show enxt town if exist other town
        if self.current_town_index < len(self.towns) - 1:
          print(f'2. go to the next town ({self.towns[self.current_town_index + 1]['name']})')
        # Show previous town if exists the user navigation between towns
        if self.current_town_index > 0:
          print(f'3. go to the next town ({self.towns[self.current_town_index - 1]['name']})')
        print('4. go to the cave')
        print('5. fight the boss')
        print('0. leave the program')

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
            self.fight_monster()
          elif option == 5:
            print("Going to fight the boss... (feature not implemented yet)")
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
        print('0. leave the shop')

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
            print('[0] go back')
              
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
            elif item_index == 0:
                clear_screen()
                print('Leaving the shop ... ')
                clear_screen()
                return
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
                print(f'[{index}] {weapon['name']} ({weapon['category']}), weapon power {weapon['power']} costs ${weapon['price']}')
            print('[0] go back')

            item_index = int(input('Choose an weapon: '))
            if 1 <= item_index <= len(weapon_items):
              selected_weapon = weapon_items[item_index - 1]
              if selected_weapon['price'] > player[0]['money']:
                print(f'No enough money to purshace this item.\n')
              
                return
              else:
                  print(f'\nSeleted weapon: {selected_weapon['name']}')
                  player[0]['money'] -= selected_weapon['price']
                  player[0]['weapon'] = selected_weapon['name']
                  player[0]['power'] += selected_weapon['power']
                  print('Item purshaced sucessfully!\n')
                  sleep(1.5)
                  clear_screen()
            elif item_index == 0:
              clear_screen()
              print('Leaving the shop ... ')
              clear_screen()
              return
            else:
                print(f'Invalid item: {item_index}. Please, choose an valid item!\n')
                sleep(2)
                clear_screen()
                continue

          # EXITING THE SHOP
          elif option == 0:
            print('Exiting the shop ...')
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


  def fight_monster(self):
    choices = [1, 2, 0]
    while True:
      try:
        current_monster = monsters[self.current_town_index]
        print("Monster status")
        print(f"Name: {current_monster['name']}, Health: {current_monster['health']}, Power: {current_monster['power']}, Reward: ${current_monster['reward']}\n")

        print("1. go to the shop")
        print("2. fight the monsters")
        print("0. leave the cave")

        option = int(input("Choose an option: "))
        clear_screen()

        if option in choices:
          # GO TO THE SHOP
          if option == 1:
            clear_screen()
            print("Going to the shop ... ")
            clear_screen()
            self.shop()

          # FIGHT THE CAVE MONSTER
          elif option == 2:
            clear_screen()
            fight_choices = ['a', 'l']
            while True:
              print("Player status")
              print(f"Health: {player[0]['health']}, Weapon: {player[0]['weapon']}, Power: {player[0]['power']}\n")

              print("Monster status")
              print(f"Name: {current_monster['name']}, Health: {current_monster['health']}, Power: {current_monster['power']}\n")

              print("a. to attack")
              print("l. leave the monster basement")

              action = input("Choose an action: ").lower()
              if action in fight_choices:
                # ATTACK THE MONSTER BASEMENT
                if action == 'a':
                  clear_screen()
                  player_power = player[0]['power']
                  player_health = player[0]['health']
                  monster_power = current_monster['power']
                  monster_health = current_monster['health']
                  
                  if player_power < monster_power or player_health < monster_health:
                    print("Your current power and health is lower than the monster")
                    confirmation = input("Are you sure you want to fight the monster (Yes/No)? ").lower()

                    if confirmation in ['yes', 'y']:
                      clear_screen()
                      while monster_health > 0:
                        monster_health -= player_power
                        player_health -= monster_power
                        player[0]['health'] = player_health

                        if monster_health <= 0:
                          print(f"You took some damage from {current_monster['name']}, but you defeated him!\n")
                          player[0]['money'] += current_monster['reward']
                          player[0]['monsters'] += 1

                          continue
                        elif player_health <= 0:
                          clear_screen()
                          print(f"You died!\nYou fought bravely and defeated {player[0]['monsters']} monsters in total.")
                          return

                        clear_screen()
                        continue
                    elif confirmation in ['no', 'n']:
                      clear_screen()
                      print("Leaving the monster basement ... ")
                      clear_screen()
                      return
                    
                    else:
                      print(f"Invalid confirmation: {confirmation}\n")
                      clear_screen()
                      return
                  
                  else:
                    while monster_health > 0:
                      monster_health -= player_power
                      player_health -= monster_power
                      player[0]['health'] = player_health

                      if monster_health <= 0:
                        print(f"You defeated {current_monster['name']}!\n")
                        player[0]['money'] += current_monster['reward']
                        player[0]['monsters'] += 1
                        continue
                      elif player_health <= 0:
                        clear_screen()
                        print(f"You died!\nYou fought bravely and defeated {player[0]['monsters']} monsters in total.")
                        return

                # LEAVE THE MONSTER BASEMENT
                elif action == 'l':
                  clear_screen()
                  print("Leaving the monster basement ... ")
                  clear_screen()
                  return
                else:
                  print(f"Invalid action: {action}! Please, try again.\n")
                  clear_screen()
                  continue
          # LEAVE THE CAVE
          elif option == 0:
            clear_screen()
            print("Exiting the cave ...")
            clear_screen()
            return
        else:
          print(f"Invalid option: {option}. Please, choose a valid option.\n")
          continue

      except ValueError:
        print("Invalid input. Please, try again.\n")
      except Exception as e:
        print(f"An error occurred: {e}. Please, try again.\n")


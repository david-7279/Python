from time import sleep
import os, random

# Cleart the console
def clear_screen():
  sleep(1)
  os.system('cls' if os.name == 'nt' else 'clear')

# PLAYER STATUS
player = [
  {"health": 100, "money": 15, "weapon": "Hand", "power": 5, "monsters": 0, "boss": 0}
]

# SHOP ITEMS
weapon_items = [
    {"name": "Stick", "category": "wood", "power": 6, "price": 5},
    {"name": "Wood Sword", "category": "wood", "power": 7, "price": 7},
    {"name": "Bow", "category": "wood", "power": 8, "price": 9},

    {"name": "Stone Sword", "category": "sword", "power": 13, "price": 35},
    {"name": "Metal Sword", "category": "sword", "power": 15, "price": 38},
    {"name": "Double Metal Sword", "category": "sword", "power": 16, "price": 45},

    {"name": "Katana", "category": "katana", "power": 18, "price": 90},
    {"name": "Santoryu", "category": "katana", "power": 20, "price": 97},
    {"name": "Santoryu Dark Magic", "category": "katana", "power": 23, "price": 120},

    {"name": "Bow Mythic Magic", "category": "magic", "power": 28, "price": 189},
    {"name": "Bow Fire Magic", "category": "magic", "power": 34, "price": 197},
    {"name": "Bow Ice Magic", "category": "magic", "power": 38, "price": 218},
    {"name": "Bow Dark Magic", "category": "magic", "power": 42, "price": 250},

    {"name": "Mythical Dark magic", "category": "magic", "power": 60, "price": 575},
    {"name": "Katana Mythical Dark Magic", "category": "magic", "power": 66, "price": 670},
    {"name": "Santoryu Mythical Dark Magic", "category": "magic", "power": 80, "price": 975},
]

health_items = [
  {"name": "small potion health", "category": "item", "health": 30, "price": 20},
  {"name": "medium potion health", "category": "item", "health": 50, "price": 45},
  {"name": "big potion health", "category": "item", "health": 120, "price": 95},
  {"name": "maxium potion health", "category": "item", "health": 200, "price": 140},
]

# MONSTER STATUS
monsters = [
  {"name": "Slime", "health": 7, "original_health": 7, "power": 6, "reward": 4},
  {"name": "Zombie", "health": 14, "original_health": 14, "power": 10, "reward": 15},
  {"name": "Vampire", "health": 20, "original_health": 20, "power": 18, "reward": 23},
  {"name": "Werewolf", "health": 26, "original_health": 26, "power": 22, "reward": 29},
  {"name": "Goblin", "health": 39, "original_health": 39, "power": 35, "reward": 35},
  {"name": "Gnome", "health": 44, "original_health": 44, "power": 40, "reward": 43},
  {"name": "Oni", "health": 55, "original_health": 55, "power": 65, "reward": 62},
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
          print(f'3. go to the previous town ({self.towns[self.current_town_index - 1]['name']})')
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
            while True:
              confirmation = input('Are you sure you want to leave the program (Yes/No)? ')
              if confirmation in ['yes', 'y']:
                sleep(0.5)
                clear_screen()
                print('Goodbye Adventure!')
                return
              elif confirmation in ['no', 'n']:
                print('Still ready for some adventure!\n')
                sleep(1)
                clear_screen()
                self.main_menu()
              else:
                print(f'Invalid confirmation: {confirmation}! Please, write an valid confirmation.')
                input('Press enter to continue...')
                clear_screen()
                continue
          else:
            print('Option not available for the current town.')
        else:
          print(f'Invalid option: {option}. Please, write a valid option.\n')

      except ValueError:
        print('Invalid input. Please, try again.\n')
        input('Press enter to continue...')
        clear_screen()
        continue
      except Exception as e:
        print(f'An error occurred: {e}. Please, try again.\n')
        input('Press enter to continue...')
        clear_screen()
        continue


  def shop(self):
    choices = [1, 2, 0]
    while True:
      try:
        print(f'Player status\nHealth: {player[0]["health"]}, Weapon: {player[0]["weapon"]}, Power: {player[0]["power"]}, Money: ${player[0]["money"]}\n')

        print('1. shop health items')
        print('2. shop weapons')
        print('0. leave the shop')

        option = int(input('Choose an option: '))
        clear_screen()

        if option in choices:
          if option == 1:
            self.shop_health_items()
          elif option == 2:
            self.shop_weapons()
          elif option == 0:
            print('Exiting the shop...')
            clear_screen()
            return
        else:
          print(f'Invalid option: {option}. Please, choose an valid option!\n')
          input('Press enter to continue...')
          clear_screen()
          continue
      except ValueError:
        print('Invalid input. Please, try again!\n')
        input('Press enter to continue...')
        clear_screen()
        continue


  def shop_health_items(self):
    available_health_items = [item for item in health_items if item['price'] <= player[0]['money']]
    if not available_health_items:
      print("You don't have enough money to buy any health items.")
      input('Press enter to continue...')
      clear_screen()
      return

    print(f'Player status\nHealth: {player[0]['health']}, Money: ${player[0]['money']}\n')
    print('Health potions available to buy:')
    for index, health in enumerate(available_health_items, start=1):
      print(f'[{index}] {health["name"]}, health gain [{health["health"]}], price ${health["price"]}')
    print('[0] go back')

    item_index = int(input('Choose a health potion: '))
    if 1 <= item_index <= len(available_health_items):
      selected_health = available_health_items[item_index - 1]
      if selected_health['price'] > player[0]['money']:
        print('You don\'t have enough money to purchase this item.')
        input('Press enter to continue...')
        clear_screen()
        return
      else:
        while True:
          try:
            confirmation = input('Are you sure want to buy this item (Yes/No)? ').lower()
            if confirmation in ['yes', 'y']:
              player[0]['money'] -= selected_health['price']
              player[0]['health'] += selected_health['health']
              print(f'You bought {selected_health["name"]} and gained {selected_health["health"]} health.\n')
              input('Press enter to continue...')
              clear_screen()
              return
            elif confirmation in ['no', 'n']:
              print('Health remains the same\n')
              input('Press enter to continue...')
              clear_screen()
              return
            else:
              print('Invalid confirmation!\n')
              input('Press enter to continue...')
              clear_screen()
              continue
          except ValueError:
            print('Invalid input! Please, try again.\n')
            input('Press enter to continue...')
            clear_screen()
            continue
          except Exception as e:
            print(f'An error ocurred: {e}! Please, try again.\n')
            input('Press enter to continue...')
            clear_screen()
            continue
    elif item_index == 0:
      clear_screen()
      return
    else:
      print('Invalid option. Please try again.')  
      input('Press enter to continue...')
      clear_screen()


  def shop_weapons(self):
    available_weapons = [weapon for weapon in weapon_items if weapon['price'] <= player[0]['money']]
    if not available_weapons:
      print("You don't have enough money to buy any weapons.")
      input('Press enter to continue...')
      clear_screen()
      return

    print(f'Player status\nWeapon: {player[0]['weapon']}, Power: {player[0]['power']}, Money: ${player[0]['money']}\n')
    print('Weapons available to buy:')
    for index, weapon in enumerate(available_weapons, start=1):
      print(f'[{index}] {weapon["name"]}, power [{weapon["power"]}], price ${weapon["price"]}')
    print('[0] go back')

    weapon_index = int(input('Choose a weapon: '))
    if 1 <= weapon_index <= len(available_weapons):
      selected_weapon = available_weapons[weapon_index - 1]
      if selected_weapon['price'] > player[0]['money']:
        print('You don\'t have enough money to purchase this weapon.')
        input('Press enter to continue...')
        clear_screen()
        return
      else:
        while True:
          try:
            confirmation = input('Are you sure want to buy this item (Yes/No)? ').lower()
            if confirmation in ['yes', 'y']:
              # HANDLE CURRENT POWER VS POWER THAT PLAYER BOUGHT
              player[0]['money'] -= selected_weapon['price']
              player[0]['weapon'] = selected_weapon['name']
              player[0]['power'] = selected_weapon['power']
              print(f'You bought {selected_weapon["name"]} and your current power is {selected_weapon["power"]}.\n')
              input('Press enter to continue...')
              clear_screen()
              return
            elif confirmation in ['no', 'n']:
              print('Weapon remains the same\n')
              input('Press enter to continue...')
              clear_screen()
              return
            else:
              print('Invalid confirmation!\n')
              input('Press enter to continue...')
              clear_screen()
              continue
          except ValueError:
            print('Invalid input! Please, try again.\n')
            input('Press enter to continue...')
            clear_screen()
            continue
          except Exception as e:
            print(f'An error ocurred: {e}! Please, try again.\n')
            input('Press enter to continue...')
            clear_screen()
            continue
    elif weapon_index == 0:
      clear_screen()
      return
    else:
      print('Invalid option. Please try again.')
      input('Press enter to continue...')
      clear_screen()


  def next_town(self):
    if self.current_town_index < len(self.towns) - 1:
        print('Traveling to the next town ... ')
        self.current_town_index += 1
        clear_screen()
    else:
        print("You are already in the last town.")
        input('Press enter to continue...')
        clear_screen()


  def prev_town(self):
    if self.current_town_index > 0:
        print('Traveling to the previous town ... ')
        self.current_town_index -= 1
        clear_screen()
    else:
        print("You are already in the first town.")
        input('Press enter to continue...')
        clear_screen()


  def calculate_damage_taken(self, attacker_power, monster_power):
    base_damage = attacker_power
    defense_reduction = max(0, monster_power * 0.3)
    minimum_damage = max(1, int(attacker_power * 0.1))
    randomness = random.uniform(0.95, 1.05)
    damage_taken = max(minimum_damage, int((base_damage - defense_reduction) * randomness))
    return damage_taken


  def fight_monster(self):
    choices = [1, 2, 0]
    while True:
      try:
        current_monster = monsters[self.current_town_index]
        print("Monster status")
        print(f"Name: {current_monster['name']}, Health: {current_monster['health']}, Power: {current_monster['power']}, Reward: ${current_monster['reward']}\n")

        print("1. go to the shop")
        print("2. fight the monster")
        print("0. leave the cave")

        option = int(input("Choose an option: "))
        clear_screen()

        if option not in choices:
          print(f'Invalid option: {option}! Please, write an valid option.')
          input('Press any key to continue ...')
          clear_screen()
          continue

        # GO TO THE SHOP
        if option == 1:
            print("Going to the shop ... ")
            clear_screen()
            self.shop()

        # FIGHT THE CAVE MONSTER
        elif option == 2:
            fight_choices = ['a', 'l']
            while True:
              print("Player status")
              print(f"Health: {player[0]['health']}, Power: {player[0]['power']}, Weapon: {player[0]['weapon']}\n")

              print("Monster status")
              print(f"Health: {current_monster['health']}, Power: {current_monster['power']}, Reward: ${current_monster['reward']}\n")

              action = input("a. to attack\nl. leave the monster basement\nChoose an action: ").lower()
              clear_screen()

              if action not in fight_choices:
                print(f'Invalid action: {action}! Please, write an valid action.')
                input('Press any key to continue ... ')
                clear_screen()
                continue

              # ATTACK THE MONSTER BASEMENT
              if action == 'a':
                player_power = player[0]['power']
                monster_power = current_monster['power']

                # Calcular dano sofrido pelo jogador
                player_damage_taken = self.calculate_damage_taken(monster_power, player_power)
                player[0]['health'] -= player_damage_taken

                # Calcular dano causado ao monstro
                monster_damage_taken = self.calculate_damage_taken(player_power, monster_power)
                current_monster['health'] -= monster_damage_taken

                # CHECK THE OUTCOMER
                if current_monster['health'] <= 0:
                    print(f"You defeated the {current_monster['name']} and earned ${current_monster['reward']}!")
                    player[0]['money'] += current_monster['reward']
                    player[0]['monsters'] += 1
                    # Reset monster's current health to its original health for the next encounter
                    current_monster['health'] = current_monster['original_health']
                    input('Press enter to continue...')
                    clear_screen()
                    continue
                elif player[0]["health"] <= 0:
                  clear_screen()
                  print(f"You died!\nYou fought bravely and defeated {player[0]['monsters']} monsters in total.")
                  if not self.revive_player():
                    print('Game Over!')
                    exit()
                  clear_screen()
                  return
                       
              # LEAVE THE MONSTER BASEMENT
              elif action == 'l':
                  print("Leaving the monster basement ... ")
                  clear_screen()
                  return
        # LEAVE THE CAVE
        elif option == 0:
          print("Exiting the cave ...")
          clear_screen()
          return
        else:
          print(f'Invalid option: {option}! Please, choose an valid option.')
          input('Press enter to continue...')
          clear_screen()
          continue
      except ValueError:
        print("Invalid input. Please, try again.\n")
        input('Press enter to continue...')
        clear_screen()
        continue
      except Exception as e:
        print(f"An error occurred: {e}. Please, try again.\n")
        input('Press enter to continue...')
        clear_screen()
        continue


  def revive_player(self):
    while True:
      try:
        print(f"Your current money is ${player[0]['money']}")
        revive_option = input("Revive cost $20. Would you like to revive? (Yes/No): ").lower()
        clear_screen()

        if revive_option in ['yes', 'y']:
          if player[0]['money'] < 20:
            print("You don't have enough money for a revival.\n")
            exit
            return False
          
          player[0]['health'] = 30  # Reset health
          player[0]['money'] -= 20
          print("You have been revived!\n")
          return True

        elif revive_option in ['no', 'n']:
          print("You chose not to revive.")
          return False

        else:
          print("Invalid input. Please choose 'Yes' or 'No'.\n")
          input('Press enter to continue...')
          clear_screen()
          continue

      except ValueError:
        print("Invalid input. Please, try again.\n")
        input('Press enter to continue...')
        clear_screen()
        continue
      except Exception as e:
        print(f"An error occurred: {e}. Please, try again.\n")
        input('Press enter to continue...')
        clear_screen()
        continue
from game import Game
from time import sleep
import os

# Clear the console
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(0.5)

# TOWNS
towns = [
    {"name": "Water Town", "description": "slime, they seem cute but they are dangerous"},
    {"name": "Olympus Town", "description": "zombie, the monsters here are strong and wise"},
    {"name": "Dark Town", "description": "vampire, a spooky place, home of dark creatures"},
    {"name": "Mountain Town", "description": "werewolf, monsters live in the high peaks"},
    {"name": "Cloud Town", "description": "goblin, monsters float in the skies"},
    {"name": "Elf Town", "description": "gnome, a peaceful town but full of mysterious elves"},
    {"name": "Tokyo Town", "description": "oni, a modern town with technological monsters"}
]

# Main program
def main():
    clear_screen()
    game = Game(towns)

    print('Welcome to the Console Game. The main objective is to defeat the dangerous fox!')

    sleep(2)
    game.main_menu()

# Call the main program
if __name__ == '__main__':
    main()
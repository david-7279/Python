from anime import Anime
from time import sleep
import os

# Clear terminal
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  sleep(0.5)

def user_main_menu():
  choices = [1, 2, 3, 4, 5, 0]
  while True:
    try:
      option = int(input('Choose an option: '))
      if option in choices:
        return option
      else:
        print(f'Invalid option: {option}. Please, choose an valid option.\n')
    except ValueError():
      print(f'Invalid number. Please, write an valid number.\n')
    except Exception as e:
      print(f'An error ocurred: {e}. Please, try again.\n')


# Main Program
def main():
  os.system('cls' if os.name == 'nt' else 'clear')
  anime = Anime()
  print('Welcome to the anime recomendation. Here we recommend an anime for you.\n')
  
  while True:
    print('1. recommend a random anime')
    print('2. recommend a random anime based on genre')
    print('3. recommend a random anime based on type')
    print('4. search for an anime by name')
    print('5. view all animes')
    print('0. for leave the program\n')

    option = user_main_menu()
    clear_screen()

    if option == 1:
      anime.random_anime()
    elif option == 2:
      anime.based_genre_anime()
    elif option == 3:
      anime.based_type_anime()
    elif option == 4:
      anime.search_anime_by_name()
    elif option == 5:
      anime.view_all_animes()
    elif option == 0:
      print('Goodbye!')
      break


# Call the main program
if __name__ == '__main__':
  main()
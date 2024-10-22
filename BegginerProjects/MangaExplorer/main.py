from manga import Manga
from time import sleep
import os


# Clear the terminal
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
        print(f'Invalid option: {option}. Please, write an valid option.\n')
    except ValueError:
      print('Invalid input. Please, write an valid number.\n')
    except Exception as e:
      print(f'An error ocurred: {e}. Please, try again.\n')

def main():
  manga = Manga()
  clear_screen()
  print('Welcome the manga recommendation. Here ')

  while True:
    print('1. recommend a random manga')
    print('2. recommend a random manga based on genre')
    print('3. search for an manga by name')
    print('4. view all mangas')
    print('0. for leave the program\n')
    
    option = user_main_menu()
    clear_screen()

    if option == 1:
      manga.random_manga()
    elif option == 2:
      manga.random_manga_based_by_genre()
    elif option == 3:
      manga.random_manga_search_by_name()
    elif option == 4:
      manga.view_all_manga()
    elif option == 0:
      print('Goodbye!')
      break


# Call the main program
if __name__ == '__main__':
  main()

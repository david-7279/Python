from time import sleep
import os, random, json, requests


# Clear the terminal
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  sleep(0.5)


def inverse_clear_screen():
  sleep(0.8)
  os.system('cls' if os.name == 'nt' else 'clear')


# Class Manga
class Manga:
  def __init__(self):
    self.manga_list = self.fetch_manga_list()
    self.save_manga_list_file()


  # Fetch api from Jikan
  def fetch_manga_list(self, max_pages = 200):
    manga_list = []
    page = 1
    while page <= max_pages:
      try:
        response = requests.get(f'https://api.jikan.moe/v4/manga?page={page}')
        response.raise_for_status()
        data = response.json()

        if not data['data']:
          break

        manga_list.extend(data['data'])
        page += 1

        sleep(0.2)
      except requests.RequestException as e:
        print(f'Error fetching manga data: {e}')
        break
    return manga_list
  

  def random_manga(self):
    try:
      if self.manga_list:
        random_manga = random.choice(self.manga_list)
        print('Random Manga')
        print(f'Name: {random_manga['title']} | {", ".join(genre["name"] for genre in random_manga["genres"])}')
        print(f'Chapters: {random_manga['chapters']}, {random_manga['status']}')
        print(f'\nSynopsise: {random_manga['synopsis']}\n')
      else:
        print('No mangas available.\n')
    except Exception as e:
      print(f'An error ocurred: {e}. Please, try again.\n')

  
  def random_manga_based_by_genre(self):
    while True:
      try:
        genres = set()

        for manga in self.manga_list:
          for genre in manga['genres']:
            genres.add(genre['name'])

        sorted_genre = sorted(genres)
        print('Avalilable genres')
        for index, genre in enumerate(sorted_genre, start=1):
          print(f'[{index}] {genre}')
        print('[0] Go back\n')

        manga_index = int(input('Choose an genre: '))
        if 1 <= manga_index <= len(sorted_genre):
          selected_genre = sorted_genre[manga_index - 1]
          print(f'Choosen genre: {selected_genre}\n')
        
        elif manga_index == 0:
          print('No genre selected')
          return
        else:
          print(f'Invalid genre: {selected_genre}.\n')
          inverse_clear_screen()
          continue

        filtered_manga = [
          manga for manga in self.manga_list
          if any(genre['name'] == selected_genre for genre in manga['genres'])
        ]
        inverse_clear_screen()
        print('Choosing an manga based in your selection..')
        sleep(1)
        inverse_clear_screen()
        if filtered_manga:
          random_manga = random.choice(filtered_manga)
          print(f'Filtered managa based on gere [{selected_genre}]')
          print(f'Name: {random_manga['title']} | {", ".join(genre["name"] for genre in random_manga["genres"])}')
          print(f'Chapters: {random_manga['chapters']}, {random_manga['status']}')
          print(f'\nSynopsise: {random_manga['synopsis']}\n')
          return
        else:
          print('No mangas found for the selected genre')
          inverse_clear_screen()
          return

      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.\n')

  def random_manga_search_by_name(self):
    while True:
      try:
        search = input('Search an manga by its name (Write "Exit" to leave): ').title()
        if search == "Exit":
          print('Exiting search.\n')
          inverse_clear_screen()
          return
        if not search:
          print('Invalid name. Please, try again.\n')
          inverse_clear_screen()
          continue

        found = False
        for manga in self.manga_list:
          if isinstance(manga, dict) and 'title' in manga:
            if search in manga['title']:
              print(f'Name: {manga['title']} | {", ".join(genre["name"] for genre in manga["genres"])}')
              print(f'Chapters: {manga['chapters']}, {manga['status']}')
              print(f'\nSynopsise: {manga['synopsis']}\n')
              found = True
              return
        if not found:
          print('No manga found \n')
          inverse_clear_screen()

      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.\n')


  def view_all_manga(self):
    try:
      print('All mangas in the list')
      sorted_manga = sorted(self.manga_list, key=lambda x: x['title'])
      for manga in sorted_manga:
        print(f'Name: {manga['title']} | {", ".join(genre['name'] for genre in manga['genres'])}')
        print(f'Chapters: {manga['chapters']}, {manga['status']}\n')
      print(f'\nNumber of mangas: {len(sorted_manga)}\n')

    except Exception as e:
      print(f'An error ocurred: {e}. Please, try again.\n')


  def save_manga_list_file(self, filename='Manga.json'):
    try:
      manga_list = []
      for manga in self.manga_list:
        manga_data = {
          "title": manga['title'],
          "genres": [genre['name'] for genre in manga['genres']],
          "chapters" : manga['chapters'],
          "satus": manga['status']
        }
        manga_list.append(manga_data)

      with open(filename, 'w') as file:
        json.dump(manga_list,  file, indent=4)
        
    except ValueError:
      print('Invalid number. Please, try again.\n')
    except Exception as e:
      print(f'An error ocurred: {e}. Please, try again.\n')
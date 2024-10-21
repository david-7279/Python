from time import sleep
import os, random, requests, json

# Clear terminal
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  sleep(0.5)

def inverse_clear_screen():
  sleep(1)
  os.system('cls' if os.name == 'nt' else 'clear')


class Anime:
  def __init__(self):
    self.anime_list = self.fetch_anime_list()
    self.save_anime_file()


  def fetch_anime_list(self, max_pages=5):
    anime_list = []
    page = 1
    while page <= max_pages:
      try:
        response = requests.get(f'https://api.jikan.moe/v4/anime?page={page}')
        response.raise_for_status()
        data = response.json()

        # If there are no more anime on this page, break the loop
        if not data['data']:
          break

        # Add the anime from this page to the overall list
        anime_list.extend(data['data'])
        page += 1  # Go to the next page

        # Delay to avoid hitting the rate limit
        sleep(0.2)

      except requests.RequestException as e:
        print(f'Error fetching anime data: {e}')
        break
    return anime_list


  def random_anime(self):
    try:
      if self.anime_list:
        random_anime = random.choice(self.anime_list)
        print('Random anime')
        print(f'Name: {random_anime["title"]}')
        print(f'Genres: {", ".join(genre["name"] for genre in random_anime["genres"])}')
        print(f'Type: {random_anime["type"]}\n')
      else:
        print('No animes found. Sorry!\n')
    except Exception as e:
      print(f'An error occurred: {e}. Please, try again.\n')

  
  def based_genre_anime(self):
    while True:
      try:
        # Show genres and selected one of them
        genres = set()
        for anime in self.anime_list:
          for genre in anime['genres']:
            genres.add(genre['name'])

        sorted_genres = sorted(genres)
        print('Available genres:')
        for index, genre in enumerate(sorted_genres, start=1):
          print(f'[{index}] {genre}')
        print('[0] Go back\n')

        anime_genre_index = int(input('Choose a genre: '))
        selected_genre = None
        if 1 <= anime_genre_index <= len(sorted_genres):
          selected_genre = sorted_genres[anime_genre_index - 1]
          print(f'Selected genre: {selected_genre}\n')
        elif anime_genre_index == 0:
          print('No genre selected.\n')  
          inverse_clear_screen()
          return
        else:
          print('Invalid genre selection\n')
          inverse_clear_screen()
          continue
        
        filtered_animes = [
          anime for anime in self.anime_list
          if any(genre['name']  == selected_genre for genre in anime['genres'])
        ]
        inverse_clear_screen()
        print('Choosing an anime based in your selection ...')
        sleep(1)
        inverse_clear_screen()
        if filtered_animes:
          random_anime = random.choice(filtered_animes)
          print('Filtered anime recommendation:')
          print(f'Name: {random_anime["title"]}')
          print(f'Genres: {", ".join(genre["name"] for genre in random_anime["genres"])}') 
          print(f'Type: {random_anime["type"]}\n')
          return
        else:
          print('No animes found for the selected genre\n')
          sleep(0.7)
          inverse_clear_screen()
          continue

      except ValueError:
        print('Invalid input. Please, try again.\n')
        inverse_clear_screen()
        return
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.\n')
        inverse_clear_screen()
        return
    

  def based_type_anime(self):
    while True:
      try:
        # Show types and selected one of them
        types = set(anime['type'] for anime in self.anime_list)
        sorted_types = sorted(types)
        print('Available genres:')
        for index, type_ in enumerate(sorted_types, start=1):
          print(f'[{index}] {type_}')
        print('[0] Go back\n')

        anime_type_index = int(input('Choose a type: '))
        selected_type = None
        if 1 <= anime_type_index <= len(sorted_types):
          selected_type = list(sorted_types)[anime_type_index - 1]
          print(f'Selected type: {selected_type}\n')
        elif anime_type_index == 0:
          print('No type selected.\n')  
          inverse_clear_screen()
          return
        else:
          print('Invalid type selection\n')
          inverse_clear_screen()
          continue
        
        filtered_animes = [
          anime for anime in self.anime_list
          if anime['type'] == selected_type
        ]
        inverse_clear_screen()
        print('Choosing an anime based in your selection ...')
        sleep(1)
        inverse_clear_screen()
        if filtered_animes:
          random_anime = random.choice(filtered_animes)
          print('Filtered anime recommendation:')
          print(f'Name: {random_anime["title"]}')
          print(f'Genres: {", ".join(genre["name"] for genre in random_anime["genres"])}') 
          print(f'Type: {random_anime["type"]}\n')
          return
        else:
          print('No animes found for the selected type\n')
          sleep(0.7)
          inverse_clear_screen()
          continue

      except ValueError:
        print('Invalid input. Please, try again.\n')
        inverse_clear_screen()
        return
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.\n')
        inverse_clear_screen()
        return
    
  
  def search_anime_by_name(self):
    while True:
      try:
        search = input('Search an anime by its name (Write "Exit" to leave): ').title()

        if search == 'Exit':
          print('Exiting search.\n')
          inverse_clear_screen()
          return
        if not search:
          print('Please, write a valid name.\n')
          continue

        found = False
        for anime in self.anime_list:
          if isinstance(anime, dict) and 'title' in anime:
            if search in anime['title']:
              print(f'Name: {anime["title"]}')
              print(f'Genres: {", ".join(genre["name"] for genre in anime["genres"])}') 
              print(f'Type: {anime["type"]}\n')
              found = True
              return
                
        if not found:
          print(f'{search} not found. Please, try again.\n')
          inverse_clear_screen()

      except ValueError:
        print('Invalid input. Please, try again.\n')
        inverse_clear_screen()
      except Exception as e:
        print(f'An error occurred: {e}. Please, try again.\n')
        inverse_clear_screen()


  def view_all_animes(self):
    try:
        print('All animes in the list:')
        sorted_anime = sorted(self.anime_list, key=lambda x: x['title'])
        for anime in sorted_anime:
            genres = ', '.join(genre['name'] for genre in anime['genres']) 
            print(f"Name: {anime['title']} ({genres}) - {anime['type']}")
        print(f'\nNumber of animes: {len(self.anime_list)}\n')

    except ValueError:
        print('Invalid input. Please, try again.\n')
        inverse_clear_screen()
    except Exception as e:
        print(f'An error occurred: {e}. Please, try again.\n')
        inverse_clear_screen()
        return
    
  
  def save_anime_file(self, filename='Anime.json'):
    try:
      anime_list = []
      for anime in self.anime_list:
        anime_data = {
          "title": anime['title'],
          "genres": [genre['name'] for genre in anime['genres']],
          "type": anime['type']
        }
        anime_list.append(anime_data)

      with open(filename, 'w') as file:
        json.dump(anime_list, file, indent=4)
    
    except ValueError:
        print('Invalid input. Please, try again.\n')
        inverse_clear_screen()
    except Exception as e:
        print(f'An error occurred: {e}. Please, try again.\n')
        inverse_clear_screen()
        return
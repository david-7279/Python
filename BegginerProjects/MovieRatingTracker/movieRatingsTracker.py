import os
from time import sleep

# Movie Array
movieList = [] 

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(1)


def userOption():
    choices = [1, 2, 3, 4, 5, 6, 7]
    while True:
      try:
          option = int(input('Choose an option: '))
          if option in choices:
            return option
          else:
            print(f'Invalid option {option}! Please, try again.')

      except ValueError:
        print(f'Invalid number {option}! Please, try again.')


def addMovieRating():
    index = len(movieList) + 1
    name = input('Name of the movie: ')
    genre = input('Genre of the movie: ')
    year = int(input('Year of the movie: '))
    director = input('Name of the director: ')
    rating = float(input('Rating the movie (1 to 5): '))
    if 0 < rating <= 5:
      movieDetails = [index, name, genre, year, director, rating]
      movieList.append(movieDetails)
      return True
    else:
      print(f'Invalid rating: {rating}')
      return False


def viewMovieRatings():
    if not movieList:
      print('No movies in the list!')
      return

    print('Movie list: ')
    for movie in movieList:
      print(f'[{movie[0]}] - {movie[1]}, Genre: {movie[2]}, Year: {movie[3]}, Director: {movie[4]}, Rating: {movie[5]}')


def updateMovie():
    if not movieList:
        print('No movies in the list!')
        return

    viewMovieRatings()
    
    try:
      movieToUpdate = int(input('Choose a movie index to update: '))

      if movieToUpdate <= 0 or movieToUpdate > len(movieList):
        print(f'Invalid movie index: {movieToUpdate}')
        return

      for movie in movieList:
        if movie[0] == movieToUpdate:
          print(f'Updating movie: [{movie[0]}] - {movie[1]}')

          newName = input(f'Old name: {movie[1]} (leave blank to keep current): ') or movie[1]
          newGenre = input(f'Old genre: {movie[2]} (leave blank to keep current): ') or movie[2]
          newYear = input(f'Old year: {movie[3]} (leave blank to keep current): ')
          newYear = int(newYear) if newYear else movie[3]
          newDirector = input(f'Old director: {movie[4]} (leave blank to keep current): ') or movie[4]
          newRating = input(f'Old rating: {movie[5]} (leave blank to keep current): ')
          newRating = float(newRating) if newRating else movie[5]

          if not 0 < newRating <= 5:
            print(f'Invalid rating: {newRating}')
            return

          movieList[movieList.index(movie)] = [movie[0], newName, newGenre, newYear, newDirector, newRating]
          clearScreen()
          print('Updating movie ...')
          sleep(1.5)
          print('Movie updated successfully!')
          return

    except ValueError:
      print('Invalid input! Please, try again.')


def deleteMovie():
    if not movieList:
      print('No movies in the list!')
      return

    viewMovieRatings()

    try:
      movieToDelete = int(input('Choose an movie index to delete: '))

      if movieToDelete <= 0 or movieToDelete > len(movieList):
        print(f'Invalid movie {movieToDelete}! Please, try again.')
        return

      
      movieList.pop(movieToDelete - 1)

      for i, movie in enumerate(movieList):
          movie[0] = i + 1
       
      clearScreen()
      print('Deleting movie ...')
      sleep(1.5)
      print(f'Movie deleted sucessfully!')
    
    except ValueError:
      print(f'Invalid option {movieToDelete}! Please, try again.')
    

def averageRating():
    if not movieList:
      print('No movies in the list!')
      return

    count = 0
    ratingSum = 0
    try:
      for movie in movieList:
        ratingSum += movie[5]
        count += 1
      average = ratingSum / count

      clearScreen()
      print('Calculating ...')
      sleep(1)
      print(f'Average movie rating: {average:.2f}')
       
    except ZeroDivisionError:
      print(f'Error: Division by zero occurred!')
    except ValueError as error:
      print(f'Error: {error}')


def lowestHighestRating():
    if not movieList:
      print('No movies in the list!')
      return

    highest = max(movieList, key=lambda x: x[4])
    lowest = min(movieList, key=lambda x: x[4])
    clearScreen()
    print('Calculating ...')
    sleep(1)
    print(f'Highest movie rating: {highest[0]} directed by {highest[3]} with rating {highest[4]}')
    print(f'Lowest movie rating: {lowest[0]} directed by {lowest[3]} with rating {lowest[4]}') 


def main():
    print('Welcome to Movie Ratings Tracker!\n')

    while True:
      print('')
      print('1. for add new movie and rating')
      print('2. for view all movies and their rating')
      print('3. for update movies and their rating')
      print('4. for delete movies')
      print('5. for calculate and display the average rating')
      print('6. for find the highest and lowest rating movies') 
      print('7. for existing the program\n') 

      option = userOption()
      clearScreen()
    
      if option == 1:
        addMovieRating()
        clearScreen()
      elif option == 2:
        viewMovieRatings()
      elif option == 3:
        updateMovie()
      elif option == 4:
        deleteMovie()
      elif option == 5:
        averageRating()
      elif option == 6:
        lowestHighestRating()
      elif option == 7:
        print('Goodbye!')
        break
      else:
        print(f'Invalid option {option}! Please, try again.')


if __name__ == "__main__":
    main()
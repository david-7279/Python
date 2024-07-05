import os
from time import sleep

# Movie Array
movieList = [] 

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(1)


def userOption():
    choices = [1, 2, 3, 4, 5]
    try:
      while True:
        option = int(input('Choose an option: '))
        while option not in choices:
          print(f'Invalid option {option}! Please, try again.')
        return option
    except ValueError:
      print(f'Invalid number {option}! Please, try again.')
      return userOption()


def addMovieRating():
    name = input('Name of the movie: ')
    genre = input('Genre of the movie: ')
    year = int(input('Year of the movie: '))
    director = input('Name of the director: ')
    rating = float(input('Rating the movie (1 to 5): '))
    if 0 < rating <= 5:
      movieDetails = [name, genre, year, director, rating]
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
      print(f' - {movie[0]}, Genre: {movie[1]}, Year: {movie[2]}, Director: {movie[3]}, Rating: {movie[4]}')


def averageRating():
    if not movieList:
      print('No movies in the list!')
      return

    count = 0
    ratingSum = 0
    try:
      for movie in movieList:
        ratingSum += movie[4]
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
      print('3. for calculate and display the average rating')
      print('4. for find the highest and lowest rating movies') 
      print('5. for existing the program\n') 

      option = userOption()
      clearScreen()
    
      if option == 1:
        addMovieRating()
        clearScreen()
      elif option == 2:
        viewMovieRatings()
      elif option == 3:
        averageRating()
      elif option == 4:
        lowestHighestRating()
      elif option == 5:
        print('Goodbye!')
        break
      else:
        print(f'Invalid option {option}! Please, try again.')


if __name__ == "__main__":
    main()
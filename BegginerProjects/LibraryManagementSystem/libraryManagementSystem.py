class Book:
    def __init__ (self, ID, title, author, publicationYear, genre):
      self.ID = ID
      self.title = title
      self.author = author
      self.publicationYear = publicationYear
      self.genre = genre
    
    def show(self):
      print(f'[{self.ID}] {self.title} by {self.author} publish in {self.publicationYear} ({self.genre})')


class Library:
    def __init__(self, books=None):
      self.books = books if books is not None else []

     # Function addBook
    def addBook(self, book):
      self.books.append(book)

     # Function removeBook
    def removeBook(self, book):
      if not self.books:
        print('Books list is empty!')
        return

      try:
        self.books.remove(book)
        print(f'[{book.ID}] {book.title} by {book.author} removed sucessfully.')
      except ValueError:
        print(f'Book not found! Please, try again.')

    # Function updateBook by index
    def updateBook(self, bookID):
      if not self.books:
        print('Books list is empty!')
        return

      for book in self.books:
        if book.ID == bookID:
          print('Enter the values for the book (leave blank to keep current)')

          newTitle = input(f'title [{book.title}]: ') or book.title
          newAuthor = input(f'Author [{book.author}]: ') or book.author
          newPublicationYear = input(f'Publication Year [{book.publicationYear}]: ') or book.publicationYear
          newGenre = input(f'Genre [{book.genre}]: ') or book.genre

          # Update book atributes
          book.title = newTitle
          book.author = newAuthor
          book.publicationYear = newPublicationYear
          book.genre = newGenre

          print('Book updated sucessfully!\n')
          book.show()
          return

      print(f'Book with ID {bookID} not found! Please, try again.')

    # Function searchBook by index, author or title
    def searchBook(self, searchBook):
      if not self.books:
        print('Books list is empty!')
        return

      found = False
      for book in self.books:
        if (searchBook == book.ID) or (searchBook == book.author) or (searchBook == book.title):
          book.show()
          found = True
      if not found:
        print(f'Invalid books found matching {searchBook}! Please, try again.')


# Create Books
book1 = Book("1", "Norwegian Wood", "Haruki Murakami", "1987", "Romance")
book2 = Book("2", "Stand", "Stephen King", "1978", "Horror/Fantasy")

# Create Library's
library = Library()

# Add books to library
library.addBook(book1)
library.addBook(book2)

# Show books
print('Books in the library:')
book1.show()
book2.show()

# Search for a book
print('\nSearching for a book by title:')
library.searchBook('Norwegian Wood')

# Update a book
print('\nUpdating a book:')
library.updateBook("1")

# Remove a book
print('\nRemoving a book:')
library.removeBook(book2)
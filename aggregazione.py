class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_book(self):
        return [f"{book.title} di {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("Mondadori")

book1 = Book("Harry Potter", "autore1")
book2 = Book("libro 2", "autore2")

library.add_book(book1)
library.add_book(book2)

print(library.name)
print(library.list_book())
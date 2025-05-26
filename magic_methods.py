class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} di {self.author}"
    
    def __eq__(self, other): #per vedere se due libri sono uguali
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other): #less then
        return self.num_pages < other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        else:
            return f"Key {key} non è stata trovata"

book1 = Book("Libro1", "autore1", 300)
book2 = Book("Libro2", "autore2", 400)

print(book2) # __str__

print(book1 == book2) # __eq__

print(book1 < book2) # __lt__

print(book1 + book2) # __add__

print("Rowling" in book1) # __contains__

print(book1['title']) # __getitem__
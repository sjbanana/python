class Dati:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

class Libro(Dati):
    def __init__(self, titolo, autore, data_pubblicazione):
        super().__init__(titolo, autore)
        self.data_pubblicazione = data_pubblicazione

class Rivista(Dati):
    def __init__(self, titolo, autore, data_uscita):
        super().__init__(titolo, autore)
        self.data_uscita = data_uscita

class Libreria:
    def __init__(self, nome):
        self.nome = nome
        self.libri = []
        self.riviste = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)

    def aggiungi_rivista(self, rivista):
        self.riviste.append(rivista)

    def lista_libro(self):
        return [
            f"Titolo: {libro.titolo}, Autore: {libro.autore}, Pubblicazione: {libro.data_pubblicazione}"
            for libro in self.libri
        ]

    def lista_rivista(self):
        return [
            f"Titolo: {rivista.titolo}, Autore: {rivista.autore}, Uscita: {rivista.data_uscita}"
            for rivista in self.riviste
        ]

# Esempio d'uso
libreria = Libreria("Mondadori")

libro1 = Libro("Harry Potter", "J.K. Rowling", "1997")
libro2 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", "1954")

rivista1 = Rivista("National Geographic", "Autore 1", "Gennaio 2024")
rivista2 = Rivista("Scientific American", "Autore 2", "Febbraio 2024")

libreria.aggiungi_libro(libro1)
libreria.aggiungi_libro(libro2)
libreria.aggiungi_rivista(rivista1)
libreria.aggiungi_rivista(rivista2)

print(f"Libreria: {libreria.nome}")

print(libreria.lista_libro())
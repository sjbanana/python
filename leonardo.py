class Libreria:
    def __init__(self, nome):
        self.nome = nome
        self.libro = []
        self.rivista = []

    def aggiungi_libro(self, libro):
        self.libro.append(libro)

    def aggiungi_rivista(self, rivista):
        self.rivista.append(rivista)

    def lista_libro(self):
        return [f"Questo libro è stato pubblicato: {libro.data_pubblicazione}. E' stato scritto da {libro.autore}" for libro in self.libro]
    
    def lista_rivista(self):
        return [f"Questa rivista è stata scritta da:{rivista.argomento}, è stata pubblicata il: {rivista.data_uscita}" for rivista in self.rivista]

class Libro:
    def __init__(self, data_pubblicazione, autore):
        self.data_pubblicazione = data_pubblicazione
        self.autore = autore

class Rivista:
    def __init__(self, argomento, data_uscita):
        self.argomento = argomento
        self.data_uscita = data_uscita

libreria = Libreria("Mondadori")

libro1 = Libro("Harry Potter", "autore1")
libro2 = Libro("libro 2", "autore 2")

rivista1 = Rivista("rivista 1", "autore 1")
rivista2 = Rivista("Rivista2", "autore 2")

libreria.aggiungi_libro(libro1)
libreria.aggiungi_libro(libro2)
libreria.aggiungi_rivista(rivista1)
libreria.aggiungi_rivista(rivista2)

print(libreria.nome)
print(libreria.lista_libro())

print(libreria.lista_rivista())
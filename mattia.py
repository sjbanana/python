# Classe che gestisce i dati personali tramite dizionario
class DatiPersonali:
    def __init__(self, dati):
        self.dati = dati

    def mostra_dati(self):
        print(f"Nome: {self.dati['nome']}, Età: {self.dati['età']}, Città: {self.dati['città']}")

# Classe che gestisce le informazioni lavorative
class Lavoratore:
    def __init__(self, lavoro):
        self.lavoro = lavoro

    def lavora(self):
        print(f"Lavoro come {self.lavoro}.")

# Classe che eredita da entrambe le classi base (multieredità)
class Impiegato(DatiPersonali, Lavoratore):
    def __init__(self, dati, lavoro):
        DatiPersonali.__init__(self, dati)
        Lavoratore.__init__(self, lavoro)

# --- Uso del programma ---

# Dizionario con i dati
dati = {
    "nome": "Luca",
    "età": 30,
    "città": "Roma"
}

# Creazione dell'oggetto Impiegato
imp = Impiegato(dati, "Programmatore")

# Chiamata dei metodi
imp.mostra_dati()

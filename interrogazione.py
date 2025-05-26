lista = ["Pippo", "Pluto", "Paperino"]
dizionario = {"Pippo" : "presente", "Paperino" : "presente"}

for nome in lista:
    if nome in dizionario:
        print(f"{nome} è nel dizionario")
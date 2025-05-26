nome = input("Inserisci il tuo nome: ")
età = int(input("Inserisci la tua età: "))
età = età +  1

print(f"Ciao {nome}")
print(f"Hai {età} anni")

#gioco nomi
aggettivo1 = input("Inserisci un aggettivo: ")
nome = input("Inserisci un nome: ")
aggettivo2 = input("Inserisci un altro oggettivo: ")
verbo = input("Inserisci un verbo: ")
print(f"Oggi sono andato a {aggettivo1} zoo")
print(f"Ho visto {nome}")
print(f"{nome} era {aggettivo2} e {verbo}")

#calcolo area rettangolo
length = float(input("Inserisci la lunghezza del rettangolo: "))
width = float(input("Interisci la larghezza del rettangolo: "))
heigth = float(input("Interisci l'altezza del rettangolo: "))

area = length * width
volume = length * width * heigth

print(f"L'area è: {area} cm^2")
print(f"Il volume è: {volume}cm^3")

#carrello 
item = input("Quali prodotti vuoi comprare?: ")
price = float(input("Qual è il prezzo?: "))
quantity = int(input("Quanti prodotti vuoi comprare?: "))

total = price * quantity

print(f"Hai speso: {total}")
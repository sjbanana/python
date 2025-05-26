def lettere_alfabeto(parola):
    alfabeto = "abcdefghilmnopqrstvuwxyzABCDEFGHILMNOPQRSTVUWXYZ"
    for lettera in parola:
        if lettera in alfabeto:
            return True
    return False

# Esempio di uso
parola = "1234"

if lettere_alfabeto(parola):
    print("Ci sono le lettere dell'alfabeto")
else:
    print("Non ci sono lettere dell'alfabeto")
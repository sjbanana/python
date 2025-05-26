#1.palindrome
#2.se contiene delle vocali
#3.se contiene delle lettere dell'alfabeto


def ci_sono_vocali(parola):
    vocali = "aeiouAEIOU"
    for lettere in parola:
        if lettere in vocali:
            return True
        return False

parola="ciao"    

if ci_sono_vocali(parola):
    print("ci sono le vocali")

def lettere_alfabeto(parola):
    alfabeto = "abcdefghilmnopqrstvuwxyzABCDEFGHILMNOPQRSTVUWXYZ"
    for lettere in parola:
        if lettere in alfabeto:
            return True
        return False
    
parola= "1234skibidi"

if lettere_alfabeto(parola):
    print("Ci sono le lettere dell'alfabeto")
else:
    print("Non ci sono lettere dell'alfabeto")
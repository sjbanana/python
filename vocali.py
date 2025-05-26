def ci_sono_vocali(parola):
    vocali = "aeiouAEIOU"
    for lettera in parola:
        if lettera in vocali:
            return True
    return False

# Esempio di uso
parola = "ciao"

if ci_sono_vocali(parola):
    print("Ci sono le vocali")
else:
    print("Non ci sono vocali")

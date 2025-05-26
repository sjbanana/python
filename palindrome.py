def is_palindrome(parola):
    return parola == parola[::-1]

# Esempio di uso
parola = "anna"
parola_invertita = parola[::-1]

print(f"Parola: {parola}")
print(f"Parola al contrario: {parola_invertita}")

if is_palindrome(parola):
    print(f'"{parola}" è una parola palindroma')
else:
    print(f'"{parola}" non è una parola palindroma')

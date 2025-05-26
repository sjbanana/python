#expression for value in iterable if condition

doubles= [x*2 for x in range(1,11)]
squares= [z*z for z in range(1,11)]
print(doubles) #[2, 4, 6, 8, 10, 12, ..]
print(squares) #[1, 4, 9, 16, ...]

fruits =["mela", "banana", "cocco"]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars) #['m', 'b', 'c']

numeri = [1, -2, 3, -4, 5, -6]
num_positivi = [num for num in numeri if num>=0]
num_negativi = [num for num in numeri if num<0]
num_pari = [num for num in numeri if num % 2==0]
num_dispari = [num for num in numeri if num % 2==1]

print(num_pari)
#liste = [] duplicati ok, ordinate
#liste = {} duplicati no, non ordinate
#tuple = () duplicati ok, ordinate, più veloce

#liste
fruits = ["mela", "banana", "pesca"]

print(fruits[0:2])
print(fruits[0::2])
print(fruits[::-1])

for frutta in fruits:
    print(frutta)

print("mela" in fruits)

fruits.append("ananas") #per aggiungere un elemento
fruits.remove("mela") #per togliere un elemento
fruits.insert(0, "ananas")#fa in modo che la lista inizi con ananas
fruits.reverse()#dal ultimo al primo
fruits.clear()

#set
frutte = {"mela", "banana", "pesca"}
frutte.pop()#toglie un elemento randomico

#tuple
fruttE = ("mela", "banana", "pesca")
fruttE.index("mela") #0
print(fruttE.count("mela"))

for fruit in fruttE:
    print(fruit)
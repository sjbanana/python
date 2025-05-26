class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("bau")

class Cat(Animal):
    def speak(self):
        print("miao")

class Car():
    alive = False
    def speak(self):
        print("boh")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
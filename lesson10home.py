# Задание 1
class Animal:
    def make_sound(self):
        print("Общий звук животного")

class Dog(Animal):
    def make_sound(self):
        print("Собака: лает")
class Cat(Animal):
    def make_sound(self):
        print("Кошка: мяукает")
class Cow(Animal):
    def make_sound(self):
        print("Корова: мычит")

animal = Animal()
dog = Dog()
cat = Cat()
cow = Cow()
animal.make_sound()
dog.make_sound()
cat.make_sound()
cow.make_sound()

# Задание 4
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print('Бренд:', self.brand)
        print('Год:', self.year)
car = Vehicle('BYD', 2023)
car.display_info()


class Car(Vehicle):
    def display_info(self):
        print('Бренд:', self.brand)
        print('Год:', self.year)
car1 = Car('Chevrolet', 2020)
car1.display_info()


class Motorcycle(Vehicle):
    def display_info(self):
        print('Бренд:', self.brand)
        print('Год:', self.year)
moto = Motorcycle('Yamaha', 2024)
moto.display_info()
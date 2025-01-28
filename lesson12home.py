# lesson 2
# Пишем команду для ввода
number1 = int(input('Введите первое число: '))
mat_oper = input('Выберите действие (+ - * /): ')
number2 = int(input('Введите второе число: '))
# Пишем команду если, а если
if mat_oper == '+':
    print(number1+number2)
elif mat_oper == '-':
    print(number1-number2)
elif mat_oper == '*':
    print(number1*number2)
elif mat_oper == '/':
    print(number1/number2)
else:
    print('Такое действие отсутстует')


# lesson 3
names = ['ivan', 'pavel', 'jordan', 5, 6]
name = input('Введите имя: ')
# Для добавления значения в конец списка
names.append(name)
# Для удаления из списка выбранное значение
names.remove(name)
# Для удаления последнего элемента или по индексу
names.pop(1)
# Для добавления нескольких значений
names.extend()
# Для добавления значения в определенное место по индексу
names.insert()
print(names)


# lesson 4
# Цикл for пробегается по каждому значению элемента помещает каждую из них в переменную, а затем мы можемпроизвести различные действия над ними
names = ['ivan', 'pavel', 'jordan', 5]
for i in range(1, 100):
    if 'pavel' in names:
        print('pavel есть в списке')
    else:
        print('не понимаю о ком вы')
# Цикл While Пока это правда - делай, а если нет - остановись)
spam = 'hello'
while spam == 'hello':
    print(spam)


# lesson 5
# List comprehension
# [новая_переменная for новая_переменная in набор_значений ]
nums = [1, 2, 3, 4]
numbers2 = [i*2 for i in nums ]
print(numbers2)
# Условные операторы в List comprehension
number = int(input('Введите число, я определю на четность и нечетность: '))
# Для четных чисел
if (number % 2 == 0):
    print('Это четное число')
# Для нечетных чисел
elif (number % 2 != 0):
    print('Это нечетное число')
else:
    print('Ошибка при вводе')


# lesson 6
# Словари {}
instructor = {'name': 'Jordan', 'age': 21, 'job': 'programmer'}
# .values() - выдаст все значения всех ключей
print(instructor.values()) #['Jordan', 21, 'programmer']
# .keys() - выдаст все ключи словаря
print(instructor.keys()) #['name', 'age', 'job']
# .items() - выдаст оба (ключи, значения) словаря

# Методы удаления
my_dict = {'song': 'Godzilla', 'singer': 'Eminem'}
# .clear() - удаляет все из словаря и оставляет его пустым
my_dict.clear()
print(my_dict) # {}
# .pop('ключ') - удаляет пару из словаря по переданному ключу
my_dict.pop('song')
print(my_dict) # {'singer': 'Eminem'}
# .popitem() - удаляет последнюю пару (ключ: значение)
my_dict.popitem()
print(my_dict) # {'song': 'Godzilla'}

# Методы словарей
#{}.fromkeys('a', 1) - создает словарь (ключ, значение)
print({}.fromkeys('song', 'Godzilla'))
#.get('ключ') - выдает значение переданного ключа
my2 = {'title': 'Python for beginners'}
print(my2.get('title'))
# 'Python for beginners'


# lesson 7
def название_функции():
# Код для этой функции
# вызов функции
название_функции()
# Парсинг сайтов
import requests
url = 'http://example.com/post'
data = {'name': 'John', 'age': 30}
response = requests.post(url, data=data)
print(response.text)

import requests
link = 'https://icanhazip.com/'
print(requests.get(link).text)
Выход:
Выйдет ваш IP-адрес


# lesson 8
# Создание функции в одну строку
x = lambda a: a**2
print(x(4))

#*args - задавать любое количество аргументов
def spammer(*args):
for a in args:
print(a)
spammer(1, 2, 3, 1, 2, 3, '4', 'Hello') # 1, 2, 3, 1, 2, 3, '4', 'Hello'

#**kwargs - задавать любое количество аргументов(ключ: значение)
def spam1(**kwargs):
return kwargs
print(spam1(name= 'my1', age= 23)) # {'name': 'my1', 'age':23}


# lesson 9
# Классы
class Car:
type = 'Bugatti'
color = 'white'
max_speed = 300
# Определение классов
class User:
    def __init__(self, name, mail, age, number):
        self.name = name
        self.mail = mail
        self.age = age
        self.number = number

    def change_name(self, new_name):
        self.name = new_name

    def change_mail(self, new_mail):
        self.mail(self, new_mail)

    def change_number(self, new_number):
        self.number(self, new_number)


# lesson 10
class Animal:
    def make_sound(self, s):
        print(s)
class Horse(Animal):
    pass
# Объявление метода
class MyClass:
@classmethod
def class_info(cls):
return f"This is the {cls.__name__} class."
print(MyClass.class_info())


# lesson 11
# Задание 1
class Student:
    def __init__(self, name, age, group_number):
        self.name = name
        self.age = age
        self.group_number = group_number

    def get_name(self, new_name):
        self.name = new_name

    def get_age(self, new_age):
        self.age = new_age

    def get_group_number(self, new_group_number):
        self.group_number(self, new_group_number)

    def set_name_age(self, new_name_age):
        self.name_age = new_name_age

    def set_group_number(self, new_group_number):
        self.group_number(self, new_group_number)
pupil = Student('Ivan', 18, '10A')

# # Задание 2
# class Math:
#     def __init__(self, a, b):
#         self.a, self.b = a, b
#     def addition(self):
#         print(self.a + self.b)
#     def multiplication(self):
#         print(self.a * self.b)
#     def division(self):
#         print(self.a / self.b)
#     def subtraction(self):
#         print(self.a - self.b)

# # Задание 3
# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
#     def start(self):
#         return 'Автомобиль заведен'
#     def stop(self):
#         return 'Автомобиль заглушен'
#
#     def change_color(self, new_color):
#         self.color = new_color
#
#     def change_year(self, new_year):
#         self.year = new_year
#
#     def change_model(self, new_model):
#         self.model = new_model
#
#
# BYD = Car('Chazor', 'Black', 2023)
# # BYD.change_color('Gray')
# print(BYD.color)
# # BYD.change_year(2024)
# print(BYD.year)
# # BYD.change_model('Song Plus')
# print(BYD.model)




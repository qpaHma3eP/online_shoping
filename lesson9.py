# from http.client import responses
#
# import  requests
#
# url = 'https://openweathermap.org/data/2.5/weather'
# params = {'q':'Лондон', 'appid': ''}
# city = input('Введите город, в котором вы хотите посмотреть погоду: ')
# params['q'] = city
# response = requests.get(url, params=params).json()
# print(f'Город: {city}\n'
#       f'Погода: {response['weather'][0]['description']}\n'
#       f'Температура: +{response['main']['temp']}C, по ощущениям +{response['main']}


# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
#     def stop(self):
#         print('Машина остановилась')
#     def change_color(self, new_color):
#         self.color = new_color
#
# BYD = Car('Chazor', 'Black', 2023)
# BYD.change_color('Gray')
# print(BYD.color)



# class BankAccount:
#     def init(self, name, balance=0):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def cash(self, amount):
#         self.balance -= amount
#
#     def my_balance(self):
#         return self.balance


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










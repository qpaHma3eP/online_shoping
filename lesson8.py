# x = lambda a: a**2
# print(x(4))


def spam2(a, b):
    print(a+b)
spam2(3, 5)


# def spammer(*args):
#     for a in args:
#         print(a)
#         spammer(1,2,3,4,5, 'hello')


# def spam1(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)


# clients = {}
# opened_rooms = [i for i in range(1,21)]
# closed_rooms = []
#
# def add_client(name, room):
#     clients[name] = room
#     opened_rooms.remove(room)
#     closed_rooms.append(room)
#
# def del_client(name):
#         opened_rooms.append(clients[name])
#         closed_rooms.remove(clients[name])
#         clients.pop(name)
#
# def show_rooms():
#     return closed_rooms
#
# while True:
#     choise = input('Что хотите сделать? ')
#     if choise.lower() == 'Добавить':
#         client_name = input('Введите имя клиента: ')
#         print(opened_rooms)
#         client_rooms = int(input('Выберите номер для клиента: '))
#         if client_rooms in opened_rooms:
#             add_client(client_name, client_rooms)
#             print('Успешно добавлено!')
#         else:
#             print('Похоже, что номер занят или ошибка в данных!')
#     elif choise.lower() == 'Удалить':
#         client_name = input('Введите имя для удаления: ')
#         if client_name in clients:
#             del_client(client_name)
#             print('Успешно удалено!')
#         else:
#             print('Похоже что такого клиента в базе нет!')
#     elif choise.lower() == 'Номера':
#         print(show_rooms())
#     else:
#         print('Неизвестная операция!')




# students = {}
# opened_klass = [i for i in range(1, 12)]
# closed_klass = []
#
#
# def add_student(name, klass):
#     students[name] = klass
#     opened_klass.remove(klass)
#     closed_klass.insert(klass - 1, klass)
#
#
# def del_student(name):
#     opened_klass.insert(students[name] - 1, students[name])
#     closed_klass.remove(students[name])
#     students.pop(name)
#
#
# def show_klass():
#     return closed_klass
#
#
# while True:
#     choice = input('Что хотите сделать? ')
#     if choice.lower() == 'Добавить':
#         student_name = input('Введите имя ученика: ')
#         print(opened_klass)
#         student_klass = int(input('Выберите класс для ученика: '))
#         if student_klass in opened_klass:
#             add_student(student_name, student_klass)
#             print('Успешно добавлено!')
#         else:
#             print('Похоже, что ошибка в данных!')
#     elif choice.lower() == 'Удалить':
#         student_name = input('Введите имя для удаления: ')
#         if student_name in students:
#             del_student(student_name)
#             print('Успешно удалено!')
#         else:
#             print('Похоже, что такого ученика в базе нет!')
#     elif choice.lower() == 'Классы':
#         print(show_klass())
#     else:
#         print('Неизвестная операция!')







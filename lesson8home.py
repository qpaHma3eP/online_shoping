x = lambda a, b: a+b
print(x(7, 8))

def spam2(a, b):
    print(a+b)
spam2(3, 5)



# students = {}
# opened_klass = [i for i in range(1, 12)]
# closed_klass = []
#
# def add_student(name, klass):
#     students[name] = klass
#     opened_klass.remove(klass)
#     closed_klass.insert(klass - 1, klass)
#
# def del_student(name):
#     opened_klass.insert(students[name] - 1, students[name])
#     closed_klass.remove(students[name])
#     students.pop(name)
#
# def show_klass():
#     return closed_klass
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
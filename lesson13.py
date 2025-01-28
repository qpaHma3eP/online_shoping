import sqlite3
from pickle import STRING

from django.contrib.auth import user_logged_out

# Подключение к базе данных
connection = sqlite3.connect('my_students.db')
# Python + SQL
sql = connection.cursor()

# Создание таблицы
sql.execute('CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARYKEY AUTO_INCREMENT, name TEXT, age INTEGER, grade INTEGER);')
# Добавление данных в БД
def add_students():
    sql.execute('INSERT INTO students VALUES (0, "kamran", 13, 3);')
    connection.commit()

def get_students_by_name():
    a = sql.execute('SELECT * FROM students WHERE name="kamran";').fetchone()
    print(a)


def update_students_grade():
    student_id = input('Введите айди ученика: ')
    student_grade = input('Введите оценку ученика: ')
    b = sql.execute('UPDATE students SET grade=? WHERE id=?;', (student_grade, student_id))
    connection.commit()

def delete_student():
    stundent_id = input('Введите id ученика которого хотите удалить: ')
    c = sql.execute('DELETE FROM students WHERE id=?;', (stundent_id))
    connection.commit()

add_students()
# get_students_by_name()
# update_students_grade()
# delete_student()
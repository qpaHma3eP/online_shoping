import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# Создание таблицы students
c.execute('''CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT)''')

# Вставка записей в таблицу
students_data = [
    ('Дильшод', 26, 'A'),
    ('Марина', 25, 'B'),
    ('Шухрат', 25, 'C'),
    ('Шохсанам', 25, 'A')
]

c.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", students_data)
conn.commit()



def get_student_by_name(name):
    c.execute("SELECT name, age, grade FROM students WHERE name=?", (name,))
    return c.fetchone()

# Пример использования функции
student = get_student_by_name('Марина')
print(student)



def update_student_grade(name, new_grade):
    c.execute("UPDATE students SET grade=? WHERE name=?", (new_grade, name))
    conn.commit()

# Пример использования функции
update_student_grade('Шухрат', 'B')



def delete_student(name):
    c.execute("DELETE FROM students WHERE name=?", (name,))
    conn.commit()

# Пример использования функции
delete_student('Шохсанам')



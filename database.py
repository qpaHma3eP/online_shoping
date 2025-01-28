import sqlite3


# Подключение к базе данных
connection = sqlite3.connect('delivery.db', check_same_thread=False)
# Python + SQL
sql = connection.cursor()


# Создаем таблицу пользователей
sql.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, number TEXT UNIQUE);')
# Создаем таблицу продуктов
sql.execute('CREATE TABLE IF NOT EXISTS products (pr_id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'pr_name TEXT, pr_des TEXT, pr_price REAL, pr_count INTEGER, pr_photo TEXT);')
# Создаем таблицу корзины
sql.execute('CREATE TABLE IF NOT EXISTS cart(user_id INTEGER, user_product TEXT, pr_amount INTEGER);')


## Методы для пользователя ##
# Регистрация
def register(tg_id, name, num):
    sql.execute('INSERT INTO users VALUES (?, ?, ?);', (tg_id, name, num))
    # Фиксируем изменения
    connection.commit()


# Проверка user'а на наличие в БД
def check_user(tg_id):
    if sql.execute('SELECT * FROM users WHERE id=?;', (tg_id,)).fetchone():
        return True
    else:
        return False


## Методы для продуктов. Клиентская сторона ##
# Вывод всех товаров
def get_all_pr():
    return sql.execute('SELECT * FROM products;').fetchall()


# Вывод товаров для кнопок
def get_pr_buttons():
    all_products = sql.execute('SELECT pr_id, pr_name, pr_count FROM products;').fetchall()
    in_stock = [n for n in all_products if n[2] > 0]
    return in_stock


# Вывод конкретного товара
def get_exact_pr(pr_id):
    return sql.execute('SELECT * FROM products WHERE pr_id=?;', (pr_id,)).fetchone()


# Вывод цены конкретного товара
def get_exact_price(pr_name):
    return sql.execute('SELECT pr_price FROM products WHERE pr_name=?;', (pr_name,)).fetchone()


## Методы для корзины ##
# Добавление в корзину
def add_to_cart(user_id, user_product, product_amount):
    sql.execute('INSERT INTO cart VALUES (?, ?, ?);', (user_id, user_product, product_amount))
    # Фиксируем изменения
    connection.commit()


# Очистка корзины
def clear_cart(user_id):
    sql.execute('DELETE FROM cart WHERE user_id=?;', (user_id,))
    #Фиксируем изменения
    connection.commit()


# Вывод корзины
def show_cart(user_id):
    return sql.execute('SELECT * FROM cart WHERE user_id=?;', (user_id,)).fetchall()


# Оформление заказа
def make_order(user_id):
    # Достаем названия товаров и их кол-во с КОРЗИНЫ
    product_names = sql.execute('SELECT user_product FROM cart WHERE user_id=?;', (user_id,)).fetchall()
    product_counts = sql.execute('SELECT pr_amount FROM cart WHERE user_id=?;', (user_id,)).fetchall()

    # Достаем кол-во продуктов со СКЛАДА
    stock_quantity = [sql.execute('SELECT pr_count FROM products WHERE pr_name=?;', (i[0],)).fetchone()[0]
                      for i in product_names]
    totals = []

    # e - сколько взял пользователь
    for e in product_counts:
        # с - количество со СКЛАДА
        for c in stock_quantity:
            totals.append(c - e[0])


    # t - измененное количество товара
    for t in totals:
        # n - названия товаров
        for n in product_names:
            sql.execute('UPDATE products SET pr_count=? WHERE pr_name=?;', (t, n[0]))

    # Фиксируем изменения
    connection.commit()
    return stock_quantity, totals


## Администраторская сторона ##
# Добавления товара в БД
def pr_to_db(pr_name, pr_des, pr_price, pr_count, pr_photo):
    if (pr_name,) in sql.execute('SELECT pr_name FROM products;').fetchall():
        return False
    else:
        sql.execute('INSERT INTO products (pr_name, pr_des, pr_price, pr_count, pr_photo) '
                    'VALUES (?,?,?,?,?);', (pr_name, pr_des, pr_price, pr_count, pr_photo))
        # Фиксируем изменения
        connection.commit()


# Удаление товара из БД
def del_product(pr_name):
    sql.execute('DELETE FROM products WHERE pr_name=?;', (pr_name,))
    # Фиксируем изменения
    connection.commit()


# Изменение атрибута товара
def change_attr(keyword, new_value, attr=''):
    if attr == 'name':
        sql.execute('UPDATE products SET pr_name=? WHERE pr_name=?;', (new_value, keyword))
    elif attr == 'des':
        sql.execute('UPDATE products SET pr_des=? WHERE pr_name=?;', (new_value, keyword))
    elif attr == 'price':
        sql.execute('UPDATE products SET pr_price=? WHERE pr_name=?;', (new_value, keyword))
    elif attr == 'count':
        sql.execute('UPDATE products SET pr_count=? WHERE pr_name=?;', (new_value, keyword))
    elif attr == 'photo':
        sql.execute('UPDATE products SET pr_photo=? WHERE pr_name=?;', (new_value, keyword))

    # Фиксируем изменения
    connection.commit()


# Проверка на наличие товаров в БД
def check_pr():
    if sql.execute('SELECT * FROM products;').fetchall():
        return True
    else:
        return False

from telebot import types


# кнопка для отправки номера
def num_button():
    # Создаём пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаём сами кнопки
    num = types.KeyboardButton('Отправить номер 📞', request_contact=True)
    # Добавляем кнопки в пространство
    kb.add(num)

    return kb

# Кнопка главного меню
def main_menu(products):
    # Создаем Пространство
    kb = types.InlineKeyboardMarkup(row_width=2)
    # Создаем сами кнопки
    cart = types.InlineKeyboardButton(text='Корзина 🛒', callback_data='cart')
    all_products = [types.InlineKeyboardButton(text=f'{i[1]}', callback_data=i[0]) for i in products]
    # Добавляем кнопки в пространство
    kb.add(*all_products)
    kb.row(cart)

    return kb


# Кнопки выбора количества товара
def choose_amount(pr_amount, plus_or_minus='', amount=1):
    #
    kb = types.InlineKeyboardMarkup(row_width=3)
    # Создаем сами кнопки
    minus = types.InlineKeyboardButton(text='-', callback_data='decrement')
    count = types.InlineKeyboardButton(text=str(amount), callback_data=str(amount))
    plus = types.InlineKeyboardButton(text='+', callback_data='increment')
    to_cart = types.InlineKeyboardButton(text='В корзину 🛒', callback_data='to_cart')
    back = types.InlineKeyboardButton(text='Назад 🔙', callback_data='back')
    # Алгоритм изменения количества
    if plus_or_minus == 'increment':
        if amount <= pr_amount:
            count = types.InlineKeyboardButton(text=str(amount + 1), callback_data=str(amount + 1))
    elif plus_or_minus == 'decrement':
        if amount >= 1:
            count = types.InlineKeyboardButton(text=str(amount - 1), callback_data=str(amount - 1))
    # Добавляем кнопки в пространство
    kb.add(minus, count, plus)
    kb.row(back, to_cart)

    return kb

# Кнопки корзины
def cart_buttons():
    # Создаем сами кнопки
    kb = types.InlineKeyboardMarkup(row_width=2)
    order = types.InlineKeyboardButton(text='Оформить заказ', callback_data='order')
    clear = types.InlineKeyboardButton(text='Очистить корзину', callback_data='clear')
    back = types.InlineKeyboardButton(text='Назад 🔙', callback_data='back')
    # Добавляем кнопки в пространство
    kb.add(order, clear)
    kb.row(back)

    return kb

# Кнопки админ-панели
# Админ меню
def admin_menu():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    but1 = types.KeyboardButton('Добавить продукт')
    but2 = types.KeyboardButton('Удалить продукт')
    but3 = types.KeyboardButton('Изменить продукт')
    but4 = types.KeyboardButton('Перейти в главное меню')
    # Добавляем кнопки в пространство
    kb.add()
import telebot
import buttons, database


# Создаем объект бота
bot = telebot.TeleBot('8023649791:AAG5thGTPgZNGkShFVGgavyOHaHGisSSCJA')
# Хранилища временных данных
users = {}
admins = {}


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if database.check_user(user_id):
        bot.send_message(user_id, f'Добро пожаловать, @{message.from_user.username}!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(user_id, 'Выберите пункт меню:', reply_markup=buttons.main_menu(database.get_pr_buttons()))
    else:
        bot.send_message(user_id, 'Привет! Давай начнем регистрацию!\nНапиши свое имя',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        # Переход на этап получения имени
        bot.register_next_step_handler(message, get_name)


# Получение имени
def get_name(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, 'Отлично! Теперь отправь свой номер!',
                     reply_markup=buttons.num_button())
    # Переход на этап получения номера
    bot.register_next_step_handler(message, get_num, user_name)


# Выбор количества товара
@bot.callback_query_handler(lambda call: call.data in ['increment', 'decrement', 'to_cart', 'back'])
def choose_count(call):
    user_id = call.message.chat.id
    if call.data == 'increment':
        bot.edit_message_reply_markup(chat_id=user_id, message_id=call.message.message_id,
                                      reply_markup=buttons.choose_amount(
                                          database.get_exact_pr(users[user_id]['pr_name'])[4], 'increment',
                                          users[user_id]['pr_count']))
        users[user_id]['pr_count'] += 1
    elif call.data == 'decrement':
        bot.edit_message_reply_markup(chat_id=user_id, message_id=call.message.message_id,
                                      reply_markup=buttons.choose_amount(
                                          database.get_exact_pr(users[user_id]['pr_name'])[4], 'decrement',
                                          users[user_id]['pr_count']))
        users[user_id]['pr_count'] -= 1
    elif call.data == 'to_cart':
        pr_name = database.get_exact_pr(users[user_id]['pr_name'])[1]
        database.add_to_cart(user_id, pr_name, users[user_id]['pr_count'])
        bot.delete_message(chat_id=user_id, message_id=call.message.message_id)
        bot.send_message(user_id, 'Товар помещен в корзину! Желаете что-то ещё?',
                         reply_markup=buttons.main_menu(database.get_pr_buttons()))
    elif call.data == 'back':
        bot.delete_message(chat_id=user_id, message_id=call.message.message_id)
        bot.send_message(user_id, 'Переношу вас обратно в меню',
                         reply_markup=buttons.main_menu(database.get_pr_buttons()))


# Работа с корзиной
@bot.callback_query_handler(lambda call: call.data in ['order', 'clear', 'cart'])
def cart_handle(call):
    user_id = call.message.chat.id
    text = 'Ваша корзина: \n\n'
    if call.data == 'cart':
        user_cart = database.show_cart(user_id)
        total = 0.0
        for i in user_cart:
            text += (f'Товар: {i[1]}\n'
                     f'Количество: {i[2]}\n')
            total += database.get_exact_price(i[1])[0] * i[2]
        text += f'Итого: {round(total, 2)} сум'
        bot.delete_message(chat_id=user_id, message_id=call.message.message_id)
        bot.send_message(user_id, text, reply_markup=buttons.cart_buttons())
    elif call.data == 'clear':
        database.clear_cart(user_id)
        bot.delete_message(chat_id=user_id, message_id=call.message.message_id)
        bot.send_message(user_id, 'Корзина очищена!', reply_markup=buttons.main_menu(database.get_pr_buttons()))
    elif call.data == 'order':
        text = text.replace('Ваша корзина:', 'Новый заказ!')
        user_cart = database.show_cart(user_id)
        total = 0.0
        for i in user_cart:
            text += (f'Товар: {i[1]}\n'
                     f'Количество: {i[2]}\n')
            total += database.get_exact_price(i[1])[0] * i[2]
        text += f'Итого: {round(total, 2)} сум\n'
        bot.delete_message(chat_id=user_id, message_id=call.message.message_id)
        bot.send_message(user_id, 'Отправьте локацию, куда доставить ваш заказ!',
                         reply_markup=buttons.loc_button())
        # Переход на этап получения локации
        bot.register_next_step_handler(call.message, get_location, text)


# Этап получения локации
def get_location(message, text):
    user_id = message.from_user.id
    # Если локация была отправлена правильно
    if message.location:
        text += f'Клиент: @{message.from_user.username}'
        bot.send_message(6775701667, text)
        bot.send_location(6775701667, latitude=message.location.latitude, longitude=message.location.longitude)
        database.make_order(user_id)
        database.clear_cart(user_id)
        bot.send_message(user_id, 'Ваш заказ был принят, ожидайте!', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(user_id, 'Выберите пункт меню:', reply_markup=buttons.main_menu(database.get_pr_buttons()))
    else:
        bot.send_message(user_id, 'Отправьте локацию по кнопке или через скрепку!')
        # Возвращение на этап получения локации
        bot.register_next_step_handler(message, get_location, text)


# Получение номера
def get_num(message, user_name):
    user_id = message.from_user.id
    # Если отправил номер в виде номера
    if message.contact:
        user_num = message.contact.phone_number
        # Заносим пользователя в БД
        database.register(user_id, user_name, user_num)
        bot.send_message(user_id, 'Регистрация прошла успешно!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    # Если пользователь написал в виде текста
    else:
        bot.send_message(user_id, 'Отправьте контакт по кнопке или отправьте контакт через скрепку!')
        # Возврат на этап получения номера
        bot.register_next_step_handler(message, get_num, user_name)


@bot.callback_query_handler(lambda call: int(call.data) in [i[0] for i in database.get_all_pr()])
def choose_pr_count(call):
    # Определяем id пользователя
    user_id = call.message.chat.id
    # Достаем всю информацию о выбранном товаре
    pr_info = database.get_exact_pr(int(call.data))
    # Удаляем сообщение с выбором в меню
    bot.delete_message(chat_id=user_id, message_id=call.message.message_id)
    # Отправляем фото товара и его описание
    bot.send_photo(user_id, photo=pr_info[-1], caption=f'{pr_info[1]}\n\n'
                                                       f'Описание: {pr_info[2]}\n'
                                                       f'Количество: {pr_info[4]}\n'
                                                       f'Цена: {pr_info[3]} сум',
                   reply_markup=buttons.choose_amount(pr_info[4]))
    users[user_id] = {'pr_name': call.data, 'pr_count': 1}


# Обработчик команды /admin
@bot.message_handler(commands=['admin'])
def admin(message):
    if message.from_user.id == 6775701667:
        admin_id = message.from_user.id
        bot.send_message(admin_id, 'Добро пожаловать в админ-панель!', reply_markup=buttons.admin_menu())
        # Переход на этап выбора
        bot.register_next_step_handler(message, choice)
    else:
        bot.send_message(message.from_user.id, 'Вы не администратор!')


# Этап выбора
def choice(message):
    admin_id = message.from_user.id
    if message.text == 'Добавить продукт':
        bot.send_message(admin_id, 'Напишите данные о продукте в следующем виде:\n\n'
                                   'Название, Описание, Цена, Количество, Ссылка на фото\n\n'
                                   'Фотографии можно загрузить на сайте https://postimages.org/, '
                                   'скопировав прямую ссылку!', reply_markup=telebot.types.ReplyKeyboardRemove())
        # Переход на этап получения товара
        bot.register_next_step_handler(message, add_product)


# Добавление товара
def add_product(message):
    admin_id = message.from_user.id
    pr_attrs = message.text.split(', ')
    database.pr_to_db(pr_attrs[0], pr_attrs[1], pr_attrs[2], pr_attrs[3], pr_attrs[4])
    bot.send_message(admin_id, 'Готово!')


bot.polling(non_stop=True)

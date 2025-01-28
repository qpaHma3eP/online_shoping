import telebot
import buttons15treshina, database15treshina

# Создаём объект бота
bot = telebot.TeleBot('8023649791:AAG5thGTPgZNGkShFVGgavyOHaHGisSSCJA')

# Обработчик команды старт /start
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if database15treshina.check_user(user_id):
        bot.send_message(user_id, f'Добро пожаловать, @{message.from_user.username}!', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(user_id, 'Выбурите пункт меню:', reply_markup=buttons15treshina.main_menu(database15treshina.get_pr_buttons()))
    else:
        bot.send_message(user_id, 'Привет! Давай начнем регистрацию! Напиши своё имя', reply_markup=telebot.types.ReplyKeyboardRemove())
        # Переход на этап получения имени
        bot.register_next_step_handler(message, get_name)


#Получение имени
def get_name(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, 'Отлично! теперь отправь свой номер!', reply_markup=buttons15treshina.num_button())
    # Переход на этап получения номера
    bot.register_next_step_handler(message, get_num, user_name)
# Получение номера
def get_num(message, user_name):
    user_id = message.from_user.id
    # Если отправил номер в виде номера
    if message.contact:
        user_num = message.contact.phone_number
        # Заносим пользователя в БД
        database15treshina.register(user_id, user_name, user_num)
        bot.send_message(user_id, 'Регистрация прошла успешно!', reply_markup=telebot.types.ReplyKeyboardRemove())
    # Если пользователь написал в виде текста
    else:
        bot.send_message(user_id, 'Отправьте контакт по кнопке или отправьте контакт через скрепку 📎')
        # Возврат на этап получения номера
        bot.register_next_step_handler(message, get_name, user_name)


@bot.callback_query_handler(lambda call: int(call.data) in [i[0] for i in database15treshina.get_all_pr()])
def choose_pr_count(call):
    # Определяем айди пользователя
    user_id = call.message.chat.id
    # Достаем всю информацию о выбранном товаре
    pr_info = database15treshina.get_exact_pr(int(call.data))
    # Удаляем сообщение с выбором в меню
    bot.delete_message(chat_id=user_id, message_id=call.message.message_id)
    # Отправляем фото товара и его описание
    bot.send_photo(user_id, photo=pr_info[-1], caption=f'{pr_info[1]}\n\n'
                                                        f'Описание: {pr_info[2]}\n'
                                                        f'Количество: {pr_info[4]}\n'
                                                        f'Цена: {pr_info[3]} сум')

# Обработчик команды
@bot.message_handler(commands=['admin'])
def admin(message):
    if message.from_user.id == 6707505117:
        admin_id = message.from_user.id
        bot.send_message(admin_id, 'Добро пожаловать в админ панель!', reply_markup=buttons15treshina.admin_menu())
        # Переход на этап выбора
        bot.register_next_step_handler(message, choice)
    else:
        bot.send_message(message.from_user.id, 'Вы не Администратор!')

# Этап выбора
def choice(message):
    admin_id = message.from_user.id
    if message.text == 'Добавить продукт':
        bot.send_message(admin_id, 'Напишите данные о продукте в следующем виде:\n\n'
                                        'Название, Описание, Цена, Количество, Ссылка на фото\n\n'
                                        'Фотографии можно загрузить на сайте https://postimages.org/,'
                                        'скопировав прямую ссылку!', reply_markup=telebot.types.ReplyKeyboardRemove())
# Переход на этап получения товара
        bot.register_next_step_handler(message, add_product)

# Добавление товара
def add_product(message):
    admin_id = message.from_user.id
    pr_attrs = message.text.split(',')
    database15treshina.pr_to_db(pr_attrs[0], pr_attrs[1], pr_attrs[2], pr_attrs[3], pr_attrs[4])
    bot.send_message(admin_id, 'Готово!')


bot.polling(non_stop=True)

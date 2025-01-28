import telebot
from telebot import types
import sqlite3

# Токен вашего бота
bot = telebot.TeleBot('8055914771:AAHVDbUDYYltemVkwL1aIqYl7Z_RC1Il_yM')

# Ваш Telegram-канал
TELEGRAM_CHANNEL = 'https://t.me/motivation_for_each_day'

# Ваш Instagram-профиль
INSTAGRAM_PROFILE = 'https://www.instagram.com/dilshodjohnakromov/'

users = {}

# Создаем базу данных и таблицу пользователей
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, 
                   user_id INTEGER, 
                   first_name TEXT, 
                   phone_number TEXT, 
                   language TEXT)''')
conn.commit()


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Русский 🇷🇺', callback_data='lang_ru'))
    markup.add(types.InlineKeyboardButton('O‘zbekcha 🇺🇿', callback_data='lang_uz'))
    bot.send_message(chat_id, "Выберите язык / Tilni tanlang:", reply_markup=markup)


# Обработка выбора языка
@bot.callback_query_handler(func=lambda call: call.data.startswith('lang_'))
def language_handler(call):
    chat_id = call.message.chat.id
    language = call.data.split('_')[1]
    users[chat_id] = {'language': language}

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    if language == 'ru':
        markup.add(types.KeyboardButton('Отправить номер телефона📞', request_contact=True))
        bot.send_message(chat_id, "Пожалуйста, зарегистрируйтесь, отправив свой номер телефона.", reply_markup=markup)
    elif language == 'uz':
        markup.add(types.KeyboardButton('Telefon raqamni yuborish📞', request_contact=True))
        bot.send_message(chat_id, "Iltimos, telefon raqamingizni yuborib ro'yxatdan o'ting.", reply_markup=markup)


# Обработка контакта
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    chat_id = message.chat.id
    if message.contact is not None:
        user_id = message.from_user.id
        first_name = message.from_user.first_name
        phone_number = message.contact.phone_number
        language = users[chat_id]['language']

        # Сохраняем данные в базу данных
        cursor.execute("INSERT INTO users (user_id, first_name, phone_number, language) VALUES (?, ?, ?, ?)",
                       (user_id, first_name, phone_number, language))
        conn.commit()

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        if language == 'ru':
            markup.add(types.KeyboardButton('Отправить местоположение📍', request_location=True))
            bot.send_message(chat_id,
                             "Спасибо! Ваши данные сохранены. Теперь, пожалуйста, отправьте ваше местоположение.",
                             reply_markup=markup)
        elif language == 'uz':
            markup.add(types.KeyboardButton('Joylashuvingizni yuboring📍', request_location=True))
            bot.send_message(chat_id, "Rahmat! Ma'lumotlaringiz saqlandi. Endi joylashuvingizni yuboring.",
                             reply_markup=markup)


# Обработка местоположения
@bot.message_handler(content_types=['location'])
def location_handler(message):
    chat_id = message.chat.id
    language = users[chat_id]['language']

    markup = types.ReplyKeyboardRemove()
    if language == 'ru':
        bot.send_message(chat_id, f"Спасибо за регистрацию😉, {message.from_user.first_name}!", reply_markup=markup)
    elif language == 'uz':
        bot.send_message(chat_id, f"Ro'yxatdan o'tganingiz uchun rahmat😉, {message.from_user.first_name}!",
                         reply_markup=markup)

    # Добавляем кнопки для подписки на каналы
    inline_markup = types.InlineKeyboardMarkup()
    inline_markup.add(types.InlineKeyboardButton('Подписаться на Telegram-канал', url=TELEGRAM_CHANNEL))
    inline_markup.add(types.InlineKeyboardButton('Подписаться на Instagram', url=INSTAGRAM_PROFILE))
    bot.send_message(chat_id, "Не забудьте подписаться на наши каналы! / Kanallarimizga obuna bo'lishni unutmang!",
                     reply_markup=inline_markup)


# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    chat_id = message.chat.id
    cursor.execute("SELECT language FROM users WHERE user_id=?", (message.from_user.id,))
    result = cursor.fetchone()
    if result:
        language = result[0]
        if language == 'ru':
            bot.send_message(chat_id, "Справочная информация:\n\n"
                                      "/start - Начать работу с ботом и зарегистрироваться\n"
                                      "/help - Показать справочную информацию")
        elif language == 'uz':
            bot.send_message(chat_id, "Ma'lumotnoma:\n\n"
                                      "/start - Bot bilan ishlashni boshlang va ro'yxatdan o'ting\n"
                                      "/help - Ma'lumotnoma ko'rsatish")
    else:
        bot.send_message(chat_id, "Справочная информация:\n\n"
                                  "/start - Начать работу с ботом и зарегистрироваться\n"
                                  "/help - Показать справочную информацию")


# Дополнительная функция: Приветствие по имени
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_id = message.chat.id
    cursor.execute("SELECT first_name, language FROM users WHERE user_id=?", (message.from_user.id,))
    result = cursor.fetchone()
    if result:
        first_name = result[0]
        language = result[1]
        if language == 'ru':
            bot.send_message(chat_id, f"Привет, {first_name}! Как я могу помочь вам сегодня?")
        elif language == 'uz':
            bot.send_message(chat_id, f"Salom, {first_name}! Bugun qanday yordam bera olaman?")
    else:
        bot.send_message(chat_id, "Пожалуйста, зарегистрируйтесь, используя команду /start.")


# Запуск бота
bot.polling()

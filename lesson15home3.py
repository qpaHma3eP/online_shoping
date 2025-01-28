import telebot
from telebot import types

# Замените 'YOUR_BOT_API_KEY' на токен вашего бота
bot = telebot.TeleBot('8055914771:AAHVDbUDYYltemVkwL1aIqYl7Z_RC1Il_yM')

# Замените 'YOUR_TELEGRAM_CHANNEL' на ссылку на ваш Telegram-канал
TELEGRAM_CHANNEL = 'https://t.me/motivation_for_each_day'

# Замените 'YOUR_INSTAGRAM' на ссылку на ваш Instagram-профиль
INSTAGRAM_PROFILE = 'https://www.instagram.com/dilshodjohnakromov/'

users = {}

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(types.KeyboardButton('Отправить номер телефона📞', request_contact=True))
    bot.send_message(chat_id, "Добро пожаловать! Пожалуйста, зарегистрируйтесь, отправив свой номер телефона.", reply_markup=markup)

# Обработка контакта
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    chat_id = message.chat.id
    if message.contact is not None:
        users[chat_id] = {'phone_number': message.contact.phone_number}
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add(types.KeyboardButton('Отправить местоположение📍', request_location=True))
        bot.send_message(chat_id, "Спасибо! Теперь, пожалуйста, отправьте ваше местоположение.", reply_markup=markup)

# Обработка местоположения
@bot.message_handler(content_types=['location'])
def location_handler(message):
    chat_id = message.chat.id
    if message.location is not None:
        users[chat_id]['location'] = (message.location.latitude, message.location.longitude)
        markup = types.ReplyKeyboardRemove()
        bot.send_message(chat_id, f"Спасибо за регистрацию😉, {message.from_user.first_name}!", reply_markup=markup)

        # Добавляем кнопки для подписки на каналы
        inline_markup = types.InlineKeyboardMarkup()
        inline_markup.add(types.InlineKeyboardButton('Подписаться на Telegram-канал', url=TELEGRAM_CHANNEL))
        inline_markup.add(types.InlineKeyboardButton('Подписаться на Instagram', url=INSTAGRAM_PROFILE))
        bot.send_message(chat_id, "Не забудьте подписаться на мои каналы чтобы не пропустить свежие новости о моем блоге!", reply_markup=inline_markup)

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Справочная информация:\n\n"
                                      "/start - Начать работу с ботом и зарегистрироваться\n"
                                      "/help - Показать справочную информацию")

# Дополнительная функция: Приветствие по имени
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_id = message.chat.id
    if chat_id in users:
        bot.send_message(chat_id, f"Привет, {message.from_user.first_name}! Как я могу помочь вам сегодня?")
    else:
        bot.send_message(chat_id, "Пожалуйста, зарегистрируйтесь, используя команду /start.")

# Запуск бота
bot.polling()


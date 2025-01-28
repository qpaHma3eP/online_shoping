import telebot

# Замените 'YOUR_BOT_API_KEY' на токен вашего бота
bot = telebot.TeleBot('8055914771:AAHVDbUDYYltemVkwL1aIqYl7Z_RC1Il_yM')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Добро пожаловать в нашего бота.")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Справочная информация:\n\n"
                                      "/start - Начать работу с ботом\n"
                                      "/help - Показать справочную информацию")

# Запускаем бота
bot.polling()

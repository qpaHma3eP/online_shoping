import telebot
from forex_python.converter import CurrencyRates

# Создаем экземпляр бота c токеном
bot = telebot.TeleBot('7664404159:AAHl9J5hST2p8lye5Nz105sBoyLnPq5aRmM')

# Создаем экземпляр конвертера валют
c = CurrencyRates()


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Привет! Введите сумму в узбекских сумах, чтобы конвертировать в евро, доллары и рубли:")


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def convert_currency(message):
    try:
        # Получаем сумму от пользователя
        amount = float(message.text)

        # Конвертируем сумму в евро, доллары и рубли
        usd = c.convert('UZS', 'USD', amount)
        eur = c.convert('UZS', 'EUR', amount)
        rub = c.convert('UZS', 'RUB', amount)

        # Формируем ответ
        response = (f"Сумма в евро: {eur:.2f}\n"
                    f"Сумма в долларах: {usd:.2f}\n"
                    f"Сумма в рублях: {rub:.2f}")

        # Отправляем ответ пользователю
        bot.send_message(message.chat.id, response)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")


# Запускаем бота
bot.polling()






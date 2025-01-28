from fnmatch import translate

import telebot

import buttons
bot = telebot.TeleBot('7216888903:AAGWB3Nnbzcrzf-0Q7eTWtuGyHOZGGXmPzU') # Создаёт объект бота
# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'Привет! {message.from_user.username}!', reply_markup=buttons.menu())

@bot.message_handler(content_types=['text'])
def text(message):
    user_id = message.from_user.id
    if message.text.title() == 'Википедия':
        bot.send_message(user_id, 'Введите слово', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, wiki)
    elif message.text.title() == 'Переводчик':
        bot.send_message(user_id, 'Введите слово для перевода', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, translate)
    else: bot.send_message(user_id, 'Что-то пошло не так, нажмите /start')

def wiki(message):
        user_id = message.from_user.id
        if message.text.lower() == 'Сталин':
            bot.send_message(user_id, 'https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D0%BB%D0%B8%D0%BD,_%D0%98%D0%BE%D1%81%D0%B8%D1%84_%D0%92%D0%B8%D1%81%D1%81%D0%B0%D1%80%D0%B8%D0%BE%D0%BD%D0%BE%D0%B2%D0%B8%D1%87')
        elif message.text.lower() == 'Эскобар':
            bot.send_message(user_id, 'https://ru.wikipedia.org/wiki/%D0%AD%D1%81%D0%BA%D0%BE%D0%B1%D0%B0%D1%80,_%D0%9F%D0%B0%D0%B1%D0%BB%D0%BE')
        else:
            bot.send_message(user_id, 'К сожалению, я не знаю такое 🤷‍♂️')


def translate(message):
    user_id = message.from_user.id
    if message.text.lower() == 'Привет':
        bot.send_message(user_id, 'Hello')
    elif message.text.lower() == 'Пока':
        bot.send_message(user_id, 'Bye')
    else:
        bot.send_message(user_id, 'Пока не знаю такого перевода 🤷‍♂️')

bot.polling(non_stop=True) # Запуск бота




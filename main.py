import telebot
from telebot import types

bot = telebot.TeleBot('6846859554:AAFdQh64Z2L4-Rhpd24Du7soCJI46y3-UGo')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     ('Привет, Я бот - Sollan. Мне всего 1 день. '
                      'Пока что я умею только рассказывать одну историю. '
                      'Не хочешь послушать?. Напиши /story и что то произойдет'),
                     parse_mode='Markdown')


@bot.message_handler(commands=['story'])
def main(message):
    kb = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Да", callback_data='btn1')
    btn2 = types.InlineKeyboardButton(text="Нет", callback_data='btn2')
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Ты хочешь услышать мою историю?', reply_markup=kb)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1':
        bot.send_message(callback.message.chat.id,
                         ('Молодой программист принял участие в конкурсе от Умскул на создание телеграм бота,'
                          'который помогал людям с поиском работы. Он изучал документацию и писал код,'
                          'добавляя новые функции и улучшая проект. В конце конкурса его бот стал одним из самых популярных,'
                          'и он получил заслуженную победу. Участие в конкурсе помогло ему развить свои навыки программирования'
                          'и достичь новых целей.'))
    else:
        bot.send_message(callback.message.chat.id, 'Как жаль, а ведь тебя ждала интересная история :)')


bot.infinity_polling()
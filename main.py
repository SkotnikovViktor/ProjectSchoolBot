from telebot import *


bot = telebot.TeleBot('6920832884:AAEFhLQCmx2is5E462s6Wp5-sNmRftnsNSQ')

## Ввод команды в чат через \
## Команда /start предназначена для ознакомления пользователя с функциями бота
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Button_1')
    markup.add(item1)
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    about = f'Чтобы узнать больше о возможности бота и его командах <b> Введите /aboutbot </b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, about, parse_mode='html')




## Ввод команды через чат с помощью \
## Команда /aboutbot говорит о его функциях, что он может, и какие команды поддерживает
##@bot.message_handler(commands=['aboutbot'])
##def aboutbot(message):
##    bot.send_message(message.chat.id, "<b>Этот бота пока ещё в разработке.\nОн будет готов совсем скоро.</b>", parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.chat.type == 'private':
        if message.text == 'Button_1':
            bot.send_message(message.chat.id,"Привет!",parse_mode='html')
        elif message.text == 'id':
            bot.send_message(message.chat.id,f"Ваш id {message.id}")



bot.polling(none_stop=True)



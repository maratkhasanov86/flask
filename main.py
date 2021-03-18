import telebot

from telebot import types

bot = telebot.TeleBot("1530139786:AAFaCX0M8WMyl6le3KatS2MLyd5TVHFQPGM")
#основная клава
keyboard = types.InlineKeyboardMarkup()
key_olymp = types.InlineKeyboardButton(text='Олимпиада', callback_data='olymp')
keyboard.add(key_olymp)
key_urok = types.InlineKeyboardButton(text='Вопросы по урокам', callback_data='lesson')
keyboard.add(key_urok)




# олимпиада
keyboard_olymp = types.InlineKeyboardMarkup(row_width=3)
key_school = types.InlineKeyboardButton(text='Школьный', callback_data='school')
keyboard_olymp.add(key_school)
key_mynicip = types.InlineKeyboardButton(text='Муниципальный', callback_data='mynicip')
keyboard_olymp.add(key_mynicip)
key_region = types.InlineKeyboardButton(text='Региональный', callback_data='region')
keyboard_olymp.add(key_region)\

#регион
keyboard_region = types.InlineKeyboardMarkup()
key_zadachi_resps = types.InlineKeyboardButton(text='задачи с республиканских этапов олимпиад'
                                    ,callback_data='zadachi_resp')
key_cdacha_resp = types.InlineKeyboardButton(text='Где можно сдать задачи с регионального этапа'
                                    ,callback_data='cdacha')
keyboard_region.add(key_cdacha_resp)
keyboard_region.add(key_zadachi_resps)


#место для школьного, муниципа, всеросса


#клава для вопросов по уроку
keyboard_vopros = types.InlineKeyboardMarkup()
key_graph = types.InlineKeyboardButton(text='Graph', callback_data='graph')

key_codeblocks = types.InlineKeyboardButton(text='Где скачать CodeBlocks'
                                    ,callback_data='cs')
key_algoritm = types.InlineKeyboardButton(text='Где можно изучить все алгоритмы?'
                                    ,callback_data='algoritm')
keyboard_vopros.add(key_graph)
keyboard_vopros.add(key_algoritm)
keyboard_vopros.add(key_codeblocks)


#отвечает на команды по типу /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id,
                     f"Здравствуйте. Я телеграмм бот был создан, чтобы помочь Вам.\n Выберите ниже пункт, с которым Вам надо помочь",
                     parse_mode='html', reply_markup=keyboard)


#обработчик запросов
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "graph":
        bot.send_message(call.message.chat.id, 'Держите ссылку для скачивания Graph: https://bitly.su/wpJq1R')
    elif call.data == "olymp":
        bot.send_message(call.message.chat.id, "Выберите этап", parse_mode='html', reply_markup=keyboard_olymp)
    elif call.data == "school":
        bot.send_message(call.message.chat.id, 'Вот результаты школьного этапа:')
    elif call.data == "mynicip":
        bot.send_message(call.message.chat.id, 'Вот результаты муниципального этапа:')
    elif call.data == "region":
        bot.send_message(call.message.chat.id, 'Выберите дальнейшие действия', reply_markup=keyboard_region)
    elif call.data == "zadachi_resp":
        bot.send_message(call.message.chat.id, 'http://neerc.ifmo.ru/school/archive/2020-2021.html#region')
    elif call.data == "cs":
        bot.send_message(call.message.chat.id, 'Наберите в гугл скачать кодблокс) Не ну, а что, вариант.')
    elif call.data == "algoritm":
        bot.send_message(call.message.chat.id, 'Сайт e-maxx.ru')
    elif call.data == "cdacha":
        bot.send_message(call.message.chat.id, 'https://informatics.msk.ru/course/view.php?id=46')
    elif call.data == "lesson":
        bot.send_message(call.message.chat.id, "Выберите дальнейшие действия", reply_markup=keyboard_vopros)





# RUN
bot.polling(none_stop=True)

#1530139786:AAFaCX0M8WMyl6le3KatS2MLyd5TVHFQPGM

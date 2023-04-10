# instalando o telepot = pip install telepot


import time
from pprint import pprint

import telepot as tp
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup

from token_1 import token

bot = tp.Bot(token)

def on_chat_message(msg):
    content_type, chat_type, chat_id = tp.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Aperte', callback_data='Feito'),
        InlineKeyboardButton(text='Sim', callback_data='Ok'),
        InlineKeyboardButton(text='Não', callback_data='No'),
        InlineKeyboardButton(text='teste', callback_data='1')],
    ])

    bot.sendMessage(chat_id, 'Escolha a opção abaixo: ', reply_markup=keyboard)

def on_callback_query(msg):

    query_id, from_id, query_data = tp.glance(msg, flavor='callback_query')

    print('Callback Query: ', query_id, from_id, query_data)

    # print(msg) # mostra todos os dados
    bot.answerCallbackQuery(query_id, text='Apertou em '+str(query_data) )


MessageLoop(bot, {'chat': on_chat_message,
    'callback_query': on_callback_query}).run_as_thread()

print('Listening ...')

while 1:
    time.sleep(10)




# ====================================================================================

# print(bot.getMe())

# response = bot.getUpdates()
# pprint(response)

# resp = bot.sendMessage(1043367435, 'Ola, eu sou o WantBot!')
# resp = bot.sendMessage(1043367435, 'Como posso Ajudar?')

# def handle(msg):
#     pprint(msg)

# MessageLoop(bot, handle).run_as_thread()


# def handle(msg):
#     content_type, chat_type, chat_id = tp.glance(msg)
#     print(content_type, chat_type, chat_id)

#     if content_type == 'text':
#         bot.sendMessage(chat_id, msg['text']+ " <= Texto repetido.")

#     if content_type == 'audio':
#         pass


# bot = tp.Bot(token)
# MessageLoop(bot, handle).run_as_thread()
# print('Listening ...')

# while 1:
#     time.sleep(10)

# ====================================================================================

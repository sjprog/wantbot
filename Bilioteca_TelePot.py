# instalando o telepot = pip install telepot


import time
from pprint import pprint

import telepot as tp
from telepot.loop import MessageLoop

from token_1 import token

bot = tp.Bot(token)

# print(bot.getMe())

# response = bot.getUpdates()
# pprint(response)

# resp = bot.sendMessage(1043367435, 'Ola, eu sou o WantBot!')
# resp = bot.sendMessage(1043367435, 'Como posso Ajudar?')

# def handle(msg):
#     pprint(msg)

# MessageLoop(bot, handle).run_as_thread()


def handle(msg):
    content_type, chat_type, chat_id = tp.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text']+ " <= Texto repetido.")

    if content_type == 'audio':
        pass


# bot = tp.Bot(token)
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)

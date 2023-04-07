# instalando o telepot = pip install telepot


from pprint import pprint

import telepot as tp
from telepot.loop import MessageLoop

from token_1 import token

bot = tp.Bot(token)

# print(bot.getMe())

response = bot.getUpdates()
pprint(response)

resp = bot.sendMessage(1043367435, 'Ola, eu sou o WantBot!')
resp = bot.sendMessage(1043367435, 'Como posso Ajudar?')

def handle(msg):
    pprint(msg)

MessageLoop(bot, handle).run_as_thread()

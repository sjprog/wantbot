import telegram
from telegram.ext import CommandHandler, Updater

from token_1 import token_s

TOKEN = token_s
updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ola, eu sou o robo telegram!")

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

updater.start_polling()
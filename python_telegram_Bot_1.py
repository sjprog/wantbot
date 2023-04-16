import telegram
from telegram.ext import CommandHandler, MessageHandler, Updater, filters

from token_1 import token_s

TOKEN = token_s
updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ola, eu sou o robo telegram!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="repete = " +update.message.text)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(filters.TEXT & (~ filters.command), echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

updater.start_polling()
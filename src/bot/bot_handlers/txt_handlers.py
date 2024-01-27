from telebot.types import Message
from bot.setup_bot import BOT


@BOT.message_handler(commands=['start'])
def start(message: Message):
    BOT.reply_to(message, 'start')


@BOT.message_handler(commands=['help'])
def help(message: Message):
    BOT.reply_to(message, 'help')


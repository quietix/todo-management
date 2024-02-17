from telebot.types import Message
from bot.setup_bot import BOT
# from bot.models import User
from django.apps import apps


@BOT.message_handler(commands=['help', 'start'])
def help(message: Message):
    BOT.reply_to(message, message.text)

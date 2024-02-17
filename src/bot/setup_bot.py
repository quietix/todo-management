from bot import bot_wrapper
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage

state_storage = StateMemoryStorage()

BOT = bot_wrapper.BotWrapper(state_storage)

BOT.add_custom_filter(custom_filters.StateFilter(BOT))
BOT.add_custom_filter(custom_filters.TextMatchFilter())


class MyStates(StatesGroup):
    confirm_registration = State()

from telebot.types import Message
from bot.setup_bot import BOT, MyStates
from bot.db_manager import DBManager
from bot.interaction_manager import InteractionManager
from bot.response_phrases import variables
from telebot.custom_filters import TextFilter


db_manager = DBManager()
interaction_manager = InteractionManager()


# /start
@BOT.message_handler(commands=[variables.start_cmd])
def start(message: Message):
    interaction_manager.greet_user(message)
    interaction_manager.ask_registration(message.chat.id)
    BOT.set_state(message.from_user.id, MyStates.confirm_registration, message.chat.id)


# /help
@BOT.message_handler(commands=[variables.help_cmd])
def help(message: Message):
    interaction_manager.help_user(message)


# /register
@BOT.message_handler(commands=[variables.register_cmd])
def register(message: Message):
    BOT.set_state(message.from_user.id, MyStates.confirm_registration, message.chat.id)
    interaction_manager.ask_registration(message.chat.id)


# Register
@BOT.message_handler(state=MyStates.confirm_registration, text=TextFilter(equals=variables.ask_register_positive))
def confirm_registration(message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    if db_manager.register_user(user_id, first_name, last_name, username):
        interaction_manager.confirm_registration(message.chat.id)
        BOT.delete_state(message.from_user.id, message.chat.id)
    else:
        interaction_manager.already_registered(message.chat.id)


# Cancel
@BOT.message_handler(state=MyStates.confirm_registration, text=TextFilter(equals=variables.ask_register_negative))
def cancel_registration(message: Message):
    interaction_manager.cancel_registration(message.chat.id)
    BOT.delete_state(message.from_user.id, message.chat.id)

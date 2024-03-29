from bot.setup_bot import BOT
from telebot.types import Message
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from bot.response_phrases import variables
from bot.models import Section, SectionItem


class InteractionManager:
    # todo create function with suggestion of bot's functionality
    def greet_user(self, message: Message):
        BOT.reply_to(message, f"Hello, {message.from_user.first_name}!\n"
                              f"Register to use this service.")

    def help_user(self, message: Message):
        self.send_dulia(message.chat.id)

    def send_dulia(self, chat_id):
        BOT.send_sticker(chat_id, open('bot/downloads/_dulia.WEBP', 'rb'))

    def ask_registration(self, chat_id):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(variables.ask_register_positive), KeyboardButton(variables.ask_register_negative))
        BOT.send_message(chat_id, "Would you like to register?", reply_markup=markup)

    def confirm_registration(self, chat_id):
        BOT.send_message(chat_id, "Registration is successful!", reply_markup=ReplyKeyboardRemove())
        # TODO call suggestion method
        self.send_dulia(chat_id)

    def cancel_registration(self, chat_id):
        BOT.send_message(chat_id,
                         "Registration session is stopped. To register use /register command.",
                         reply_markup=ReplyKeyboardRemove())

    def already_registered(self, chat_id):
        BOT.send_message(chat_id,
                         "You are already registered. Enjoy the bot!",
                         reply_markup=ReplyKeyboardRemove())
        # TODO call suggestion method

    def send_sections(self, chat_id, sections: list[Section]):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2

        for i in range(0, len(sections), 2):
            section_name1 = sections[i].section_name
            section_name2 = sections[i + 1].section_name

            markup.add(InlineKeyboardButton(section_name1, callback_data=section_name1),
                       InlineKeyboardButton(section_name2, callback_data=section_name2))

        markup.add(InlineKeyboardButton("Add section", callback_data='add_section'))

        BOT.send_message(chat_id, "Your sections:", reply_markup=markup)

# TODO implement logger

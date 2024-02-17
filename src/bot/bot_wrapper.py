import os
import telebot
from dotenv import find_dotenv, load_dotenv
from telebot.storage import StateMemoryStorage


class BotWrapper(telebot.TeleBot):
    """
    Initializes <telebot.Telebot> object with token and webhook url taken from local .env file
    """
    def __init__(self, state_storage: StateMemoryStorage):
        token, url = self._get_data_for_bot()
        super().__init__(token, state_storage=state_storage)
        self.set_webhook(url)

    def _get_data_for_bot(self) -> (str, str):
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        token = os.getenv('TOKEN')
        webhook_url = os.getenv('DEV_SERVER_URL')
        return token, webhook_url

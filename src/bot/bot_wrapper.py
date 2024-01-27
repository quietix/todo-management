import os
import telebot
from dotenv import find_dotenv, load_dotenv


class BotWrapper(telebot.TeleBot):
    """
    Initializes <telebot.Telebot> object with token and webhook url taken from local .env file
    """
    def __init__(self):
        token, url = self._get_data_for_bot()
        super().__init__(token)
        self.set_webhook(url)

    def _get_data_for_bot(self) -> (str, str):
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        token = os.getenv('TOKEN')
        webhook_url = os.getenv('DEV_SERVER_URL')
        return token, webhook_url

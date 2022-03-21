import os

import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('telegram_token'))


def send_message_to_chat(chat_id: str, message: str) -> None:
    bot.send_message(chat_id, message, parse_mode="HTML")


if __name__ == '__main__':
    # bot.polling(none_stop=True, interval=0)
    send_message_to_chat("-1001758152269", "test")

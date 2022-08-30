import os

import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('telegram_token'))


async def send_message_to_chat(chat_id: str, message: str) -> None:
    bot.send_message(chat_id, message, parse_mode="MARKDOWN")


if __name__ == '__main__':
    # @bot.message_handler(content_types=['text'])
    # def text(message: Message):
    #     bot.send_message(message.chat.id, message.text)
    # bot.polling(none_stop=True, interval=0)
    send_message_to_chat("-1001758152269", "test")

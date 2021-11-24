import telebot
import httpx

token = """ваш токен"""


bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def content_messages(message):
    response = httpx.get(f'http://127.0.0.1:5000/send_msg/{message}')
    bot.send_message(message.from_user.id, response.text)


bot.infinity_polling()

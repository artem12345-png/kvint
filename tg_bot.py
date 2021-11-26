import telebot
import httpx

token = """1795434684:AAH268t1AvC7ajbexu7KNXOwIW4P_8onHDA"""


bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def content_messages(message):
    msg = message.json
    response = httpx.get(f"http://127.0.0.1:9999/send_msg/{msg.get('text', '')}/{msg.get('chat', '').get('id')}")
#    print(message.json)#['chat']['text'])
    print(response.text)
    bot.send_message(message.from_user.id, response.text)


bot.infinity_polling()

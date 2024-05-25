import telebot
import requests
import json

bot = telebot.TeleBot('')
API = ''



@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Happy to see you here. Hope the sun is shining. If you say where you are in this moment we will say about weather for sure')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'The weather now: {data["main"]["temp"]}')

        image = 'sunny.png' if temp > 5.0 else 'sun.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Inputed text is incorrect!')
bot.polling(none_stop=True)


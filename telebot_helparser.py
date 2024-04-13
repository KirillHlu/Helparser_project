import telebot
from telebot import types
import requests

city = ""

bot = telebot.TeleBot("7010721973:AAEFw5C5VxaI0wbRJDx2LxGiS76XEJJAnvY")

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup()
    btn3 = types.KeyboardButton('/weather')
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Hello, it is helparser, send /set_city to save your city.', reply_markup=markup)

@bot.message_handler(commands=['set_city'])
def set_city(message):
    global city
    city = message.text
    city = city.replace('/set_city ', '')
    bot.reply_to(message, f"Your city ({city}) has been saved, enter /weather to view the weather")

@bot.message_handler(commands=['weather'])
def get_weather(message):
    base_url = f"http://wttr.in/{city}?format=%t"
    response = requests.get(base_url)
    if response.status_code == 200:
        caption = f"The temperature is now in {city}: {response.text}"
        bot.send_photo(message.chat.id,'https://get.wallhere.com/photo/2560x1440-px-abstract-geometry-lake-landscape-minimalism-mountains-Sun-trees-1425123.jpg',caption=caption)
    else:
        bot.send_message(message.chat.id, "Not found.")

@bot.message_handler(content_types=['text'])
def talk(message):
    print("[log]: ", message.text)
    bot.reply_to(message,'Wrong request!')


bot.polling()

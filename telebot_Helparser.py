from telebot import types
import requests
from bs4 import BeautifulSoup
import time
import telebot
import qrcode
from io import BytesIO
import json

def load_users():
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}
    return users

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

city = "New York City"

bot = telebot.TeleBot("Token")

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('/commands')
    btn2 = types.KeyboardButton('/news')
    btn3 = types.KeyboardButton('/weather')
    markup.row(btn1, btn2, btn3)
    name = str(message.chat.first_name)
    bot.send_message(message.chat.id, f'Hello, {name}, it is helparser.\nSend me - /commands to see commands.', reply_markup=markup)

@bot.message_handler(commands=['qr'])
def generate_qr(message):
    try:
        link = message.text.split()
        link = link[1]
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(link)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")

        resized_image = qr_img.resize((300, 300))

        buffer = BytesIO()
        resized_image.save(buffer, format='PNG')
        buffer.seek(0)

        bot.send_photo(message.chat.id, photo=buffer)

    except IndexError:
        bot.reply_to(message, 'Send your link correctly, please!')

@bot.message_handler(commands=['commands'])
def start_message(message):
    bot.send_message(message.chat.id, '/set_city - set the city to view the weather in it (/set_city "city"). \n\n/weather - view the weather.\n\n/search_by_word - command for parsing a page by a specific word (/search_by_word link word).\n\n/search_by_inf - find the text according to the given information (/search_by_inf url class tag).\n\n/news - viewing the news of the world.\n\n/qr - create an Qr-code by link (/qr link)')

@bot.message_handler(commands=['set_city'])
def set_city(message):
    try:
        global city
        city = message.text
        city = city.split()
        city = city[1]
        bot.reply_to(message, f"Your city ({city}) has been saved, enter /weather to view the weather")

        users = load_users()
        city = city
        users[str(message.chat.first_name)] = {'City': city}
        save_users(users)

    except IndexError:
        bot.reply_to(message, f'Please, send your city correctly!')

@bot.message_handler(commands=['weather'])
def get_weather(message):
    with open('users.json', 'r') as file:
        data = json.load(file)
    city = data[str(message.chat.first_name)].get('City')
    base_url = f"http://wttr.in/{city}?format=%t"
    response = requests.get(base_url)

    if response.status_code == 200:
        caption = f"The temperature is now in {city}: {response.text}"
        bot.send_photo(message.chat.id,'https://get.wallhere.com/photo/2560x1440-px-abstract-geometry-lake-landscape-minimalism-mountains-Sun-trees-1425123.jpg',caption=caption)

    else:
        bot.send_message(message.chat.id, "Not found.")

@bot.message_handler(commands=['search_by_word'])
def search_by_word(message):
    try:
        word_and_link_for_search = message.text
        word_and_link_for_search = word_and_link_for_search.split()
        url = word_and_link_for_search[1]
        word = word_and_link_for_search[2]

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        word = word.lower()
        elements = soup.find_all(text=lambda text: word in text.lower())

        for element in elements:
            parent = element.parent
            if parent.name != 'script':
                bot.send_message(message.chat.id, f'Tag: {parent.name}\nClass: {parent.get("class")}\n Text: {element.strip()}\n')
                time.sleep(0.8)

    except IndexError:
        bot.reply_to(message, f'Please, send your information correctly!')

@bot.message_handler(commands=['search_by_inf'])
def search_by_inf(message):
    try:
        inf = message.text
        inf = inf.split()
        url = inf[1]
        class1 = inf[2]
        tag = inf[3]
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        data = soup.findAll(tag, class_=class1)

        bot.send_message(message.chat.id, f'The information from {url} ({tag}, {class1}): ')

        for i in data:
            bot.send_message(message.chat.id, f'\n{i.text}')
            time.sleep(0.8)

    except IndexError:
        bot.reply_to(message, f'Please, send your information correctly!')

@bot.message_handler(commands=['news'])
def search_by_word(message):
    response = requests.get('https://edition.cnn.com/world')
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.findAll('span', class_="container__headline-text")
    count = 0
    final_news = '🌍News🌎\n\n'

    for news in data:
        if count < 5:
            final_news = final_news + f'{news.text}\n\n'
            count = count + 1

        else:
            break

    bot.send_message(message.chat.id, final_news)

@bot.message_handler(content_types=['text'])
def talk(message):
    print("[log]: ", message.text)
    bot.reply_to(message,'Wrong request!')

bot.polling()

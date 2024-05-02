import flet as ft
from telebot import types
import requests
from bs4 import BeautifulSoup
import time
import telebot
import qrcode
from io import BytesIO
import json
from model import Parsing1

def main(page: ft.Page):
    page.title = "Helparser's telebot"

    def show_bs(e):
        bs.open = True
        bs.update()

    def close_bs(e):
        bs.open = False
        bs.update()

    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("The server was started!"),
                    ft.ElevatedButton("        Okay        ", on_click=close_bs),
                ],
                tight=True,
            ),
            padding=50,
        ),
        open=False,
    )
    page.overlay.append(bs),

    def show_bs2(e):
        bs2.open = True
        bs2.update()

    def close_bs2(e):
        bs2.open = False
        bs2.update()

    bs2 = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("Message sent successfully!"),
                    ft.ElevatedButton("        Okay        ", on_click=close_bs2),
                ],
                tight=True,
            ),
            padding=50,
        ),
        open=False,
    )
    page.overlay.append(bs2)

    def click2(self):
        text = tb1.value
        link = tb2.value
        ids = []
        with open('chat_ids.txt', 'r') as file:
            chat_ids = file.readlines()
            for chat_id in chat_ids:
                if chat_id in ids:
                    pass
                elif len(link) == 0:
                    token = 'TOKEN'
                    url = f'https://api.telegram.org/bot{token}/sendMessage'
                    params = {'chat_id': chat_id, 'text': text}
                    response = requests.get(url, params=params)
                    ids.append(chat_id)
                else:
                    token = 'TOKEN'
                    url_send_message = f'https://api.telegram.org/bot{token}/sendMessage'
                    url_send_photo = f'https://api.telegram.org/bot{token}/sendPhoto'

                    # Отправка фото
                    params_photo = {'chat_id': chat_id, 'photo': link, 'caption': text}
                    response_photo = requests.get(url_send_photo, params=params_photo)
                    ids.append(chat_id)
            ids = []
        show_bs2(self)


    def button_clicked(e):
        show_bs(e)
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

        bot = telebot.TeleBot("TOKEN")

        @bot.message_handler(commands=['start'])
        def start_message(message):
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('/commands')
            btn2 = types.KeyboardButton('/news')
            btn3 = types.KeyboardButton('/weather')
            markup.row(btn1, btn2, btn3)
            name = str(message.chat.first_name)
            bot.send_message(message.chat.id, f'Hello, {name}, it is helparser.\nSend me - /commands to see commands.',
                             reply_markup=markup),
            with open('chat_ids.txt', 'a') as file:
                file.write(str(message.chat.id) + '\n')

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
            bot.send_message(message.chat.id,
                             '/set_city - set the city to view the weather in it (/set_city "city"). \n\n/weather - view the weather.\n\n/search_by_word - command for parsing a page by a specific word (/search_by_word link word).\n\n/search_by_inf - find the text according to the given information (/search_by_inf url class tag).\n\n/news - viewing the news of the world.\n\n/qr - create an Qr-code by link (/qr link).\n\n/img - send images from the site (/img site).')

        @bot.message_handler(commands=['set_city'])
        def set_city(message):
            try:
                global city
                city = message.text
                city = city.replace('/set_city ', '')
                bot.reply_to(message, f"Your city ({city}) has been saved, enter /weather to view the weather")

                users = load_users()
                chat_id = message.chat.id
                user_id = message.from_user.id
                chat_member = bot.get_chat_member(chat_id, user_id)
                username = chat_member.user.username
                users[username] = {'City': city}
                save_users(users)

            except IndexError:
                bot.reply_to(message, f'Please, send your city correctly!')

        @bot.message_handler(commands=['weather'])
        def get_weather(message):
            try:
                with open('users.json', 'r') as file:
                    data = json.load(file)
                chat_id = message.chat.id
                user_id = message.from_user.id
                chat_member = bot.get_chat_member(chat_id, user_id)
                username = chat_member.user.username
                city = data[username].get('City')
                base_url = f"http://wttr.in/{city}?format=%t"
                response = requests.get(base_url)

                if response.status_code == 200:
                    caption = f"The temperature is now in {city}: {response.text}"
                    bot.send_photo(message.chat.id,
                                   'https://get.wallhere.com/photo/2560x1440-px-abstract-geometry-lake-landscape-minimalism-mountains-Sun-trees-1425123.jpg',
                                   caption=caption)

                else:
                    bot.send_message(message.chat.id, "Not found.")

            except KeyError:
                bot.reply_to(message, 'Please, send me your city (/set_city city) or make sure you have a username.')

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
                        bot.send_message(message.chat.id,
                                         f'Tag: {parent.name}\nClass: {parent.get("class")}\n Text: {element.strip()}\n')
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

        @bot.message_handler(commands=['img'])
        def search_images(message):
            try:
                url = message.text.replace('/img ', '')
                response = requests.get(url)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    images = soup.find_all('img')

                    for img in images:
                        img_url = img.get('src')
                        if img_url and img_url.startswith('http'):  # проверка начала строки img_url с подстроки 'http'.
                            bot.send_photo(message.chat.id, img_url)
                else:
                    bot.reply_to(message, 'Sorry, i cant find images!')

            except telebot.apihelper.ApiTelegramException:
                bot.reply_to(message, 'Sorry, i cant find images!')

        @bot.message_handler(content_types=['text'])
        def talk(message):
            chat_id = message.chat.id
            user_id = message.from_user.id
            chat_member = bot.get_chat_member(chat_id, user_id)
            username = chat_member.user.username
            bot.reply_to(message, 'Wrong request!')
            page.controls.append(ft.Text(f'{username}: {message.text}'))
            page.scroll = "always"
            page.update()

        bot.polling()

    weather = Parsing1().get_weather()

    main_root = ft.Row(
        [
            ft.Container(
                content=ft.Text(f'{weather} 🌤️'),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLUE,
                width=100,
                height=100,
                border_radius=10,
            ),
            ft.Row(
                [
                    ft.ElevatedButton("Start", on_click=button_clicked, data=0, width=250, height=100)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
    )

    tb1 = ft.TextField(label='Text')
    tb2 = ft.TextField(label='Link for image')
    btn = ft.ElevatedButton("Send", on_click=click2, data=0, width=250, height=100)

    def navigate(e):
        index = page.navigation_bar.selected_index
        page.clean()

        if index == 0:
            page.add(main_root)

        elif index == 1:
            page.add(tb1, tb2, btn)


    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(label='Main', icon=ft.icons.HOUSE),
            ft.NavigationDestination(label='Send message', icon=ft.icons.MAIL),
        ], on_change=navigate
    )

    page.add(main_root)


ft.app(target=main)

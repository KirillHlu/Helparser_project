from bs4 import BeautifulSoup
import requests
import pyttsx3
import json
from translation import translate1
import time
import os

class Parsing1:
    def news(self):
        with open('settings.json', 'r') as file:
            data = json.load(file)

        country = data["Country"]

        if country == 'Russia':
            url = 'https://ria.ru/location_rossiyskaya-federatsiya/'
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            news = soup.findAll('a', class_="list-item__title color-font-hover-only")
            news_list = []

            for i in news:
                i = i.text
                news_list.append(i)
                time.sleep(0.2)

            return news_list

        elif country == 'United States of America':

            news_list = []
            response = requests.get("https://www.cbsnews.com/us/")
            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.findAll('h4', class_="item__hed")

            for i in data:
                i = i.text
                i = i.split()
                i = " ".join(i)
                news_list.append(i)
                time.sleep(0.1)

            return news_list

        elif country == 'Japan':

            news_list = []
            response = requests.get("https://www.nikkei.com/")
            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.findAll('a', class_="fauxBlockLink_fzngw6j")

            for i in data:
                i = i.text
                i = i.split()
                i = " ".join(i)
                news_list.append(i)
                time.sleep(0.1)

            return news_list

        elif country == "United Kingdom":

            news_list = []
            response = requests.get("https://www.independent.co.uk/news/uk?CMP=ILC-refresh")
            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.findAll('a', class_="title")

            for i in data:
                i = i.text
                i = i.split()
                i = " ".join(i)
                news_list.append(i)
                time.sleep(0.1)

            return news_list

        elif country == "France":

            news_list = []
            response = requests.get("https://francais.rt.com/france?ysclid=luffwocxau48285105")
            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.findAll('a', class_="card__underline")

            for i in data:
                i = i.text
                i = i.split()
                i = " ".join(i)
                news_list.append(i)
                time.sleep(0.1)

            return news_list

        elif country == "Germany":

            news_list = []
            response = requests.get('https://www.tagesschau.de/inland')
            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.findAll('p', class_="teaser__shorttext")

            for i in data:
                i = i.text
                i = i.split()
                i = " ".join(i)
                news_list.append(i)
                time.sleep(0.1)

            return news_list

        elif country == "Mexico":

            news_list = []
            response = requests.get('https://diario.mx/')
            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.findAll('p', class_="texto_2")

            for i in data:
                i = i.text
                i = i.split()
                i = " ".join(i)
                news_list.append(i)
                time.sleep(0.1)

            return news_list

        else:
            news_list = translate1['Your country has no news']
            return news_list

    def get_weather(self):
        with open('settings.json', 'r') as file:
            data = json.load(file)

        city = data["City"]
        base_url = f"http://wttr.in/{city}?format=%t"

        response = requests.get(base_url)

        if response.status_code == 200:
            return response.text
        else:
            return ""

class Speak():
    def __init__(self):
        pass

    def text_to_speech(self, text):
        lang = ('ru')
        engine = pyttsx3.init()
        engine.setProperty('rate', 175)  # Устанавливаем скорость озвучивания
        engine.setProperty('voice', lang)  # Устанавливаем язык озвучивания
        engine.say(text)
        engine.runAndWait()


class Open_txt_class():
    def __int__(self):
        pass

    def open_first_txt(self):
        os.system('parsed_files1.txt')

    def open_second_txt(self):
        os.system('parsed_files2.txt')

    def open_third_txt(self):
        os.system('nice_news.txt')

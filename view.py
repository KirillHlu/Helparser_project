import json
import requests
from bs4 import BeautifulSoup
from model import Speak, Open_txt_class
from translation import translate1
import time
from tkinter import *
from PIL import ImageTk
import qrcode
from tkinter import ttk


class SettingsApp:
    def __init__(self):

        def settings_submit():
            language = self.choose_lang.get()
            country = self.choose_country.get()
            city = self.choose_city.get()
            if len(language) == 0 or len(country) == 0 or city == 0:
                pass
            else:
                data2 = {
                    "Country": country,
                    "City": city,
                    "Language": language
                }
                with open('settings.json', 'w') as file:
                    json.dump(data2, file)

        self.settings_root = Tk()
        self.settings_root.title(translate1['Settings'])
        self.settings_root.geometry('250x250')

        with open('settings.json') as f:
            data1 = json.load(f)
            default_country = data1["Country"]
            default_city = data1["City"]
            default_language = data1["Language"]

        language_var = StringVar(value=default_language)
        languages = ["English", 'Russian', 'German', "French", "Spanish", "Japanese", 'Chinese']

        country_var = StringVar(value=default_country)
        countries = [
            "United States of America", "Russia", "Japan",
            "United Kingdom", "France", "Germany", 'Mexico'
        ]

        city_var = StringVar(value=default_city)
        cities = [
            "Tokyo", "Paris", "London", "New York City", "Los Angeles",'Moscow',
            "Sydney", "Dubai", "Rome", "Moscow", "Beijing",
            "Mumbai", "Rio de Janeiro", "Cape Town", "Toronto", "Berlin",
            "Singapore", "Istanbul", "Bangkok", "Amsterdam", "Seoul",
            "Mexico City", "Cairo", "Dublin", "Barcelona", "Buenos Aires"
        ]

        self.text1 = Label(self.settings_root, text=translate1['Language: '])
        self.choose_lang = ttk.Combobox(self.settings_root, textvariable=language_var, values=languages, style='TCombobox')
        self.text2 = Label(self.settings_root, text=translate1['Country: '])
        self.choose_country = ttk.Combobox(self.settings_root, textvariable=country_var, values=countries, style='TCombobox')
        self.text3 = Label(self.settings_root, text=translate1['City:'])
        self.choose_city = ttk.Combobox(self.settings_root, textvariable=city_var, values=cities)
        self.btn1 = ttk.Button(self.settings_root, text=translate1['Submit'], command=settings_submit)

        self.text1.pack()
        self.choose_lang.pack()
        self.text2.pack()
        self.choose_country.pack()
        self.text3.pack()
        self.choose_city.pack()
        self.btn1.pack()

        self.settings_root.mainloop()



class SearchByWord():
    def __init__(self):
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.root.geometry('800x500')
        self.root.title(translate1['Search by word'])

        self.message1 = StringVar()
        self.message2 = StringVar()

        self.label1 = Label(self.root, width=500, height=800)
        self.text1 = ttk.Label(self.root, text=translate1['Link:'], font=("Arial", 15))
        self.enter1 = ttk.Entry(self.root, textvariable=self.message1, font=("Arial", 15))
        self.text2 = ttk.Label(self.root, text=translate1['Word:'], font=('Arial', 15))
        self.enter2 = ttk.Entry(self.root, textvariable=self.message2, font=("Arial", 15))
        self.found_text = Text(self.root, wrap='word', state='disabled', width=40, height=25)
        self.found_text.grid(row=0, column=0, padx=400, pady=20, sticky='nsew')
        self.btn1 = ttk.Button(self.root, text=translate1['Search'], padding=10, width=20, command=self.click11)
        self.btn2 = ttk.Button(self.root, text=translate1['Save inf'], padding=8, width=16, command=self.click12)
        self.btn3 = ttk.Button(self.root, text=translate1['Speak'], padding=10, width=20, command=self.click13)
        self.found_text.config(state='normal')

        self.found_text.tag_config("big", font=("Helvetica", 12))
        self.found_text.tag_add("big", "1.0", "end")


        self.label1.place(x=0, y=0)
        self.text1.place(x=10, y=10)
        self.enter1.place(x=10, y=50)
        self.text2.place(x=10, y=110)
        self.enter2.place(x=10, y=150)
        self.btn1.place(x=40, y=220)
        self.btn2.place(x=500, y=440)
        self.btn3.place(x=40, y=300)

        self.root.mainloop()



    def click11(self):
        found_inf = []
        index2 = 0
        url = self.enter1.get()
        word = self.enter2.get()

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        word = word.lower()

        elements = soup.find_all(text=lambda text: word in text.lower())

        for element in elements:
            parent = element.parent
            if parent.name != 'script':
                self.found_text.insert('end', f'Tag: {parent.name}\n')
                self.found_text.insert('end', f"Class: {parent.get('class')}\n")
                self.found_text.insert('end', f'Text: {element.strip()}\n\n')
                time.sleep(0.2)


    def click12(self):
        found_inf = []
        index2 = 0
        url = self.enter1.get()
        word = self.enter2.get()

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        word = word.lower()

        elements = soup.find_all(text=lambda text: word in text.lower())

        for element in elements:
            parent = element.parent
            if parent.name:
                with open('parsed_files1.txt', 'a', encoding='utf-8') as file:
                    file.write(f'Url: {url}')
                    file.write(f'\t\nTag: {parent.name}\n')
                    file.write(f"Class: {parent.get('class')}\n")
                    file.write(f'Text: {element.strip()}\n\n\n\n')
                    time.sleep(0.2)

    def click13(self):
        url = self.enter1.get()
        word = self.enter2.get()

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        word = word.lower()

        elements = soup.find_all(text=lambda text: word in text.lower())

        for element in elements:
            parent = element.parent
            if parent.name != 'script':
                Speak().text_to_speech(element.strip())
                time.sleep(0.2)





class SearchByInf:
    def __init__(self):
        self.root2 = Tk()
        self.root2.resizable(width=False, height=False)
        self.root2.geometry('800x500')
        self.root2.title(translate1['Search words'])

        self.message1 = StringVar()
        self.message2 = StringVar()
        self.message3 = StringVar()

        self.label1 = Label(self.root2, width=500, height=800)
        self.text1 = ttk.Label(self.root2, text=translate1['Link:'], font=("Arial", 15))
        self.text2 = ttk.Label(self.root2, text=translate1['Tag:'], font=('Arial', 15))
        self.text3 = ttk.Label(self.root2, text=translate1['Class:'], font=('Arial', 15))
        self.enter1 = ttk.Entry(self.root2, textvariable=self.message1, font=("Arial", 15))
        self.enter2 = ttk.Entry(self.root2, textvariable=self.message2, font=("Arial", 15))
        self.enter3 = ttk.Entry(self.root2, textvariable=self.message3, font=("Arial", 15))
        self.found_text = Text(self.root2, wrap='word', state='disabled', width=40, height=25)
        self.btn1 = ttk.Button(self.root2, text=translate1['Search'], padding=10, width=20, command=self.click21)
        self.btn2 = ttk.Button(self.root2, text=translate1['Save inf'], padding=8, width=16, command=self.click22)

        self.found_text.grid(row=0, column=0, padx=400, pady=20, sticky='nsew')
        self.found_text.config(state='normal')
        self.found_text.tag_config("big", font=("Helvetica", 12))
        self.found_text.tag_add("big", "1.0", "end")

        self.label1.place(x=0, y=0)
        self.text1.place(x=10, y=10)
        self.enter1.place(x=10, y=50)
        self.text2.place(x=10, y=110)
        self.enter2.place(x=10, y=150)
        self.text3.place(x=10, y=210)
        self.enter3.place(x=10, y=250)
        self.btn1.place(x=40, y=310)
        self.btn2.place(x=500, y=440)

        self.root2.mainloop()

    def click21(self):
        url = self.enter1.get()
        tag = self.enter2.get()
        class1 = self.enter3.get()

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        data = soup.findAll(tag, class_=class1)

        self.found_text.insert('end', f'The information from {url} ({tag}, {class1}): ')
        for i in data:
            self.found_text.insert('end', f'\n{i.text}')
            time.sleep(0.2)
        self.found_text.insert('end', f'\n\n\n')

    def click22(self):
        url = self.enter1.get()
        tag = self.enter2.get()
        class1 = self.enter3.get()

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        data = soup.findAll(tag, class1)

        with open('parsed_files2.txt', 'a', encoding='utf-8') as file:
            file.write(f'The information from {url} ({tag}, {class1}): ')
            for i in data:
                file.write(f'\n{i.text}')
                time.sleep(0.2)
            file.write(f'\n\n\n')

class QRCodeGenerator():
    def __init__(self):
        self.rootqr = Tk()
        self.rootqr.title("Qr code")
        self.rootqr.geometry('500x300')
        self.rootqr.resizable(width=False, height=False)

        self.url_label = Label(self.rootqr, text="Link:", font=("Arial", 15))
        self.url_label.place(x=40, y=40)

        self.url_entry = ttk.Entry(self.rootqr, font=("Arial", 15))
        self.url_entry.place(x=40, y=80)

        self.btn = ttk.Button(self.rootqr, text="Create an QR-code", command=self.btncommand1, width=20, padding=10)
        self.btn.place(x=80, y=150)
        self.rootqr.mainloop()

    def btncommand1(self):
        url = self.url_entry.get()
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)

        qr.add_data(url)
        qr.make(fit=True)
        qr_img = qr.make_image(fill='black', back_color='white')
        qr_img.save('Main_qr.png')
        qr_img_resized = qr_img.resize((80,80))
        qr_code_img = ImageTk.PhotoImage(qr_img_resized)
        self.qr_code_label = Label(image=qr_code_img)
        self.qr_code_label.image = qr_code_img
        self.qr_code_label.place(x=718, y=370)


class Txt_root():
    def __init__(self):
        self.root_txt = Tk()
        self.root_txt.geometry('450x250')
        self.root_txt.title('Open files')
        self.btn = ttk.Button(self.root_txt, text=translate1["By word"], command=Open_txt_class().open_first_txt, width=12, padding=20)
        self.btn2 = ttk.Button(self.root_txt, text=translate1["By inf"], command=Open_txt_class().open_second_txt, width=12, padding=20)
        self.btn3 = ttk.Button(self.root_txt, text=translate1["Nice news"], command=Open_txt_class().open_third_txt, width=12, padding=20)
        self.btn.place(x=15, y=90)
        self.btn2.place(x=150, y=90)
        self.btn3.place(x=285, y=90)
        self.root_txt.mainloop()

from view import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from translation import translate1
from model import Parsing1, Tg_bot
import datetime

class Main_root(Tk):
    def __init__(self):

        super().__init__()
        self.resizable(width=False, height=False)
        self.geometry('800x450')
        self.title(translate1['Helparser'])

        def save_news():
            news_list = Parsing1().news()

            current_datetime = datetime.datetime.now()

            with open('nice_news.txt', 'a', encoding='utf-8') as file:
                file.write(f"\n\n\n\nDate: {current_datetime}")
                file.write(f'\nNews: \n')
                for news in news_list:
                    file.write(f'\n{news}\n')

        self.news1 = Text(self, wrap="word", state="normal", width=41, height=20, background='#F3FFFF')
        self.news1.grid(row=0, column=0, padx=30, pady=30, sticky="nsew")
        self.btn1 = ttk.Button(text='👍🏻', padding=8, width=17, command=save_news)
        self.btn2 = ttk.Button(text='👎🏻', padding=8, width=17)
        self.btn3 = ttk.Button(text=translate1['Search by word'], padding=10, width=20, command=SearchByWord)
        self.btn4 = ttk.Button(text=translate1['Search by information'], padding=10, width=20, command=SearchByInf)
        self.btn5 = ttk.Button(text=translate1['Settings'], padding=10, width=20, command=SettingsApp)
        self.btn6 = ttk.Button(text=translate1['Qr-Code'], padding=10, width=20, command=QRCodeGenerator)
        self.btn7 = ttk.Button(text=translate1['Working with a parsed files'], command=Txt_root, padding=10, width=20)
        self.btn8 = ttk.Button(text=translate1['Telegram bot'], command=Tg_bot().open_link, padding=8, width=25)


        news_list = Parsing1().news()

        # Update the news1 Text widget with the news and time lists
        if translate1['Your country has no news'] in news_list:
            self.news1.insert(END, f'Try our tg bot!\n')
            self.news1.insert(END, f'https://t.me/helparser_bot\n\n\n')
            self.news1.insert(END, f'\n{news_list} \n\n\n')

        else:
            for news in news_list:
                self.news1.insert(END, f'\n{news} \n\n\n')

        self.news1.config(state="disabled")

        weather_info = Parsing1().get_weather()

        image = Image.open("images/weather1.jpg")
        draw = ImageDraw.Draw(image)

        if len(weather_info) == 5:
            font = ImageFont.truetype("arial.ttf", 160)  # Выбираем шрифт и размер текста
            draw.text((80, 430), weather_info, fill="White", font=font)
        else:
            font = ImageFont.truetype("arial.ttf", 180)  # Выбираем шрифт и размер текста
            draw.text((80, 420), weather_info, fill="White", font=font)

        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = Label(self, image=photo)
        label.image = photo

        image2 = Image.open("images/Main_qr.png")
        image2 = image2.resize((80, 80))
        photo2 = ImageTk.PhotoImage(image2)
        self.label2 = Label(self, image=photo2)
        self.label2.image2 = photo2

        self.btn1.place(x=42, y=380)
        self.btn2.place(x=220, y=380)
        self.btn3.place(x=400, y=180)
        self.btn4.place(x=600, y=180)
        self.btn5.place(x=500, y=100)
        self.btn6.place(x=400, y=260)
        self.btn7.place(x=600, y=260)
        self.btn8.place(x=485, y=330)
        label.place(x=680, y=00)
        self.label2.place(x=718, y=370)



if __name__ == "__main__":
    app = Main_root()
    app.mainloop()

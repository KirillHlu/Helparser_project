from view import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from translation import translate1
from model import Parsing1

class Main_root(Tk):
    def __init__(self):
        super().__init__()
        self.resizable(width=False, height=False)
        self.geometry('800x450')
        self.title(translate1['Helparser'])

        parser = Parsing1()

        self.news1 = Text(self, wrap="word", state="normal", width=41, height=20, background='#F3FFFF')
        self.news1.grid(row=0, column=0, padx=30, pady=30, sticky="nsew")
        self.btn1 = ttk.Button(text='👍🏻', padding=8, width=17)
        self.btn2 = ttk.Button(text='👎🏻', padding=8, width=17)
        self.btn3 = ttk.Button(text=translate1['Search by word'], padding=10, width=20, command=SearchByWord)
        self.btn4 = ttk.Button(text=translate1['Search by information'], padding=10, width=20, command=SearchByInf)
        self.btn5 = ttk.Button(text=translate1['Settings'], padding=10, width=20, command=SettingsApp)

        news_list, times_list, index = Parsing1().news()

        # Update the news1 Text widget with the news and time lists
        for i in range(index):
            self.news1.insert(END, f'\n{news_list[i]} - {times_list[i]} \n\n\n')

        self.news1.config(state="disabled")


        weather_info = Parsing1().get_weather()


        image = Image.open("weather1.jpg")
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



        self.btn1.place(x=42, y=380)
        self.btn2.place(x=220, y=380)
        self.btn3.place(x=500, y=100)
        self.btn4.place(x=500, y=200)
        self.btn5.place(x=500, y=300)
        label.place(x=680, y=00)


if __name__ == "__main__":
    app = Main_root()
    app.mainloop()

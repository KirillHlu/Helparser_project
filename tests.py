from tkinter import *
from PIL import ImageTk
import qrcode
from tkinter import ttk


class QRCodeGenerator:
    def __init__(self):
        self.rootqr = Tk()
        self.rootqr.title("Qr code")
        self.rootqr.geometry('650x300')
        self.rootqr.resizable(width=False, height=False)

        self.url_label = Label(self.rootqr, text="Link:", font=("Arial", 15))
        self.url_label.place(x=40, y=40)

        self.url_entry = ttk.Entry(self.rootqr, font=("Arial", 15))
        self.url_entry.place(x=40, y=80)

        self.btn = ttk.Button(self.rootqr, text="Create an QR-code", command=self.btncommand1, width=20, padding=10)
        self.btn.place(x=80, y=150)

        self.qr_code_img = None
        self.qr_code_label = None
        self.qr_images = []

    def btncommand1(self):
        url = self.url_entry.get()
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)

        qr.add_data(url)
        qr.make(fit=True)
        qr_img = qr.make_image(fill='black', back_color='white')
        qr_img_resized = qr_img.resize((200, 200))
        new_qr_code_img = ImageTk.PhotoImage(qr_img_resized)

        if self.qr_code_label:
            self.qr_code_label.destroy()

        # Destroy previous images from list
        for img in self.qr_images:
            img.__del__()

        self.qr_images = []  # Clear the list

        self.qr_code_img = new_qr_code_img
        self.qr_images.append(self.qr_code_img)

        self.qr_code_label = Label(self.rootqr, image=self.qr_code_img)
        self.qr_code_label.image = self.qr_code_img
        self.qr_code_label.place(x=350, y=25)

if __name__ == "__main__":
    qr_generator = QRCodeGenerator()
    qr_generator.rootqr.mainloop()

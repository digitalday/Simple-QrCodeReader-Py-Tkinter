from tkinter import *
import tkinter as tk
import tkinter.filedialog as fd


import qrcode
import cv2
from pyzbar import pyzbar
from PIL import ImageTk, Image


def upload():
    filename = fd.askopenfilename(title="Add QR", initialdir="/",
                                  filetypes=[('JPG file', '*.jpg'),
                                             ('PNG file', '*.png'),
                                             ('PDF file', '*.pdf')],)

    if filename:
        read = cv2.imread(filename)
        barcodes = pyzbar.decode(read)

        for barcode in barcodes:
            barcodedata = barcode.data.decode('utf-8')
            print(f'Result: {barcodedata}')
        text.insert(1.0, barcodedata)

        img = Image.open(filename)
        img = img.resize((250, 250))
        img = ImageTk.PhotoImage(img)

        panel.image = img
        panel.config(image=img)


def generate():

    name = fd.asksaveasfilename(filetypes=[('JPG file', '*.jpg'),
                                           ('PNG file', '*.png'),
                                           ('PDF file', '*.pdf')],
                                defaultextension='.png'
                                )

    if name:
        value = text.get(1.0, END)

        qimg = qrcode.make(value)
        type(qimg)  # qrcode.image.pil.PilImage
        qimg.save(name)

        img = Image.open(name)
        img = img.resize((250, 250))
        img = ImageTk.PhotoImage(img)

        panel.image = img
        panel.config(image=img)
        text.delete(1.0, END)


root = tk.Tk()  # Окно
root.title('QrCodeReader')  # title
root.config(bg='#EFEAEB')
root.geometry("600x600+40+40")  # размер и положение
root.resizable(False, False)  # возможность изменять размер окна
logo = tk.PhotoImage(file='myQrCode.png')  # добавляем логотип к переменной лого
root.iconphoto(False, logo)  # присовение нашего логотипа к приложению
label_logo = tk.Label(root, text='QrCodeReader',  # создание текста
                      bg='#EFEAEB',  # фон шрифта для текста
                      font=('Arial', 24, 'bold')  # шрифт
                      )
label_logo.pack(pady=5)  # добавление текста в приложение

upload_button = tk.Button(root, text='Upload QR',
                          command=upload,


                          )
panel = tk.Label(root)
img = Image.open('QrWelcome.png')
img = img.resize((250, 250))
img = ImageTk.PhotoImage(img)

panel.image = img
panel.config(image=img)
panel.pack(pady=5)

text = Text(root, height=10, width=45,
           font="Arial 14",
           wrap=WORD)


text.pack(pady=5)


upload_button.place(x=325, y=560)

generate_button = tk.Button(root, text='Genrate New Qr',
                            command=generate
                            )
generate_button.place(x=160, y=560)


root.mainloop()

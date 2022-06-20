import tkinter as tk
import tkinter.filedialog as fd
from tkinter import *
from tkinter import messagebox as mbox


import qrcode
from pyzbar.pyzbar import decode
from PIL import Image,ImageTk


def onInfo():
    mbox.showinfo("Информация", "Ваш QR код сгенерирован")

def onError():
    mbox.showerror("Ошибка", "Не могу открыть файл")



def upload():
    filename = fd.askopenfilename(filetypes=[('JPG file', '*.jpg'),
                                           ('PNG file', '*.png'),
                                           ('PDF file', '*.pdf')],
                                defaultextension='.png'
                                )
    if filename:
        decocdeQR = decode(Image.open(filename))
        decodedt = decocdeQR[0].data.decode('utf-8')
        text.delete(0.1,END)
        text.insert(0.1,decodedt)
    else:
        onError()
        


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
        onInfo()


root = tk.Tk()  # Окно
root.title('QrCodeReader')  # title
root.config(bg='#EFEAEB')
root.geometry("600x600+40+40")  # размер и положение
root.resizable(False, False)  # возможность изменять размер окна
logo = tk.PhotoImage(file='QrWelcome.png')  # добавляем логотип к переменной лого
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

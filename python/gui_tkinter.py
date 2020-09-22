# from tkinter import *
# window = Tk()
# window.geometry('800x500')

# def display():
#     getText = b.get()
#     label1= Label(text=getText,fg="black",bg="white").pack()
# b= StringVar()

# text1 = Entry(textvariable=b ).pack()
# button1 = Button(text="click Me", fg="yellow",bg="black",command=display).pack()

# window.mainloop()

# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import filedialog
# import os

# root = Tk()
# root.geometry("550x300+300+150")
# root.resizable(width=True, height=True)

# def openfn():
#     filename = filedialog.askopenfilename(title='open')
#     return filename
# def open_img():
#     x = openfn('layout_upper_part.png')
#     img = Image.open(x)
#     img = img.resize((250, 250), Image.ANTIALIAS)
#     img = ImageTk.PhotoImage(img)
#     panel = Label(root, image=img)
#     panel.image = img
#     panel.pack()

# btn = Button(root, text='open image', command=open_img).pack()

# root.mainloop()
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

path = 'layout_Upper_Part.PNG'

root = tk.Tk()
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
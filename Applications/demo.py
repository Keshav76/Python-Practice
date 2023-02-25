from tkinter import *
from random import randint

App = Tk()


def change():
    lbl.config(text=randint(1, 10000), font=('Arial', randint(5, 15)))


btn = Button(App, text='Change', command=change)
btn.pack()

lbl = Label(App, text='')
lbl.pack()

App.mainloop()

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

App = Tk()
App.title('App')
App.iconbitmap(r'./python.ico')


def show():
    img_loc = filedialog.askopenfilename(initialdir='C:', title='Open an Image', filetypes=(
        ('PNG Images', '*.png'),
        ('JPG Images', '*.jpg'),
        ('ICON Files', '*.ico'),
        ('BMP Images', '*.bmp'),
        ('All Files', '*.*')
    ))
    global img
    img = ImageTk.PhotoImage(Image.open(img_loc))
    lbl = Label(App, image=img)
    lbl.pack()
    Btn.destroy()


Btn = Button(App, text='Open', command=show)
Btn.pack()

App.mainloop()

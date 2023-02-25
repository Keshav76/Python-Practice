from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

App = Tk()
App.title('Image to Icon Converter')


def choose():
    global img_loc
    img_loc = filedialog.askopenfilename(initialdir='D:', title='Choose Your Image', filetypes=(
        ('PNG Image', '*.png'),
        ('JPG Image', '*.jpg'),
        ('All Files', '*.*')
    ))


Lbl1 = Label(App, text='Select your image:')
Lbl1.grid(row=0, column=0, padx=20, pady=5)
Btn1 = Button(App, text='Choose', command=choose)
Btn1.grid(row=0, column=1, padx=20, pady=5)

Lbl2 = Label(App, text='Select the icon size:')
Lbl2.grid(row=1, column=0, padx=20, pady=5)
size = StringVar()
Btn2 = OptionMenu(App, size, '16', '24', '32', '48', '64', '128', '255')
Btn2.grid(row=1, column=1, padx=20, pady=5)
size.set('16')


def convert():
    img = Image.open(img_loc)
    img.save('icon.ico', format='ICO', sizes=[(int(size.get()), int(size.get()))])
    success = Toplevel()
    success.geometry('250x100')
    success.title('Successful')
    lbl = Label(success, text='Image Converted to Icon successfully!!!')
    lbl.pack()


def show():
    prev = Toplevel()
    prev.geometry('150x100')
    prev.title('Icon')
    prev.iconbitmap('icon.ico')
    lbl = Label(prev, text='Check Your Icon!!')
    lbl.pack()
    prev.mainloop()


Btn3 = Button(App, text='Convert', command=convert)
Btn3.grid(row=2, column=0, padx=20, pady=5)
Btn4 = Button(App, text='Preview', command=show)
Btn4.grid(row=2, column=1, padx=20, pady=5)
App.mainloop()

from tkinter import *
from random import choice

App = Tk()
App.title('Random Generator')
App.geometry('350x300')
App['background'] = 'red'

Lbl = Label(App, text='Enter comma separated options:', background='red', foreground='white', relief='sunken', font=('Arial', 8))
Lbl.grid(row=0, column=0, padx=5, pady=10)

Inp = Entry(App, background='pink', foreground='red')
Inp.grid(row=0, column=1, padx=5, pady=10)


def find_rand():
    opt = 'Choice: ' + str(choice(Inp.get().split(',')))
    if check.get() == '2':
        opt += ', ' + str(choice(Inp.get().split(',')))

    ans.config(text=opt, font=('Arial', size.get()), relief='raised')

    Close['state'] = NORMAL


check = StringVar()
# Chk = Checkbutton(App, text='Two Output', variable=check, onvalue='2', offvalue='1', background='red', foreground='black')
# Chk.deselect()
# Chk.grid(row=1, column=0, columnspan=2)

rb1 = Radiobutton(App, text='One Output', variable=check, value='1', background='red', foreground='black')
rb2 = Radiobutton(App, text='Two Output', variable=check, value='2', background='red', foreground='black')
rb1.grid(row=1, column=0)
rb2.grid(row=1, column=1)
rb1.select()

size = IntVar()
sz = Scale(App, from_=5, to=15, variable=size, orient=HORIZONTAL, foreground='white', background='red')
sz.grid(row=2, column=0, columnspan=2)

Btn = Button(App, text='Generate', command=find_rand, background='black', foreground='white')
Btn.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

Close = Button(App, text='X', command=App.destroy, state=DISABLED, background='black', foreground='white', width=2)
Close.grid(row=0, column=2, padx=5, pady=10)


ans = Label(App, text='', foreground='white', background='red', font=('Arial', 0))
ans.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

val = StringVar()
menu = OptionMenu(App, val, 'White', 'Red', 'Blue', 'Purple', 'Cyan', 'Magenta', 'Yellow', 'Pink', 'Orange')
menu.grid(row=5, column=0, columnspan=2, padx=5, pady=10)
val.set('White')


def show():
    msg = Label(App, text='', background=val.get().lower(), width=20)
    msg.grid(row=7, column=0, columnspan=2, padx=5, pady=10)


B = Button(App, text='Show', command=show)
B.grid(row=6, column=0, columnspan=2, padx=5, pady=10)


App.mainloop()

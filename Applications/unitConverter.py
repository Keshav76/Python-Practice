from tkinter import *

App = Tk()
App.title('Unit Converter')
App.geometry('250x120')

From = StringVar()
Opt1 = OptionMenu(App, From, 'Inches', 'Foot', 'Metres')
Opt1.grid(row=0, column=0, padx=5, pady=5)
From.set('Inches')

lbl = Label(App, text='converts to')
lbl.grid(row=0, column=1, padx=0, pady=5)

To = StringVar()
Opt2 = OptionMenu(App, To, 'Inches', 'Foot', 'Metres')
Opt2.grid(row=0, column=2, padx=5, pady=5)
To.set('Inches')

lbl1 = Label(App, text='Enter the number:')
lbl1.grid(row=1, column=0, columnspan=2, padx=0, pady=5)

inp = Entry(App, width=5)
inp.grid(row=1, column=2, padx=5, pady=5)


def show():
    inch = float(inp.get())
    if From.get() == 'Foot':
        inch *= 12
    if From.get() == 'Metres':
        inch *= 39.37

    global ans
    ans = inch
    if To.get() == 'Foot':
        ans = inch/12
    if To.get() == 'Metres':
        ans = inch/39.37

    ans = str(round(ans, 2))

    msg = Label(App, text=ans)
    msg.grid(row=2, column=1, padx=0, pady=5)


Btn = Button(App, text='Convert', command=show)
Btn.grid(row=2, column=0, padx=20, pady=5)



App.mainloop()

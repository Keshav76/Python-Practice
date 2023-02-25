from tkinter import *
from random import randint

App = Tk()
App.geometry('225x145')
App.title('Dice Roller')
App['background'] = 'black'

dice = {
    0: '🎲',
    1: '⚀',
    2: '⚁',
    3: '⚂',
    4: '⚃',
    5: '⚄',
    6: '⚅'
}


def roll():
    rand = randint(1, 6)
    lbl = Label(App, text=str(dice[rand]), font=('Arial', 50), foreground='white', background='black')
    lbl.grid(row=0, column=0, padx=20, pady=5)



lbl = Label(App, text=str(dice[0]), font=('Arial', 50), foreground='white', background='black')
lbl.grid(row=0, column=0, padx=20, pady=5)

B = Button(App, text='Roll', command=roll, foreground='white', background='black', relief='ridge', width=25)
B.grid(row=1, column=0, padx=20, pady=5)

App.mainloop()

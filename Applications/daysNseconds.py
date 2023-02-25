from tkinter import *
from datetime import *

App = Tk()
App.title('Days and Seconds Calculator')
App.geometry('240x145')

Lbl = Label(App, text='Enter your Date of Birth: ')
Lbl.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

Lbl1 = Label(App, text='Date:')
Lbl1.grid(row=1, column=0, padx=5, pady=5)
dt = Entry(App, width=2)
dt.grid(row=1, column=1, padx=5, pady=5)

Lbl1 = Label(App, text='Month:')
Lbl1.grid(row=1, column=2, padx=5, pady=5)
mn = Entry(App, width=2)
mn.grid(row=1, column=3, padx=5, pady=5)

Lbl1 = Label(App, text='Year:')
Lbl1.grid(row=1, column=4, padx=5, pady=5)
yr = Entry(App, width=4)
yr.grid(row=1, column=5, padx=5, pady=5)


def show_days():
    dob = datetime(year=int(yr.get()), month=int(mn.get()), day=int(dt.get()), hour=00, minute=00, second=00)
    curr_time = datetime.now()
    time_diff = curr_time - dob
    msg = 'You have lived ' + str(time_diff.days) + ' days!'
    lbl = Label(App, text=msg)
    lbl.grid(row=3, column=0, columnspan=6)


def show_secs():
    dob = datetime(year=int(yr.get()), month=int(mn.get()), day=int(dt.get()), hour=00, minute=00, second=00)
    curr_time = datetime.now()
    time_diff = curr_time - dob
    msg = 'You have lived ' + str(time_diff.seconds) + ' seconds!'
    lbl = Label(App, text=msg)
    lbl.grid(row=4, column=0, columnspan=6)


Btn1 = Button(App, text='No of Days', command=show_days, width=12)
Btn1.grid(row=2, column=0, columnspan=3, pady=5)
Btn2 = Button(App, text='No of Seconds', command=show_secs, width=12)
Btn2.grid(row=2, column=3, columnspan=3, pady=5)

App.mainloop()

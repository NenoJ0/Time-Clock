from tkinter import Tk 
from tkinter import Label
import time

master = Tk()
master.title('clock time')

def get_time():
    timeVar = time.strftime('%I:%M:%S %p')
    clock.config(text=timeVar)
    clock.after(220, get_time)

clock = Label(master, font=('DS-Digital Italic', 100), bg='black', fg='#2BF90E')
clock.pack()
get_time()

master.mainloop()
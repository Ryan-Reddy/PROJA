from tkinter import *
import time


root = Tk()
root.title('')
root.geometry('600x400')


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    clock_label.config(text=hour + ':' + minute + ':' + second)


def update():
    clock_label.config(text='new text')


clock_label = Label(master=root, text=clock)
clock_label.pack(pady=20)

clock()

root.mainloop()
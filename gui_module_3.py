from module2moderatie import *
from tkinter import *
from PIL import Image, ImageTk
from read_from_twitter import grabtweets
from weather_api_importer import *
from geopylocation import *
import time

root = Tk()
root.title('Twitter zuil notificatiescherm')


stad = welke_stad()

def clicked_quit():
    yeslabel = Label(master=root, text='quit', command=quit())
    yeslabel.pack()


def grabfromtwitter():
    'YES'

# ????????????????????? Volgens mij is deze module plots kapot gegaan oid HELAAS GEEN LOGO..............:
# Logo image placement:
# pilimage = Image.Open("40px-Logo_NS.jpg")
# ns_logo = ImageTk.PhotoImage(pilimage)
# logo_label = Label(image=ns_logo)
# logo_label.pack(pady=15, padx=15)

# first message
label = Label(master=root,text='Welkom bij de NS Twitterzuil',height=2,bg='blue',fg='yellow',font= 'Times 32')
label.pack(pady=10, padx=17)

# first message
label = Label(master=root,text='in de stad: {}, postcode: {}'.format(stad[0],stad[1]),height=2,bg='blue',fg='yellow',font= 'Times 32')
label.pack(pady=10, padx=17)

label3 = Label(master=root,text='Laatste tweet: ',height=2,bg='blue',fg='white')
label3.pack(pady=10, padx=17)

# second message
label3 = Label(master=root,text=grabtweets(),height=2,bg='blue',fg='white')
label3.pack(pady=10, padx=17)


# gonna have to be a selective grab from DB
label3 = Label(master=root,text='Weersvoorspelling het komende uur: ',height=2,bg='blue',fg='white')
label3.pack(pady=1, padx=1)


# fourth message weather
label3 = Label(master=root,text=weatherget(),height=2,bg='blue',fg='white')
label3.config(height=8, width=70)
label3.pack(pady=50, padx=50)

# CLOCK
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime('%A')

    clock_label.config(text=hour + ':' + minute + ':' + second)
    clock_label.after(1000, clock)

    date_label.config(text='Vandaag is het: '+day)

def update():
    clock_label.config(text='new text')

date_label = Label(root, text='', font='Helvetica, 16', bg = 'blue', fg='white')
date_label.pack(pady=10)

clock_label = Label(master=root, text='', font='Helvetica, 42', bg='black', fg='green')
clock_label.pack(pady=20)
clock()






buttonYes = Button(master=root, text="quit", command=clicked_quit)
buttonYes.pack(padx=10,pady=10)

#weerbericht:
# weerbericht bij geen nieuwe tweets na ? minuten
# --- This is my weather importing tool, Will try to add this to the homescreen of module 3
from pprint import pprint
import requests
# pro.openweathermap.org/data/2.5/forecast/hourly?q={city name}&appid={API key}
# r = requests.get(
# pprint(r.json())


# post nieuwe tweets uit goedgekeurde tweets


root.mainloop()